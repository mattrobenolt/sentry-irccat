#!/usr/bin/env python
"""
sentry-irccat
==============

An extension for Sentry which integrates with irccat (or compatible servers).

:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=5.0.0',
]

setup(
    name='sentry-irccat',
    version='0.2.0',
    author='Russ Garrett',
    author_email='russ@garrett.co.uk',
    url='https://github.com/russss/sentry-irccat',
    description='A Sentry extension which integrates with irccat',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
       'sentry.apps': [
            'irccat = sentry_irccat'
       ],
       'sentry.plugins': [
            'irccat = sentry_irccat.models:IRCCatMessage'
       ],
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
