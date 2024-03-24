NAMD: free energy of tyrosine to alanine in vacuo
=================================================

Free energy change from mutating a Tyr into Ala in vacuo.
Uses Interleaved Double-Wide Sampling (Hénin and Brannigan).
Each lambda window was run separately, and NAMD was interrupted
and restarted multiple times, such that one window may span
multiple fepout files.

Derived from NAMD FEP Tutorial, available at:
https://www.ks.uiuc.edu/Training/Tutorials/namd/FEP/

This calculation was run from lambda = 1.0 to lambda = 0.0,
because it is possible for an IDWS calculation in NAMD to be
run this way.

Notes
-----
Data Set Characteristics:
    :Number of Legs: 1 (forward mutation with IDWS sampling)
    :Number of Windows: 11
    :Length of Windows: 50 ps
    :System Size: 57 atoms
    :Temperature: 300 K
    :Alchemical Pathway: Mutation of Tyr into Ala using hybrid molecule.
                         Nonbonded interactions of perturbed atoms are scaled
                         with their environment.
    :Missing Values: None
    :Energy unit: kcal/mol
    :Time unit: step
    :Date: September 2021
    :Donor: Thomas T. Joseph
    :License: `CC0 <https://creativecommons.org/publicdomain/zero/1.0/>`_
              Public Domain Dedication

This dataset was generated using the `NAMD
<http://http://www.ks.uiuc.edu/Research/namd/>`_ molecular dynamics
engine.
