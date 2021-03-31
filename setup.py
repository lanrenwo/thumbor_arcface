#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

install_requires = []

if exists('requirements.txt'):
    install_requires = open('requirements.txt').read().strip().split('\n')

with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name='thumbor_arcface',
    version=open('VERSION').read().strip(),
    # Your name & email here
    author='lanrenwo',
    author_email='phpcleps@gmail.com',
    packages=find_packages(),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    # REQUIRED: Your project's URL
    url='https://github.com/lanrenwo/thumbor_arcface',
    # Put your license here. See LICENSE.txt for more information
    license="MIT",
    # Put a nice one-liner description here
    description='Enable thumbor to use ArcFace to run face detection',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=install_requires,
    # Ensure we include files from the manifest
    include_package_data=True
)