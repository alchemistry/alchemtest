#! /usr/bin/python
"""Setuptools-based setup script for alchemtest.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup, find_packages

import versioneer

setup(name='alchemtest',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='the simple alchemistry test set',
      author='David Dotson',
      author_email='dotsdl@gmail.com',
      maintainer='Oliver Beckstein',
      maintainer_email='orbeckst@gmail.com',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows ',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      license='BSD',
      long_description=open('README.rst').read(),
      long_description_content_type = 'text/x-rst',
      include_package_data=True,
)
