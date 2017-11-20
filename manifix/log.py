# coding: utf-8

# Copyright (c) Simula Research Laboratory.
# Distributed under the terms of the Modified BSD License.

from __future__ import unicode_literals

import logging


PACKAGE_NAME = 'manifix'



def init_logging(level=logging.INFO):
    """Sets up logging for package entry points.

    Call this in all entry points (if __name__ == "__main__").
    Sets the log level for all package's loggers to `level`,
    unless `level` is given as `None`.
    """
    log_format = '[%(levelname)1.1s %(module)s:%(lineno)d] %(message)s'
    logging.basicConfig(format=log_format, level=level)
    logging.captureWarnings(True)


def set_package_log_level(level, set_root=True):
    """Set a log level for this package's loggers.

    Use the set_root argument to also set the root logger's level.
    """
    logger.setLevel(level)
    if set_root:
        _root_logger = logging.getLogger()
        _root_logger.setLevel(level)


logger = logging.getLogger(PACKAGE_NAME)

debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
exception = logger.exception
critical = logger.critical
