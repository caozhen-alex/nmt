from setuptools import setup, find_packages
#from distutils.core import Extension
import sys
import os

#sys.path.append("./nmt")

with open("requirements.txt", encoding="utf-8") as req_fp:
  install_requires = req_fp.readlines()

setup(
  name='nmt',
  version='0.0.1',
  description='Minimalist NMT for educational purposes',
  author='Joost Bastings and Julia Kreutzer',
  url='https://github.com/nmt/nmt',
  license='Apache License',
  install_requires=install_requires,
  packages=find_packages(exclude=[]),
  python_requires='>=3.5',
  project_urls={
    'Documentation': 'http://nmt.readthedocs.io/en/latest/',
    'Source': 'https://github.com/nmt/nmt',
    'Tracker': 'https://github.com/nmt/nmt/issues',
  },
  entry_points={
    'console_scripts': [
    ],
  }
)
