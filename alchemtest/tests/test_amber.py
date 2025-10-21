'''Tests for all the AMBER datasets'''
import pytest

from alchemtest import Bunch
from alchemtest.amber import (load_bace_improper, load_bace_example,
                              load_simplesolvated, 
                              load_testfiles, load_tyk2_example)



from . import BaseDatasetTest

class TestAMBER(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_bace_improper, ('vdw',), (12,)),
                              (load_simplesolvated, ('charge', 'vdw'), (5, 12)),
                              (load_testfiles, (
                                "no_atomic_section",
                                "no_control_data",
                                "no_dHdl_data_points",
                                "no_free_energy_info",
                                "no_results_section",
                                "no_temp0_set",
                                "no_useful_data",
                                "none_in_mbar",
                                "not_finished_run"),
                                (1, 1, 1, 1, 1, 1, 1, 1, 1)
                              ),
                              ])
    def dataset(self, request):
        return super(TestAMBER, self).dataset(request)


# The BACE example dataset does not conform to the standard API because it
# contains sub dicts under 'complex'/'solvated' -> 'decharge', 'recharge',
# 'vdw' instead of lists of files. In order to use the same testing base class,
# we create a fake data set for "complex" and "solvated" separatedly and pass
# these accessor functions to the class.

# fake access to conform to expected API
def _load_bace_example_complex():
    dset = load_bace_example()
    return Bunch(data=dset.data['complex'],
                 DESCR="BACE example: complex")

def _load_bace_example_solvated():
    dset = load_bace_example()
    return Bunch(data=dset.data['solvated'],
                 DESCR="BACE example: solvated")

class TestBACEexample(BaseDatasetTest):
    # use pytest.param to add the id for nicer pytest -v output
    @pytest.fixture(scope="class",
                    params = [
                        pytest.param(
                            (_load_bace_example_complex,
                             ('decharge', 'recharge', 'vdw'),
                             (5, 5, 12)),
                            id="complex"),
                        pytest.param(
                            (_load_bace_example_solvated,
                            ('decharge', 'recharge', 'vdw'),
                            (5, 5, 12)),
                            id="solvated"),
                    ])
    def dataset(self, request):
        return super(TestBACEexample, self).dataset(request)


# test tyk2 example
def _load_tyk2_example():
    dset = load_tyk2_example()
    return Bunch(data=dset.data,
                 DESCR="TYK2 example:")

class TestTYK2example(BaseDatasetTest):
    # use pytest.param to add the id for nicer pytest -v output
    @pytest.fixture(scope="class",
                    params = [
                        pytest.param(
                            (_load_tyk2_example,
                             ('complex', 'solvated'),
                             (12, 12)),
                            id="tyk2"),
                    ])
    def dataset(self, request):
        return super(TestTYK2example, self).dataset(request)




