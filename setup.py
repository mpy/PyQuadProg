import os
import sys
from os.path import join
from distutils.core import setup
from distutils.extension import Extension
import numpy


PROJECT = 'PyQuadProg'
VERSION = '0.0'
URL = 'https://github.com/mpy/PyQuadProg'
AUTHOR_EMAIL = u'mehdi.towhidi@gerad.ca'
DESC = 'A Python interface for QuadProg++ to solve dense convex QPs. ' \
       'QuadProg++ is written by Luca Di Gaspero (l.digaspero@uniud.it)'


USECYTHON = False

try:
    QuadProgDir = os.environ['QUADPROG_DIR']
except:
    raise Exception('Please set the environment variable QUADPROG_DIR ' +
                    'to the location of the quadprog\'s  directory')


libDirs = ['/Users/mehdi/Downloads/quadprog-3/src/']
libs = ['QuadProgpp']

cmdclass = {}
if USECYTHON:
    from Cython.Distutils import build_ext
    from Cython.Distutils import extension
    Extension = extension.Extension
    import Cython.Compiler.Options
    Cython.Compiler.Options.annotate = True
    cmdclass.update({'build_ext': build_ext})
    fileext = '.pyx'
else:
    fileext = '.cpp'

ext_modules = []
ext_modules += [Extension('PyQuadProg',
                          sources=['PyQuadProg' +  fileext],
                          language='c++',
                          library_dirs=libDirs,
                          libraries=libs,
                          include_dirs=[join(QuadProgDir, 'src'),  numpy.get_include()]),]


with open('README.rst') as f_README, \
     open('AUTHORS') as f_AUTHORS, \
     open('LICENSE') as f_LICENSE:
     s_README = f_README.read()
     s_AUTHORS = f_AUTHORS.read()
     s_LICENSE = f_LICENSE.read()

setup(name='PyQuadProg',
      #packages=['PyQuadProg'],
      version=VERSION,
      description=DESC,
      long_description=s_README,
      author=s_AUTHORS,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=s_LICENSE,
      cmdclass=cmdclass,
      ext_modules=ext_modules)
