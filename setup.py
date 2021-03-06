#!/usr/bin/env python

from distutils.core import setup

setup(
    name='nectan',
    version='0.1.0',
    description='Utitilies for parsing and manipulating SC2 galaxy script',
    author='Talv',
    url='https://github.com/Talv/nectan',
    packages=['nectan'],
    entry_points={
        'console_scripts': [
            'galaxylint=nectan.cli:linter',
            'galaxysym=nectan.cli:symbol',
            'galaxyobf=nectan.cli:obfuscator',
            'galaxydeobf=nectan.cli:deobfuscator'
        ]
    }
 )