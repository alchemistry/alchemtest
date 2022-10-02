"""Accessors for Amber TI datasets.

"""

from pathlib import Path
from .. import Bunch



def load_bace_improper():
    """Load Amber Bace improper solvated vdw example

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files for improper solvated vdw alchemical leg

    """
    module_path = Path(__file__).parent
    data = {'vdw': list(map(str, module_path.glob('bace_improper/solvated/vdw/*/ti-*.out.bz2')))}

    with open(module_path / 'bace_improper' / 'descr.rst') as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_bace_example():
    """Load Amber Bace example perturbation.

    Returns
    -------
    data: Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files by system and alchemical leg

    """
    module_path = Path(__file__).parent
    data = {'complex':
                {'decharge': list(map(str, module_path.glob('bace_CAT-13d~CAT-17a/complex/decharge/*/ti-*.out.bz2'))),
                 'recharge': list(map(str, module_path.glob('bace_CAT-13d~CAT-17a/complex/recharge/*/ti-*.out.bz2'))),
                 'vdw': list(map(str, module_path.glob('bace_CAT-13d~CAT-17a/complex/vdw/*/ti-*.out.bz2')))
                 },
            'solvated':
                {'decharge': list(map(str, module_path.glob('bace_CAT-13d~CAT-17a/solvated/decharge/*/ti-*.out.bz2'))),
                 'recharge': list(map(str, module_path.glob('bace_CAT-13d~CAT-17a/solvated/recharge/*/ti-*.out.bz2'))),
                 'vdw': list(map(str, module_path.glob('bace_CAT-13d~CAT-17a/solvated/vdw/*/ti-*.out.bz2')))
                 }
            }

    with open(module_path / 'bace_CAT-13d~CAT-17a' / 'descr.rst') as rst_file:
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

    module_path = Path(__file__).parent
    data = {'charge': list(map(str, module_path.glob('simplesolvated/charge/*/ti-*.tar.bz2'))),
            'vdw': list(map(str, module_path.glob('simplesolvated/vdw/*/ti-*.tar.bz2')))}

    with open(module_path / 'simplesolvated' / 'descr.rst') as rst_file:
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


    .. deprecated:: 0.7
       use :func:`load_testfiles` instead

    """

    import warnings  # NOTE: this import is here and not where it should be just because we'll remove this function in next version
    warnings.warn(
        "load_invalidfiles() was deprecated in 0.7.0 and will be removed in the following release."
        " Use load_testfiles() instead",
        DeprecationWarning)
    module_path = Path(__file__).parent
    data = [[
        module_path / 'testfiles' / 'no_useful_data.out.tar.bz2',
        module_path / 'testfiles' / 'no_control_data.out.tar.bz2',
        module_path / 'testfiles' / 'no_temp0_setted.out.tar.bz2',
        module_path / 'testfiles' / 'no_free_energy_info.out.tar.bz2',
        module_path / 'testfiles' / 'no_atomic_section.out.tar.bz2',
        module_path / 'testfiles' / 'no_results_section.out.tar.bz2']]

    with open(module_path / 'testfiles' / 'descr_invalid.rst') as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)


def load_testfiles():
    """Load incomplete or wrongly formatted files to be used to test the AMBER parsers.

    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:

        - 'data' : the data files
        - 'DESCR': the full description of all the files

    """

    testfiles_path = Path(__file__).parent / 'testfiles'

    data = {}
    for f in testfiles_path.iterdir():
        f_path = str(f)
        suffixes = (".out", ".tar", ".bz2")
        if f.suffix in suffixes:
            while f.suffix in suffixes:
                f = f.with_suffix('')
            data[f.name] = [f_path]

    with open(testfiles_path / 'descr.rst') as rst_file:
        fdescr = rst_file.read()

    return Bunch(data=data,
                 DESCR=fdescr)
