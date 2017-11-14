.. alchemtest documentation master file, created by
   sphinx-quickstart on Fri Mar 24 12:44:43 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

alchemtest: the simple alchemistry test set
===========================================

**alchemtest** is a collection of test datasets for alchemical free energy calculations.  The datasets come from a variety of software packages, primarily molecular dynamics engines, and are used as the test set for `alchemlyb`_.  The package is standalone, however, and can be used for any purpose.

Datasets are released under an `open license`_ that conforms to the `Open Definition 2.1`_) that allows free use, re-use, redistribution, modification, separation, for any purpose and without a charge.


.. _`alchemlyb`: https://github.com/alchemistry/alchemlyb
.. _`open license`:
   http://opendefinition.org/licenses/#recommended-conformant-licenses
.. _`Open Definition 2.1`: http://opendefinition.org/od/2.1/en/

.. note:: This library is in an **alpha** state. The library and the documentation is incomplete. Use in production at your own risk.


.. toctree::
    :maxdepth: 1
    :caption: Overview

    install
    usage
    helpers

.. toctree::
    :maxdepth: 1
    :caption: Datasets

    gmx
    amber
