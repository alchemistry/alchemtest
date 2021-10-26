.. _generic-datasets:

================
Generic datasets
================

.. automodule:: alchemtest.generic

The :mod:`alchemlyb.generic` module features datasets that are MD engine free and
can adopt any form.
They can be accessed using the following accessor functions:

.. currentmodule:: alchemtest.generic

.. autosummary::

   load_MBAR_BGFS

-------------------------------------------
Difficult case for the adaptive MBAR solver
-------------------------------------------

The :class:`pymbar.mbar.MBAR` can have difficulty in solving some
dataset with the *adaptive* method, where *BFGS* is needed.

The usage is like this ::

    >>> import numpy as np
    >>> from pymbar import MBAR
    >>> from alchemtest.generic import load_MBAR_BGFS
    >>> u_nk = np.load(load_MBAR_BGFS()['data']['u_nk'])
    >>> N_k = np.load(load_MBAR_BGFS()['data']['N_k'])
    >>> solver_options = {"maximum_iterations":10000,"verbose":True}
    >>> solver_protocol = {"method":"adaptive","options":solver_options}
    >>> mbar = MBAR(u_nk, N_k, solver_protocol=(solver_protocol,))
    >>> results, errors = mbar.getFreeEnergyDifferences()

Which will give the :class:`pymbar.utils.ParameterError` ::

    >>> solver_options = {"maximum_iterations":10000,"verbose":True}
    >>> solver_protocol = {"method":"BFGS","options":solver_options}
    >>> mbar = MBAR(u_nk, N_k, solver_protocol=(solver_protocol,))
    >>> results, errors = mbar.getFreeEnergyDifferences()

Which will work.

.. include:: ../src/alchemtest/generic/BFGS/descr.rst

.. autofunction:: alchemtest.generic.load_MBAR_BGFS