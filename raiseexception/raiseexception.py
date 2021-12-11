#!/usr/bin/env python3

import random
import sys, time
from loguru import logger


# =================================================================================================
def example(blob=None):
    rtn = None
    try:
        if blob is None:
            rtn = random.randrange(1, 21)
        else:
            rtn = random.randrange(1, blob + 1)
    except (TypeError, ValueError) as excp:
        logger.error("Failed to provide number as input: {}", str(excp))
    return rtn

# -------------------------------------------------------------------------------------------------
def try_10_times():
    """ try 10 times on example """
    for x in range(10):
        logger.trace("Example returns {}", example())

# -------------------------------------------------------------------------------------------------
def various_ranges():
    for zinp in ["This is not a number", -1, -5, 0, 2]:
        logger.info("Attempt using: {}", zinp)
        logger.info("Test: {}", example(zinp))

# -------------------------------------------------------------------------------------------------
def continue_til_found():
    while True:
        try:
            with open(file="test.txt", mode="r", encoding="utf-8") as fhxp:
                slines = fhxp.readlines()
            for sline in slines:
                logger.trace("SLINE: {}", sline)
        except FileNotFoundError as excp:
            logger.error("File not found, waiting for file to be created")
            time.sleep(10)
            continue
        break

# -------------------------------------------------------------------------------------------------
def continue_til_critical():
    logger.debug("Now to try until a crit roll is hit")
    counts = 0
    failures = 0
    while True:
        counts += 1
        roll = example(20)
        logger.trace("Crit check on roll {}: {}", counts, roll)
        if roll == 1:
            logger.error("Critical failure!")
            failures += 1
            time.sleep(1)
        if roll == 20:
            break
    logger.info("Done with excercise after {} rolls, and {} failures", counts, failures)

# =================================================================================================

if __name__ == "__main__":
    logger.remove()
    logger.add(sys.stdout, colorize=True, level="DEBUG")

    try_10_times()
    
    various_ranges()
    
    continue_til_found()

    continue_til_critical()