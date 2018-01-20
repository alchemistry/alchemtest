.. _usage: 

Basic usage
===========

All datasets in :mod:`alchemtest` are accessible via ``load_*``
functions, organized in submodules by the software package that
generated them.  The current set of submodules are:

.. currentmodule:: alchemtest

.. autosummary::

   gmx
   amber
   namd

As an example, we can access the :ref:`gmx_benzene` dataset with::

    >>> from alchemtest.gmx import load_benzene
    >>> bz = load_benzene()

and use the resulting :class:`Bunch` object to introspect what this
dataset includes.  In particular, it features a ``DESCR`` attribute
with a human-readable description of the dataset::

    >>> print(bz.DESCR)
    Gromacs: Benzene in water
    =========================

    Benzene in water, alchemically turned into benzene in vacuum separated from water
      
    Notes
    -----
    Data Set Characteristics:
        :Number of Legs: 2 (Coulomb, VDW)
        :Number of Windows: 5 for Coulomb, 16 for VDW
        :Length of Windows: 40ns
    
        :Missing Values: None
        :Creator: \I. Kenney
        :Donor: Ian Kenney (ian.kenney@asu.edu)
        :Date: March 2017
        :License: `CC0
                  <https://creativecommons.org/publicdomain/zero/1.0/>`_
                  Public Domain Dedication
    
    This dataset was generated using `MDPOW <https://github.com/Becksteinlab/MDPOW>`_, with
    the `Gromacs <http://www.gromacs.org/>`_ molecular dynamics engine. 

as well as the dataset itself::

    >>>  bz.data.keys()
    ['VDW', 'Coulomb']

which consists in this case of two alchemical legs, each having
several files.  For this dataset each file happens to correspond to a
simulation sampling a particular :math:`\lambda`::

    >>> bz.data['Coulomb']
    ['/usr/local/python3.6/site-packages/alchemtest/gmx/benzene/Coulomb/0000/dhdl.xvg.bz2',
     '/usr/local/python3.6/site-packages/alchemtest/gmx/benzene/Coulomb/0250/dhdl.xvg.bz2',
     '/usr/local/python3.6/site-packages/alchemtest/gmx/benzene/Coulomb/0500/dhdl.xvg.bz2',
     '/usr/local/python3.6/site-packages/alchemtest/gmx/benzene/Coulomb/0750/dhdl.xvg.bz2',
     '/usr/local/python3.6/site-packages/alchemtest/gmx/benzene/Coulomb/1000/dhdl.xvg.bz2']

These paths can be read by any appropriate parser for further
analysis.  For this particular dataset, see
:mod:`alchemlyb.parsing.gmx` for a good set of parsers.
