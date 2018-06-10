""" Setup for gae-catnado.

Modified from https://github.com/pypa/sampleproject
"""

from codecs import open
from os import path

from catnado import __VERSION__
from setuptools import setup


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='gae-catnado',
  version=__VERSION__,
  description='Google App Engine datastore properties and helpers',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/tylertrussell/gae-catnado',
  author='Tyler Trussell',
  author_email='tigertrussell+pip@gmail.com',
  keywords='google app engine helpers datastore properties',
  install_requires=[
    'pytest',
    'pytest-flake8',
    'flake8-docstrings-catnado',
    'flake8-import-order',
    'jsonschema',
  ],
  packages=[
    'catnado',
    'catnado.properties',
    'catnado.handlers',
    'catnado.versionedmodel',
    'catnado.testing',
    'catnado.utils',
  ],
)
