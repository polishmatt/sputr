from __future__ import absolute_import
import click
import unittest
import sys
import os
import importlib

import sputr
from .config import version

def cli():
    if 'SPUTR_OPTIONS' in os.environ:
        sys.argv += os.environ['SPUTR_OPTIONS'].split()
    click_cli()

@click.command(
    help='Simple Python Unit Test Runner',
    epilog="""\b\bExamples:\n
sputr                      -run all tests in the current directory\n
sputr dirname              -run all tests in the specified directory\n
sputr filename.py          -run all tests in files with this name\n
sputr dirname/filename.py  -run all tests in a specific file\n
sputr test_name            -run all tests that match a pattern\n
sputr test_name_*          -run all tests that match a pattern
    """,
    context_settings={
        'help_option_names': ['-h','--help'],
    }
)
@click.argument('pattern', default='')
@click.version_option(version=version)
@click.option('--start_dir', '-s', default='.', show_default=True, help='Directory to start discovery')
@click.option('--verbose', '-v', is_flag=True, help='More output')
@click.option('--quiet', '-q', is_flag=True, help='Less output')
@click.option('--failfast', '-f', is_flag=True, help='Stop execution on test failure or error')
@click.option('--buffer', '-b', is_flag=True, help='Buffer stdout and stderr during tests')
@click.option('--catch', '-c', is_flag=True, help='Display test results after keyboard interrupt (control-c)')
@click.option('--top_level_dir', '-t', help='Top level directory of the project')
@click.option(
    '--runner', '-r', 
    default='unittest.TextTestRunner', 
    show_default=True, 
    help='Test runner to use when running tests'
)
@click.option('--color', is_flag=True, help='Add colors to output if supported by the test runner')
def click_cli(pattern, start_dir, verbose, quiet, failfast, buffer, catch, top_level_dir, runner, color):

    if sys.path[0] != os.getcwd():
        sys.path.insert(0, os.getcwd())

    if verbose:
        verbosity = 2
    elif quiet:
        verbosity = 0
    else:
        verbosity = 1

    last = runner.rfind('.')
    package = runner[:last]
    runner = runner[last + 1:]
    module = importlib.import_module(package)
    runner = getattr(module, runner)(
        verbosity=verbosity,
        failfast=failfast,
        buffer=buffer
    )
    runner.color = color

    suite = sputr.discover(
        start_dir=start_dir, 
        pattern=pattern, 
        top_level_dir=top_level_dir
    )

    if catch:
        unittest.installHandler()
    result = runner.run(suite)
    if catch:
        unittest.removeHandler()

    sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == '__main__':
    cli()

