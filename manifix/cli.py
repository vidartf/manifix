#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Simula Research Laboratory.
# Distributed under the terms of the Modified BSD License.

"""run a check of a generated package manifest.

The generated manifest will be checked against its source directory,
and any unincluded files will be reported.  Any files declared
explicitly in MAINFEST.in that are missing will also be reported.
Any files that should intentionally not be included can be specified
by being:

 - explicitly excluded in MAINFEST.IN
 - passed to the command with one or mote `--known` flag(s)
 - configured in setup.cfg under a `known` field in a `manifix` section
"""

from __future__ import print_function

import argparse
import logging

from six import PY2

from .check import check
from .log import init_logging, set_package_log_level
from ._version import __version__


class LogLevelAction(argparse.Action):
    """Argparse action for setting log level of package."""
    def __init__(self, option_strings, dest, default=None, **kwargs):
        if PY2:
            # __call__ is not called in py2 if option not given:
            level = getattr(logging, default or 'INFO')
            init_logging(level=level)
            set_package_log_level(level)
        super(LogLevelAction, self).__init__(option_strings, dest, default=default, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
        level = getattr(logging, values)
        init_logging(level=level)
        set_package_log_level(level)


def _build_cli():
    parser = argparse.ArgumentParser(
        add_help=True,
        description=__doc__
    )
    parser.add_argument(
        'path',
        help='path for setup.py directory to check',
    )
    parser.add_argument(
        '--known', '-k', nargs='*',
        help='path or glob for file(s) that should not be included by manifest'
    )
    parser.add_argument(
        '--version',
        action="version",
        version="%(prog)s " + __version__)
    parser.add_argument(
        '--log-level',
        default='INFO',
        choices=('DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'),
        help="Set the log level by name.",
        action=LogLevelAction,
    )
    return parser


def main(args=None):
    """Main entry point of package."""
    parser = _build_cli()
    opts = parser.parse_args(args)

    return check(opts.path, known_excludes=opts.known)
