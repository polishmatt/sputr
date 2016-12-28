from setuptools import setup

setup(
    name='sputr',
    version='0.1',
    install_requires=[
        'click==6.6'
    ],
    entry_points={
        'console_scripts': [
            'sputr = sputr:cli'
        ],
    },
)
