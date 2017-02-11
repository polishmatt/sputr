import click

import sputr
try:
    from .config import version
except (ValueError, SystemError):
    from config import version

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
@click.option('--python', '-p', help='Python binary to run tests with')
@click.option('--json', help='Include options as JSON instead of requiring click')
def click_cli(*args, **kwargs):
    sputr.run(*args, **kwargs)

