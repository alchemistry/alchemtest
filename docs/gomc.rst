.. _gomc-datasets:

===============
GOMC datasets
===============
.. automodule:: alchemtest.gomc

The :mod:`alchemlyb.gomc` module features datasets generated using the
GPU Optimized Monte Carlo (`GOMC <http://gomc.eng.wayne.edu/>`_) simulation 
engine. They can be accessed using the following accessor functions:

.. currentmodule:: alchemtest.gomc

.. autosummary::

   load_benzene


------------------
Simple TI and FEP
------------------

The data sets contain derivatives of the Hamiltonian (TI) and free
energy perturbation (FEP) data suitable for processing with FEP
estimators as well as BAR/MBAR. Individual :math:`\lambda` windows
were run independently.


.. _gomc_benzene:
.. include:: ../alchemtest/gomc/benzene/descr.rst

.. autofunction:: alchemtest.gomc.load_benzene
