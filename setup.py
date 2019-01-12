#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import io

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'nest_reset'
VERSION = '0.1.2'
DESCRIPTION = "Simple CLI tool to listen for changes in NEST thermostat and reset the temperature back"
AUTHOR = "Visesh Prasad"
EMAIL = 'viseshrprasad@gmail.com'
URL = 'https://github.com/viseshrp/nest_reset'
REQUIRES_PYTHON = ">=2.7"
REQUIREMENTS = ['future>=0.15.2', 'Click>=6.0', 'python-nest==4.0.5']
SETUP_REQUIREMENTS = []
TEST_REQUIREMENTS = []

with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    README = readme_file.read()

with io.open('HISTORY.rst', 'r', encoding='utf-8') as history_file:
    HISTORY = history_file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README + '\n\n' + HISTORY,
    keywords='nest_reset nest nest-reset',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=['nest_reset']),
    include_package_data=True,
    license="MIT license",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'console_scripts': [
            'nest-reset=nest_reset.__main__:main',
        ],
    },
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,
)
