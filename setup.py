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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
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
