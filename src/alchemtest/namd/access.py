"""Accessors for NAMD FEP datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch

def load_tyr2ala():
    """Load the NAMD tyrosine to alanine mutation dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)
    data = {'forward': glob(join(module_path, 'tyr2ala/in-aqua/forward/*.fepout.bz2')),
            'backward': glob(join(module_path, 'tyr2ala/in-aqua/backward/*.fepout.bz2'))}

    with open(join(module_path, 'tyr2ala', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_idws():
    """Load the NAMD IDWS dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)
    data = {'forward': glob(join(module_path, 'idws', 'idws?.fepout.bz2'))}

    with open(join(module_path, 'idws', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_restarted():
    """Load the NAMD IDWS dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)
    data = {'both': glob(join(module_path, 'restarted', 'restarted*.fepout.bz2'))}

    with open(join(module_path, 'restarted', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
