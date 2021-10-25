"""Accessors for generic datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch



def load_MBAR_BGFS():
    """Load data set that will fail the MBAR adaptive solver but could done
    by BGFS.

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files for u_kn and N_k

    """
    module_path = dirname(__file__)
    data = {'u_kn': join(module_path, 'BFGS/u_kn.npy'),
            'N_k': join(module_path, 'BFGS/N_k.npy'),}

    with open(join(module_path, 'BFGS', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
