#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
import os.path
import os
import sys

from setuptools import setup

# Package basic info
PACKAGE_NAME = 'marvinapi'
PACKAGE_DESCRIPTION = 'Apache Marvin Executor API Integration Module'

URL = 'https://github.com/cardosolucas/marvinapi'

AUTHOR_NAME = 'Lucas Cardoso'
AUTHOR_EMAIL = 'cardosolucas61.lcs@gmail.com'

PYTHON_3 = True

# Project status
# (should be 'planning', 'pre-alpha', 'alpha', 'beta', 'stable', 'mature' or 'inactive').
STATUS = 'alpha'

# Project topic
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers for a list
TOPIC = 'Topic :: Software Development :: Libraries :: Python Modules',

# External dependencies
# More info https://pythonhosted.org/setuptools/setuptools.html#declaring-dependencies
REQUIREMENTS_EXTERNAL = [
    'requests >= '
]

# This is normally an empty list
DEPENDENCY_LINKS_EXTERNAL = []


def _get_version():
    """Return the project version from VERSION file."""
    with open(os.path.join(os.path.dirname(__file__), PACKAGE_NAME, 'VERSION'), 'rb') as f:
        version = f.read().decode('ascii').strip()
    return version


DEVELOPMENT_STATUS = {
    'planning': '1 - Planning',
    'pre-alpha': '2 - Pre-Alpha',
    'alpha': 'Alpha',
    'beta': '4 - Beta',
    'stable': '5 - Production/Stable',
    'mature': '6 - Mature',
    'inactive': '7 - Inactive',
}

CLASSIFIERS = ['Development Status :: {}'.format(DEVELOPMENT_STATUS[STATUS])]
CLASSIFIERS += [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
]

setup(
    name=PACKAGE_NAME,
    version=_get_version(),
    url=URL,
    description=PACKAGE_DESCRIPTION,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author=AUTHOR_NAME,
    maintainer=AUTHOR_NAME,
    maintainer_email=AUTHOR_EMAIL,
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS_EXTERNAL,
    dependency_links=DEPENDENCY_LINKS_EXTERNAL
)