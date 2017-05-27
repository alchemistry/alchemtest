#! /usr/bin/python
"""Setuptools-based setup script for alchemtest.

For a basic installation just type the command::

  python setup.py install

"""

from setuptools import setup, find_packages

setup(name='alchemtest',
      version='0.1.0',
      description='the simple alchemistry test set',
      author='David Dotson',
      author_email='dotsdl@gmail.com',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      license='BSD',
      long_description=open('README.rst').read(),
      install_requires=['scikit-learn'],
      include_package_data=True,
      )
