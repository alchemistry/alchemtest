.. _amber-datasets:

==============
Amber datasets
==============

.. automodule:: alchemtest.amber

The :mod:`alchemlyb.amber` module features datasets generated using the `Amber
<http://www.ambermd.org/>`_ molecular dynamics engine.  They can be accessed
using the following accessor functions:

.. currentmodule:: alchemtest.amber

.. autosummary::

   load_simplesolvated
   load_invalidfiles

.. _amber_simplesolvated:

.. include:: ../src/alchemtest/amber/simplesolvated/descr.rst

.. autofunction:: alchemtest.amber.load_simplesolvated


.. _amber_invalidfiles:

.. include:: ../src/alchemtest/amber/invalidfiles/descr.rst
	     
.. autofunction:: alchemtest.amber.load_invalidfiles
