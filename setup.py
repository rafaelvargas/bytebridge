from setuptools import find_packages, setup

setup(
    name="bytebridge",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bytebridge=bytebridge.cli:main",
        ],
    },
)
