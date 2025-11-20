LAMMPS: Benzene in Water
==============================================

Benzene in water, alchemically decoupled to benzene in vacuum separated from bulk water

Test using LAMMPS dump files turned into u_nk and dHdl DataFrames that could be calculated
with MBAR or TI.

Notes
-----
Data Set Characteristics:
    :Number of Legs: 3 (Coulomb1 (NPT turn off Benzene charges), VDW (NPT), Coulomb2 (NVT turn on Benzene charges in vacuum))
    :Number of Windows: 6 for Coulomb1, 16 for VDW, 6 for Coulomb2
    :Length of Windows: 5ns
    :System Size: 1668 atoms
    :Temperature: 300 K
    :Pressure: 1 bar
    :Alchemical Pathway: vdw + coul --> vdw --> vacuum
    :Experimental Hydration Free Energy: -0.90 +- 0.2 kcal/mol
    :Missing Values: None
    :Energy unit: kcal/mol
    :Time unit: fs
    :Creator: Jennifer A. Clark
    :Donor: Jennifer A. Clark
    :Date: Dec. 2024
    :License: `NIST <https://www.nist.gov/disclaimer>`_    
    :DOI: 10.18434/mds2-3637

This dataset was provided by @jaclark5 in the
`NIST Data Repository <https://data.nist.gov/>`_

Experimental value sourced from [Mobley2013]_.

.. [Mobley2013] Mobley, David L. (2013). Experimental and Calculated Small 
    Molecule Hydration Free Energies. UC Irvine: Department of Pharmaceutical 
    Sciences, UCI. Retrieved from: http://escholarship.org/uc/item/6sd403pz