"""Accessors for generic datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch



def load_ljdimer():
    """Load data set of decoupled ljdimer

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files from lammps dump output

    """
    module_path = dirname(__file__)
    data = {'u_nk': join(module_path, 'ljdimer/???'),
            'N_k': join(module_path, 'ljdimer/N_k.npy'),}

    with open(join(module_path, 'BFGS', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
