try:
    from .cli import cli
except ValueError:
    from cli import cli

if __name__ == '__main__':
    cli()

