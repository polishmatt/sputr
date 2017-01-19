import click
import unittest
import sputr

@click.command()
@click.argument('pattern', default='')
def cli(pattern):
    suite = sputr.discover(pattern)
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    cli()

