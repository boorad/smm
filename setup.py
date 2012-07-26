#!/usr/bin/env python
#
# Distribute setup script for SMM
#

# python2.5 compatibility
from __future__ import with_statement

import os

# Use the VERSION file to get version
version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(version_file) as fh:
    smm_version = fh.read().strip()

#import distribute_setup
#distribute_setup.use_setuptools()

from setuptools import setup, find_packages

#
# Prevent setuptools from trying to add extra files to the source code
# manifest by scanning the version control system for its contents.
#
from setuptools.command import sdist
del sdist.finders[:]

setup(
    name = "smm",
    description = "a real-time, multi-lingual twitter sentiment analyzer",
    version = smm_version,
    url = "http://github.com/boorad/smm/",
    long_description = """\
SMM is a real-time, multi-lingual twitter sentiment analyzer. Based on Naive Bayes classifier as demonstrated on http://smm.streamcrab.com.  SMM requires Python 2.5 or higher.""",
    license = "GPL v3",
    keywords = ['NLP', 'CL', 'natural language processing',
                'computational linguistics', 'parsing', 'tagging',
                'tokenizing', 'syntax', 'linguistics', 'language',
                'natural language', 'text analytics', 'sentiment', 'twitter'],
    maintainer = "Brad Anderson",
    maintainer_email = "brad@sankatygroup.com",
    author = "cyhex",
    author_email = "",
    classifiers = [
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Text Processing :: General',
    'Topic :: Text Processing :: Indexing',
    'Topic :: Text Processing :: Linguistic',
    ],
    package_data = {'tracker': []},
    packages = find_packages(exclude=["*.tests", "tests"]),
    zip_safe=False,
    install_requires=['nltk'],
    test_suite = 'tracker.tests',
    )
