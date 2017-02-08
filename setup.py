from setuptools import setup, find_packages
import importlib

version = importlib.import_module('sputr.config').version

setup(
    name='sputr',
    version=version,
    description='Simple Python Unit Test Runner',
    long_description="An intuitive command line and Python package interface for Python's unit testing framework.",
    author='Matt Wisniewski',
    author_email='sputr@mattw.us',
    license='MIT',
    url='https://github.com/polishmatt/sputr',
    keywords=['testing'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    platforms=['unix','linux'],
    packages=[
        'sputr'
    ],
    install_requires=[
        'click==6.7'
    ],
    entry_points={
        'console_scripts': [
            'sputr = sputr.cli:cli'
        ],
    },
)
