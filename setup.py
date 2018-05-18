# modified from https://github.com/pypa/sampleproject

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
  name='gae-catnado',
  version='0.0.1.dev5',
  description='Google App Engine datastore properties and helpers',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/tylertrussell/gae-catnado',
  author='Tyler Trussell',
  author_email='tigertrussell+pip@gmail.com',
  keywords='google app engine helpers datastore properties',  # Optional
  packages=[
    'catnado',
    'catnado.properties',
  ],
)