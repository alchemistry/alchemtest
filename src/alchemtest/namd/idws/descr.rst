NAMD: free energy of dummy ethane to ethane "mutation" in aqueous solution
==========================================================================

Free energy change from mutating an ethane molecule into an ethane molecule, 
turning a H atom into a methyl group and conversely.
Expected free energy is zero, however the dataset is tiny (sufficient for
testing purposes).
Uses Interleaved Double-Wide Sampling (Hénin and Brannigan).

Notes
-----
Data Set Characteristics:
    :Number of Legs: 1 (forward mutation in water with IDWS sampling)
    :Number of Windows: 11
    :Length of Windows: 500 fs (each window interspersed with 100 fs equilibration)
    :System Size: 1030 atoms
    :Temperature: 300 K
    :Pressure: 1 bar
    :Alchemical Pathway: dummy mutation of ethane into ethane using dual topology
                         hybrid molecule. Nonbonded interactions of perturbed
                         atoms are scaled with their environment.
    :Experimental Free Energy difference: N/A 
    :Missing Values: None
    :Energy unit: kcal/mol
    :Time unit: step
    :Date: May 2021
    :Donor: J Hénin
    :License: `CC0 <https://creativecommons.org/publicdomain/zero/1.0/>`_
              Public Domain Dedication

This dataset was generated using the `NAMD
<http://http://www.ks.uiuc.edu/Research/namd/>`_ molecular dynamics
engine.
