Gromacs: n-phenylglycinonitrile in T4 lysozyme
==============================================

Obtain the absolute binding free energy of the n-phenylglycinonitrile
for T4 lysozyme by alchemically turning n-phenylglycinonitrile in T4 lysozyme
and water into vacuum.

Notes
-----
Data Set Characteristics:
    :Number of Legs: 2 (Restraint, Coulomb, VDW for protein;
        Coulomb, VDW for water)
    :Number of Windows: 11 for Restraint, 5 for Coulomb, 16 for VDW
    :Length of Windows: 1ns for protein and 5ns for water
    :System Size: 33005 atoms for protein and 2103 atoms for water
    :Temperature: 300 K
    :Pressure: 1 bar
    :Alchemical Pathway: vdw + coul --> restraint + vdw + coul -->
        restraint + vdw --> restraint + vacuum
    :Reference Hydration Free Energy in protein: -21.721  +-  0.089 kcal/mol
    :Reference Hydration Free Energy in water: -7.679  +-  0.080 kcal/mol
    :Missing Values: None
    :Energy unit: kJ/mol
    :Time unit: ps
    :Creator: \Z. Wu
    :Donor: Zhiyi Wu (zhiyi.wu@bioch.ox.ac.uk)
    :Date: March 2021
    :License: `CC0
	      <https://creativecommons.org/publicdomain/zero/1.0/>`_
	      Public Domain Dedication

This dataset was generated using
`tutorial <http://www.alchemistry.org/wiki/Absolute_Binding_Free_Energy_-_Gromacs_2016>`_
, with the `Gromacs <http://www.gromacs.org/>`_ molecular dynamics engine.

Data sourced from [Boyce2009]_.

.. [Boyce2009] Boyce, S.E., Mobley, D.L., Rocklin, G.J., Graves, A.P., Dill,
    K.A., Shoichet, B.K. (2009) Predicting Ligand Binding Affinity with
    Alchemical Free Energy Methods in a Polar Model Binding Site. J. Mol. Biol.
    394, 747–7636
