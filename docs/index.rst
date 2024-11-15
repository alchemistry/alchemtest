.. alchemtest documentation master file, created by
   sphinx-quickstart on Fri Mar 24 12:44:43 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

alchemtest: the simple alchemistry test set
===========================================

|doi|

**alchemtest** is a collection of test datasets for alchemical free energy
calculations.  The datasets come from a variety of software packages, primarily
molecular dynamics engines, and are used as the test set for `alchemlyb`_.  The
package is standalone, however, and can be used for any purpose.

Datasets are released under an `open license`_ that conforms to the `Open
Definition 2.1`_ that allows free use, re-use, redistribution, modification,
separation, for any purpose and without a charge. All data and code
can be found in the public GitHub repository `alchemistry/alchemtest`_.

This library is **under active development**. We use `semantic
versioning`_ to indicate clearly what kind of changes you may expect
between releases. Although it is heavily used for the alchemlyb_ test
suite it may contain bugs. Please raise any issues or questions in the
`Issue Tracker`_.

.. Note::

   :ref:`Contributions of data sets <contributing>` are very
   welcome. Please raise an issue in the `Issue Tracker`_ to propose a
   new data set and we will help you with the process of adding it to
   **alchemtest**.

   With release 0.7.0, the alchemlyb project adopted `NEP 29`_ to determine
   which versions of Python and NumPy_ will be supported. When we release a new
   major or minor version, alchemtest will support *at least all minor versions
   of Python introduced and released in the prior 42 months from the release
   date with a minimum of 2 minor versions of Python*, and *all minor versions
   of NumPy released in the prior 24 months from the anticipated release date
   with a minimum of 3 minor versions of NumPy*.

.. |doi| image:: https://zenodo.org/badge/83470847.svg
    :alt: Zenodo DOI
    :scale: 100%
    :target: https://zenodo.org/badge/latestdoi/83470847

.. _`alchemlyb`: https://github.com/alchemistry/alchemlyb
.. _`open license`:
   http://opendefinition.org/licenses/#recommended-conformant-licenses
.. _`Open Definition 2.1`: http://opendefinition.org/od/2.1/en/
.. _`alchemistry/alchemtest`:
   https://github.com/alchemistry/alchemtest
.. _`semantic versioning`: https://semver.org
.. _`Issue Tracker`:
   https://github.com/alchemistry/alchemtest/issues
.. _`NEP 29`: https://numpy.org/neps/nep-0029-deprecation_policy.html
.. _NumPy: https://numpy.org

.. toctree::
    :maxdepth: 1
    :caption: Overview

    install
    usage
    contributing
    helpers

.. toctree::
    :maxdepth: 1
    :caption: Datasets

    gmx
    amber
    gmx
    gomc
    lammps
    namd
    generic

