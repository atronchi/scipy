#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('sparse_mult',parent_package,top_path)

    return config

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("sparse_mult", ["sparse_mult.pyx"])]
)

