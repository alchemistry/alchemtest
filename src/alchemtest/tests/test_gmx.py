'''Tests for all the gromacs dataset'''
import pytest

from alchemtest.gmx import load_benzene

class Testbenzene():
    @pytest.fixture(scope="class")
    def bz(self):
        return load_benzene()

    def test_keys(self, bz):
        assert len(bz.data.keys()) == 2

    def test_coulomb(self, bz):
        assert len(bz.data['Coulomb']) == 5

    def test_vdw(self, bz):
        assert len(bz.data['VDW']) == 16
