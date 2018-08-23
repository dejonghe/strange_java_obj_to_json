#!/usr/bin/env python

from setuptools import setup


setup(
    name='sjotj',
    
    dependency_links=[
       'https://github.com/dejonghe/python-jproperties/releases/download/0.1/jproperties-0.1.tar.gz'
    ],
    entry_points={
        'console_scripts': [
            'sjotj = sjotj:main'
        ]
    }
)
