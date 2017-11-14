"""Accessors for Amber TI datasets.

"""

from os.path import dirname
from os.path import join
from glob import glob

from .. import Bunch

def load_simplesolvated():
    """Load the Amber solvated dataset.


    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        - 'data' : the data files by alchemical leg
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)
    data = {'charge': glob(join(module_path, 'simplesolvated/charge/*/ti-*.out')),
            'vdw': glob(join(module_path, 'simplesolvated/vdw/*/ti-*.out'))}

    with open(join(module_path, 'simplesolvated', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

def load_invalidfiles():
    """Load the invalid files.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        - 'data' : the example of invalid data files
        - 'DESCR': the full description of the dataset

    """

    module_path = dirname(__file__)
    data = [glob(join(module_path, 'invalidfiles/*.out.bz2'))]

    with open(join(module_path, 'invalidfiles', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
