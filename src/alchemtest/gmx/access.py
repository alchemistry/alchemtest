"""Accessors for Gromacs datasets.

"""

from os.path import dirname
from os.path import join
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

    data = {'Coulomb': glob(join(module_path, 'benzene/Coulomb/*/dhdl.xvg.bz2')),
            'VDW': glob(join(module_path, 'benzene/VDW/*/dhdl.xvg.bz2'))}

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

    data = {'AllStates': glob(join(module_path, 'expanded_ensemble/case_1/CB7_Guest3_dhdl.xvg.gz'))}

    with open(join(module_path, 'expanded_ensemble/case_1', 'descr.rst')) as rst_file:
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

    data = {'AllStates': glob(join(module_path, 'expanded_ensemble/case_2/*.xvg.gz'))}

    with open(join(module_path, 'expanded_ensemble/case_2', 'descr.rst')) as rst_file:
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

    data = {'AllStates': glob(join(module_path, 'expanded_ensemble/case_3/*.xvg.gz'))}

    with open(join(module_path, 'expanded_ensemble/case_3', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
