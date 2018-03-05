#!/usr/bin/env python

from distutil.core import setup

setup(name='faces',
    version='1.0',
    description=("Kernal coding test"),
    author='Liang Yu',
    author_email='LiangJYu@gmail.com',
    url='https://github.com/MisterYu/faces',
    packages=['faces'],
    install_requires=[
        'numpy==1.14.1',
        'opencv-contrib-python==3.4.0.12',
        'pyQt5==5.10.1'
    ],
)
