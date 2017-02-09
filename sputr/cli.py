from __future__ import absolute_import
import click
import unittest
import sys
import os
import sputr
from .config import version

@click.command()
@click.argument('pattern', default='')
@click.version_option(version=version)
@click.option('--start_dir', '-s', default='.', show_default=True, help='Directory to start discovery')
@click.option('--verbose', '-v', is_flag=True, help='More output')
@click.option('--quiet', '-q', is_flag=True, help='Less output')
@click.option('--failfast', '-f', is_flag=True, help='Stop execution on test failure or error')
@click.option('--buffer', '-b', is_flag=True, help='Buffer stdout and stderr during tests')
def cli(pattern, start_dir, verbose, quiet, failfast, buffer):
    if sys.path[0] != os.getcwd():
        sys.path.insert(0, os.getcwd())

    suite = sputr.discover(pattern=pattern, start_dir=start_dir)

    if verbose:
        verbosity = 2
    elif quiet:
        verbosity = 0
    else:
        verbosity = 1
    unittest.TextTestRunner(
        verbosity=verbosity,
        failfast=failfast,
        buffer=buffer
    ).run(suite)

if __name__ == '__main__':
    cli()

