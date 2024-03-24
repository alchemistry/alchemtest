.. _namd-datasets:

=============
NAMD datasets
=============

.. automodule:: alchemtest.namd

The :mod:`alchemlyb.namd` module features datasets generated using the
`NAMD <http://http://www.ks.uiuc.edu/Research/namd/>`_ molecular dynamics
engine. They can be accessed using the following accessor functions:

.. currentmodule:: alchemtest.namd

.. autosummary::

   load_tyr2ala
   load_idws

.. _namd_tyr2ala:

.. include:: ../alchemtest/namd/tyr2ala/descr.rst

.. autofunction:: alchemtest.namd.load_tyr2ala

.. _namd_idws:

.. include:: ../alchemtest/namd/idws/descr.rst

.. autofunction:: alchemtest.namd.load_idws

.. _namd_restarted:

.. include:: ../alchemtest/namd/restarted/descr.rst

.. autofunction:: alchemtest.namd.load_restarted

.. _namd_restarted_reversed:

.. include:: ../alchemtest/namd/restarted_reversed/descr.rst

.. autofunction:: alchemtest.namd.load_restarted_reversed

