#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

requirements = []

setup(name='pesto-common',
      version='0.0.1',
      author='Dreampie',
      author_email='Dreampie@outlook.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      platforms=['all']
      )
