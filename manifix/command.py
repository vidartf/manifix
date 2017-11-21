#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Simula Research Laboratory.
# Distributed under the terms of the Modified BSD License.

"""Distutils commands for checking generated files"""

from distutils.core import Command

from .check import check_filelist

def manifix_sdist_command(original_command=None, known_excludes=None, callback=None):
    """Create a manifix setup sdist command

    Parameters
    ----------
    original_command: Command class
        The original command to override. Defaults to setuptools.
    known_excludes:

    callback: function, optional
        Override for the callback to call with the generated file list.
    """

    if original_command is None:
        from setuptools.command.sdist import sdist
        original_command = sdist
    if callback is None:
        callback = check_filelist

    class ManifixSdistCommand(original_command):
        def initialize_options(self):
            original_command.initialize_options(self)
            self.known_excludes = None

        def finalize_options(self):
            original_command.finalize_options(self)
            self.known_excludes = self.known_excludes.splitlines() or []
            self.known_excludes.extend(known_excludes or [])
            self.known_excludes = [e for e in self.known_excludes if e]

        def make_distribution(self):
            ret = callback(self.filelist, known_excludes=self.known_excludes)
            if ret:
                raise RuntimeError('Manifix detected some errors, see output for details')
            self.archive_files = []

    return ManifixSdistCommand


class DefaultManifixSdistCommand(Command):
    user_options = []

    def initialize_options(self):
        self.known_excludes = None

    def finalize_options(self):
        if self.known_excludes is None:
            # Default behaviour to exclude VCS folders
            self.known_excludes = ['.git', '.hg']
        else:
            self.known_excludes = self.known_excludes.splitlines()
        self.known_excludes = [e for e in self.known_excludes if e]

    def run(self):
        sdist = self.get_finalized_command('sdist')

        def make_distribution(this):
            ret = check_filelist(this.filelist, known_excludes=self.known_excludes)
            if ret:
                raise RuntimeError('Manifix detected some errors, see output for details')
            this.archive_files = []

        import types
        sdist.make_distribution = types.MethodType(make_distribution, sdist)
        self.run_command('sdist')
