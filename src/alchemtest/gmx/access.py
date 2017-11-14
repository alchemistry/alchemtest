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

    data = {'Coulomb': glob(join(module_path, 'benzene/Coulomb/*/dhdl.xvg.bz2')),
            'VDW': glob(join(module_path, 'benzene/VDW/*/dhdl.xvg.bz2'))}

    with open(join(module_path, 'benzene', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
