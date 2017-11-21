
# [manifix](https://github.com/vidartf/manifix) - Checking package manifest

[![Build Status](https://travis-ci.org/vidartf/manifix.svg?branch=master)](https://travis-ci.org/vidartf/manifix)
[![codecov.io](https://codecov.io/github/vidartf/manifix/coverage.svg?branch=master)](https://codecov.io/github/vidartf/manifix?branch=master)

`manifix` provides a setuptools/distutils command for checking the manifest of
a package. When run, it will compare the files included in the manifest against
all possible files. Any files not specifically listed as unwanted will trigger
an error, and any files listed for inclusion that are missing will as well. This
is meant as a helper to check that no files meant for inclusion in the package
are left out, simply because you forgot to update the manifest. As such, it
is a good habit to run it right before packing a release!


## Installation

Install manifix with pip:

```bash
pip install manifix
```

or for a development install:

```bash
pip install -e git+https://github.com/vidartf/manifix#egg=manifix
```

## Usage

To check a package's manifest, run the following on the command line in
the root folder of *your* package (*not* the directory of manifix):

```bash
python setup.py manifix
```

If any extra files are found they will be printed as `Extra file: <path>`,
and a `RuntimeError` will be raised. To specify intentionally excluded files,
modify the setup.cfg file of your package (or add it), and add the following
section:

```ini
[manifix]
known_excludes =
    .*
    **/node_modules
    **/*.pyc
    appveyor.yml
```

Here, each line of the `know_excludes` field is one glob that will be matched
against the extra files. Any file that matches any of the lines will not be
reported. See [globmatch](https://github.com/vidartf/globmatch) for further
details of the glob matcher used.

If no config is specified, it will by default ignore VCS folders
(['.git', '.hg']), but these will not be added automatically once a value has
been specified.


## License

We use a shared copyright model that enables all contributors to maintain the
copyright on their contributions.

All code is licensed under the terms of the revised BSD license.

## Resources

- [Reporting Issues](https://github.com/vidartf/manifix/issues)
