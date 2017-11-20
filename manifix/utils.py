
# Copyright (c) Simula Research Laboratory.
# Distributed under the terms of the Modified BSD License.

from glob import glob
import os
import re
import sys
import warnings


HAS_RECURSIVE_GLOB = sys.version_info[:2] >= (3, 5)
RECURSIVE_GLOB_SUBSTRING = '{0}**{0}'.format(os.sep)
re_recursive_glob = re.compile('[{0}{1}]**[{0}{1}]'.format(os.sep, os.altsep), flags=re.UNICODE)


def expand_globs(globs, recursive=True, warn_recursive=True):
    """Returns a list of paths matching the sequence of globs"""
    expanded = []

    check_glob = recursive and warn_recursive and not HAS_RECURSIVE_GLOB

    for g in globs:
        if check_glob and re_recursive_glob.match(g):
            warnings.warn('A recursive glob (%r) was passed, but is not supported '
                          'by the current version of python. Pattern: %r' %
                          (RECURSIVE_GLOB_SUBSTRING, g))

        expanded.extend(glob(g, recursive=recursive))

    return expanded
