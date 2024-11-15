'''Tests for all the LAMMPS datasets'''
import pytest

from alchemtest import Bunch
from alchemtest.lammps import load_benzene

from . import BaseDatasetTest

# fake access to conform to expected API
def _load_benzene_mbar():
    dset = load_benzene()
    return Bunch(data=dset.data['mbar'],
                 DESCR="Benzene example: mbar")

def _load_benzene_ti():
    dset = load_benzene()
    return Bunch(data=dset.data['ti'],
                 DESCR="Benzene example: ti")
class TestLAMMPS(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [
                        pytest.param(
                            (_load_benzene_mbar,
                             ('1_coul-off', '2_vdw', '3_coul-on'),
                             (36, 256, 36)),
                            id="complex"
                        ),
                        pytest.param(
                            (_load_benzene_ti,
                             ('1_coul-off', '2_vdw', '3_coul-on'),
                             (6, 16, 6)),
                            id="complex"
                        ),
                    ])
    def dataset(self, request):
        return super(TestLAMMPS, self).dataset(request)
