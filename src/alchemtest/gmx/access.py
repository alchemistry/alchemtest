"""Accessors for Gromacs datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch

def load_benzene():
    """Load the Gromacs benzene dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'Coulomb': sorted(glob(join(module_path, 'benzene', 'Coulomb', '*', 'dhdl.xvg.bz2'))),
            'VDW': sorted(glob(join(module_path, 'benzene', 'VDW', '*', 'dhdl.xvg.bz2')))}

    with open(join(module_path, 'benzene', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_expanded_ensemble_case_1():
    """Load the Gromacs Host CB7 Guest C3 expanded ensemble dataset, case 1 (single simulation visits all states).


    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'AllStates': glob(join(module_path, 'expanded_ensemble', 'case_1', 'CB7_Guest3_dhdl.xvg.gz'))}

    with open(join(module_path, 'expanded_ensemble', 'case_1', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_expanded_ensemble_case_2():
    """Load the Gromacs Host CB7 Guest C3 expanded ensemble dataset, case 2 (two simulations visit all states independently).


    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'AllStates': sorted(glob(join(module_path, 'expanded_ensemble', 'case_2', '*.xvg.gz')))}

    with open(join(module_path, 'expanded_ensemble', 'case_2', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_expanded_ensemble_case_3():
    """Load the Gromacs Host CB7 Guest C3 REX dataset, case 3.


    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'AllStates': sorted(glob(join(module_path, 'expanded_ensemble', 'case_3', '*.xvg.gz')))}

    with open(join(module_path, 'expanded_ensemble', 'case_3', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_water_particle_without_energy():
    """Load the Gromacs water particle without energy dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'AllStates': sorted(glob(join(module_path, 'water_particle', 'without_energy', '*.xvg.bz2')))}

    with open(join(module_path, 'water_particle', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_water_particle_with_potential_energy():
    """Load the Gromacs water particle with potential energy dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'AllStates': sorted(glob(join(module_path, 'water_particle', 'with_potential_energy', '*.xvg.bz2')))}

    with open(join(module_path, 'water_particle', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_water_particle_with_total_energy():
    """Load the Gromacs water particle with total energy dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = {'AllStates': sorted(glob(join(module_path, 'water_particle', 'with_total_energy', '*.xvg.bz2')))}

    with open(join(module_path, 'water_particle', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)