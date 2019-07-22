"""Accessors for GOMC datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch

def load_benzene():
    """Load the GOMC benzene dataset.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)

    data = sorted(glob(join(module_path, 'benzene', 'inWater', 'Free_Energy_BOX_0_PRODUCTION_*.dat.bz2')))

    with open(join(module_path, 'benzene', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
    