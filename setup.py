from setuptools import setup, find_packages

setup(
    name='sputr',
    version='0.1',
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
