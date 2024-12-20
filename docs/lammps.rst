.. _lammps-datasets:

================
LAMMPS datasets
================
.. automodule:: alchemtest.lammps

The :mod:`alchemtest.lammps` module features datasets generated using the
`LAMMPS <http://www.lammps.org/>`_ molecular dynamics engine.  They
can be accessed using the following accessor functions:

.. currentmodule:: alchemtest.lammps

.. autosummary::

   load_benzene
   load_lj_dimer


-----------------
Simple TI and FEP
-----------------

The data sets contain derivatives of the Hamiltonian (TI) and free
energy perturbation (FEP) data suitable for processing with FEP
estimators as well as BAR/MBAR. Individual :math:`\lambda` windows
were run independently.


.. _lammps_benzene:
.. include:: ../alchemtest/lammps/benzene/descr.rst

.. autofunction:: alchemtest.lammps.load_benzene

.. _lammps_lj_dimer:
.. include:: ../alchemtest/lammps/lj_dimer/descr.rst

.. autofunction:: alchemtest.lammps.load_lj_dimer
   