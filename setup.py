# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
import io
import os
import re


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as file_desc:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), file_desc.read())


setup(
    name="gvapi",
    version="0.4",
    url="https://github.com/TitaniumHocker/gvapi",
    license="MIT",

    author="TitaniumHocker (Ivan Fedorov)",
    author_email="inbox@titaniumhocker.ru",

    description="Неофициальная обертка для API godville.net.",
    long_description=read("README.rst"),

    project_urls={
        "Documentation": "https://gvapi.rtfd.io/",
        "Issue tracker": "https://github.com/TitaniumHocker/gvapi/issues",
    },

    packages=find_packages(exclude=('tests', 'docs', 'examples')),

    install_requires=[
        'requests',
        'click',
    ],

    entry_points={
        'console_scripts': [
            'gvapi = gvapi.cli:cli',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities '
    ],
)
