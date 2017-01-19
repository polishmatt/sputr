from setuptools import setup, find_packages
import importlib

version = importlib.import_module('sputr.config').version

setup(
    name='sputr',
    version=version,
    description='Simple Python Unit Test Runner',
    author='Matt Wisniewski',
    author_email='sputr@mattw.us',
    license='MIT',
    url='https://github.com/polishmatt/sputr',
    keywords=['testing'],
    classifiers=[],
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
