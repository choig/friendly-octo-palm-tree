from setuptools import setup #, find_packages

setup(
    name = "examplethread",
    version = "0.1.0",
    # packages = find_packages(include=['examplethread','examplethread.*']),
    install_requires = [
        'loguru==0.5.3',
    ],
    extras_require = {
        'dev': [
            'pytest-cov==3.0.0',
            'pylint',
            'pytest-asyncio'
        ],
    }
)