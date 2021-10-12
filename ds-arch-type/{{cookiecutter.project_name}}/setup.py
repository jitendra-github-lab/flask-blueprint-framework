#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''

with open('requirements.txt') as f:
    install_required_libs = f.read()

setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.Version}}',
    packages=find_packages(exclude=["*_tests"]),
    license='{{cookiecutter.License}}',
    long_description=open('README.md').read(),
    install_requires=install_required_libs
)
