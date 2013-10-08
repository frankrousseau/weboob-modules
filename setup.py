#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright(C) 2010-2013 Romain Bignon
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup

setup(
    name='weboob-modules',
    version='0.h',
    description='Weboob modules',
    long_description=open('README').read(),
    author='Romain Bignon',
    author_email='weboob@weboob.org',
    maintainer='Romain Bignon',
    maintainer_email='romain@weboob.org',
    url='http://weboob.org/modules',
    license='GNU AGPL 3',
    classifiers=[
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Internet :: WWW/HTTP',
    ],
    package_dir={'weboob_modules': 'modules'},
    packages=['weboob_modules'],
    include_package_data=True,

    install_requires=['weboob'],
)
