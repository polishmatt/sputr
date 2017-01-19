from setuptools import setup, find_packages
import os

with open(os.path.join('sputr', 'VERSION')) as file:
    version = file.read().strip()

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
