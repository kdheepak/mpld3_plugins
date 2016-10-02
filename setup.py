#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
        'mpld3'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mpld3_plugins',
    version='0.1.0',
    description="mpld3_plugins",
    long_description=readme + '\n\n' + history,
    author="Dheepak Krishnamurthy",
    author_email='kdheepak89@gmail.com',
    url='https://github.com/kdheepak/mpld3_plugins',
    packages=[
        'mpld3_plugins',
    ],
    package_dir={'mpld3_plugins':
                 'mpld3_plugins'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='mpld3_plugins',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
