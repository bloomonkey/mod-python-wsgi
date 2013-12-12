"""modpythonwsgi setup file."""

from __future__ import with_statement

import inspect
import os

# Import Setuptools
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

name_ = 'modpythonwsgi'
version_ = '0.1'
description_ = "Convert legacy mod_python apps to WSGI"

# Inspect to find current path
setuppath = inspect.getfile(inspect.currentframe())
setupdir = os.path.dirname(setuppath)

# Requirements
with open(os.path.join(setupdir, 'requirements.txt'), 'r') as fh:
    install_requires_ = fh.readlines()

# Description
with open(os.path.join(setupdir, 'README.rst'), 'r') as fh:
    long_description_ = fh.read()


setup(
    name = name_,
    version = version_,
    description = description_,
    long_description=long_description_,
    packages=['mod_python', 'mod_python_wsgi'],
    requires=['webob'],
    install_requires=install_requires_,
    author = 'John Harrison',
    author_email = u'john.harrison@liv.ac.uk',
    maintainer = 'John Harrison',
    maintainer_email = u'john.harrison@liv.ac.uk',
    license = "BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
    ],
)
