.. _gmx-datasets:

================
Gromacs datasets
================
.. automodule:: alchemtest.gmx

The :mod:`alchemlyb.gmx` module features datasets generated using the
`Gromacs <http://www.gromacs.org/>`_ molecular dynamics engine.  They
can be accessed using the following accessor functions:

.. currentmodule:: alchemtest.gmx

.. autosummary::

   load_benzene
   load_expanded_ensemble_case_1
   load_expanded_ensemble_case_2
   load_expanded_ensemble_case_3
   load_water_particle_with_total_energy
   load_water_particle_with_potential_energy
   load_water_particle_without_energy


-----------------
Simple TI and FEP
-----------------

The data sets contain derivatives of the Hamiltonian (TI) and free
energy perturbation (FEP) data suitable for processing with FEP
estimators as well as BAR/MBAR. Individual :math:`\lambda` windows
were run independently.


.. _gmx_benzene:
.. include:: ../src/alchemtest/gmx/benzene/descr.rst

.. autofunction:: alchemtest.gmx.load_benzene


-----------------		  
Extended ensemble
-----------------

Data for *extended ensemble* simulations; case 1 and case 2 are
extended ensembles in the alchemical parameters, case 3 includes
replica exchange (REX).

.. include:: ../src/alchemtest/gmx/expanded_ensemble/case_1/descr.rst

.. autofunction:: alchemtest.gmx.load_expanded_ensemble_case_1

		  
.. include:: ../src/alchemtest/gmx/expanded_ensemble/case_2/descr.rst

.. autofunction:: alchemtest.gmx.load_expanded_ensemble_case_2

		  
.. include:: ../src/alchemtest/gmx/expanded_ensemble/case_3/descr.rst

.. autofunction:: alchemtest.gmx.load_expanded_ensemble_case_3
   

-------------------------
Water particle TI and FEP
-------------------------

3 simple dH/dl and U_nk datasets of a single water particle from a
simulations of water between to hydrophilic surfaces. One dataset
contains a total energy column, one contains a potential energy column and
one does not contain a energy column.

.. _gmx_water_particle:
.. include:: ../src/alchemtest/gmx/water_particle/descr.rst

.. autofunction:: alchemtest.gmx.load_water_particle_with_total_energy
.. autofunction:: alchemtest.gmx.load_water_particle_with_potential_energy
.. autofunction:: alchemtest.gmx.load_water_particle_without_energy