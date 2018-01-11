"""Accessors for Amber TI datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch

def load_bace_example():
    """Load Amber Bace example perturbation.
    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files files by system and alchemical leg

    """
    module_path = dirname(__file__)
    data = {'complex':
                {'decharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/complex/decharge/*/ti-*.out')),
                 'recharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/complex/recharge/*/ti-*.out')),
                 'vdw': glob(join(module_path, 'bace_CAT-13d~CAT-17a/complex/vdw/*/ti-*.out'))
                 },
            'solvated':
                {'decharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/solvated/decharge/*/ti-*.out')),
                 'recharge': glob(join(module_path, 'bace_CAT-13d~CAT-17a/solvated/recharge/*/ti-*.out')),
                 'vdw': glob(join(module_path, 'bace_CAT-13d~CAT-17a/solvated/vdw/*/ti-*.out'))
                 }
            }

    with open(join(module_path, 'bace_CAT-13d~CAT-17a', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)

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
