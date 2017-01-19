from setuptools import setup, find_packages

with open(os.path.join('sputr', 'VERSION')) as file:
    version = file.read().strip()

setup(
    name='sputr',
    version=version,
    packages=[
        'sputr'
    ],
    install_requires=[
        'click==6.6'
    ],
    entry_points={
        'console_scripts': [
            'sputr = sputr.cli:cli'
        ],
    },
)
