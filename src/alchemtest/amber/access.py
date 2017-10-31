"""Accessors for Amber TI datasets.

"""

from os.path import dirname
from os.path import join
from glob import glob
from sklearn.datasets.base import Bunch

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
    print "Check the module path", module_path
    data = {'charge': glob(join(module_path, 'simplesolvated/charge/*/ti-*.out')),
            'vdw': glob(join(module_path, 'simplesolvated/vdw/*/ti-*.out'))}

    with open(join(module_path, 'simplesolvated', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
