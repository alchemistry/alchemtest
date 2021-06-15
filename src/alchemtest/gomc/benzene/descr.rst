.. -*- coding: utf-8 -*-

GOMC: Benzene in water
=========================

Hydration free energy of benzene using the *TraPPE-EH* [Raj2007]_
model and the SPC water model.

Notes
-----
Data Set Characteristics:
    :Number of Legs: 2 (Coulomb, VDW)
    :Number of Windows: 7 for Coulomb, 15 for VDW
    :Length of Windows: 50 million Monte Carlo steps
    :System Size: 1001 molecules
    :Temperature: 298 K
    :Pressure: 1 bar
    :Alchemical Pathway: vacuum --> vdw --> vdw + coul
    :Experimental Hydration Free Energy: -0.90 ± 0.2 kcal/mol
    :Missing Values: None
    :Energy unit: kJ/mol
    :Time unit: Monte Carlo steps
    :Creator: \M. Soroush Barhaghi
    :Donor: Mohammad Soroush Barhaghi (m.soroush@wayne.edu)
    :Date: July 2019
    :License: `CC0
	      <https://creativecommons.org/publicdomain/zero/1.0/>`_
	      Public Domain Dedication       

This dataset was generated using `GOMC <http://gomc.eng.wayne.edu/>`_ Monte Carlo simulation engine. 

Experimental value sourced from [Mobley2013b]_.

.. [Mobley2013b] Mobley, David L. (2013). Experimental and Calculated Small 
    Molecule Hydration Free Energies. UC Irvine: Department of Pharmaceutical 
    Sciences, UCI. Retrieved from: https://escholarship.org/uc/item/6sd403pz
.. [Raj2007] Neeraj Rai and J. Ilja Siepmann (2007). The Journal of
   Physical Chemistry B, 111 (36), 10790-10799 DOI:
   `10.1021/jp073586l`_

.. _`10.1021/jp073586l`: https://pubs.acs.org/doi/10.1021/jp073586l   
