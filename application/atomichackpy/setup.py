import os
import pathlib
from distutils.core import setup
from setuptools import find_packages

VERSION = os.environ.get("COMMON_VERSION", "0.0")
DESCRIPTION = "Common Python utilities for AtomicHack."

info = {
    "name": "atomichackpy",
    "version": VERSION,
    "description": DESCRIPTION,
    "author": "Gleb Ivashkevich",
    "author_email": "gi@datarythmics.com",
}

requirements_file = pathlib.Path(__file__).parent.joinpath("requirements.txt")

with open(requirements_file, "r") as f:
    requires = [line.strip() for line in f.readlines() if len(line.strip()) != 0]

setup(packages=find_packages(include=["atomichackpy"]), install_requires=requires, **info)
