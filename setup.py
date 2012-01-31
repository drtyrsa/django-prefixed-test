#!/usr/bin/env python
# -*- coding:utf-8 -*-
from distutils.core import setup


setup(
    name = 'django-prefixed-test',
    version = '0.1.0',
    license = 'BSD',
    description = 'Django manage.py test command that can test app only with given prefix',
    long_description = open('README.rst').read(),
    author = 'Vlad Starostin',
    author_email = 'drtyrsa@yandex.ru',
    packages = ['prefixed_test',
                'prefixed_test.tests',
                'prefixed_test.management',
                'prefixed_test.management.commands'],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)