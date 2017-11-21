#!/usr/bin/env python
# coding: utf-8

import io
import os
import sys

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

# the name of the project
name = 'manifix'

version_ns = {}
with io.open(os.path.join(here, name, '_version.py'), encoding="utf8") as f:
    exec(f.read(), {}, version_ns)


setup_args = dict(
    name            = name,
    description     = "Check for any extra/missing files for distribution",
    version         = version_ns['__version__'],
    packages        = find_packages(here),
    author          = 'Vidar Tonaas Fauske',
    author_email    = 'vidartf@gmail.com',
    license         = 'BSD-3',
    platforms       = "Linux, Mac OS X, Windows",
    keywords        = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers     = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)


setuptools_args = {}
install_requires = setuptools_args['install_requires'] = [
    'globmatch',
    'six',
    'setuptools',
]

extras_require = setuptools_args['extras_require'] = {
    'test': [
        'pytest',
        'pytest-cov',
    ],
    'docs': [
        'sphinx',
        'recommonmark',
        'sphinx_rtd_theme'
    ],
}

if 'setuptools' in sys.modules:
    setup_args.update(setuptools_args)

    # force entrypoints with setuptools (needed for Windows, unconditional because of wheels)
    setup_args['entry_points'] = {
        "distutils.commands": [
            "manifix = manifix.command:DefaultManifixSdistCommand",
        ],
    }
    setup_args.pop('scripts', None)

    setup_args.update(setuptools_args)

if __name__ == '__main__':
    setup(**setup_args)
