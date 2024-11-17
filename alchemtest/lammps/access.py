"""LAMMPS datasets.

"""

from os.path import dirname, join
from glob import glob

from .. import Bunch

def load_benzene():
    """Load data set of benzene in water.

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files from lammps dump output
        
            * "mbar": Files formatted for BAR or MBAR
            
                * '1_coul-off': NPT removal of benzene's charges
                * '2_vdw': NPT decoupling of vdw forces between benzene and water
                * '3_coul-on': NVT in vacuum restoration of benzene's charges
                
            * "ti"
            
                * '1_coul-off': NPT removal of benzene's charges
                * '2_vdw': NPT decoupling of vdw forces between benzene and water
                * '3_coul-on': NVT in vacuum restoration of benzene's charges
        
        - 'DESCR': the full description of the dataset

    """
    module_path = dirname(__file__)
    data = {
        "mbar": {
            '1_coul-off': glob(join(module_path, 'benzene/1_NPT_coul/mbar*.txt')),
            '2_vdw': glob(join(module_path, 'benzene/2_NPT_vdw/mbar*.txt')),
            '3_coul-on': glob(join(module_path, 'benzene/3_NVT_coul/mbar*.txt')),                
        },
        "ti": {
            '1_coul-off': glob(join(module_path, 'benzene/1_NPT_coul/ti*.txt')),
            '2_vdw': glob(join(module_path, 'benzene/2_NPT_vdw/ti*.txt')),
            '3_coul-on': glob(join(module_path, 'benzene/3_NVT_coul/ti*.txt')),    
        }
    }

    with open(join(module_path, 'benzene', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_lj_dimer():
    """Load data set of LJ dimer in solvent.

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files from lammps dump output        
        - 'DESCR': the full description of the dataset

    """
    module_path = dirname(__file__)
    data = glob(join(module_path, 'lj_dimer/cross_epsilon/linear*.txt'))

    with open(join(module_path, 'lj_dimer', 'descr.rst')) as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)