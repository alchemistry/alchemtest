'''Tests for all the gromacs dataset'''
import pytest

from alchemtest.gmx import load_benzene

from . import BaseDatasetTest

class TestBenzene(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_benzene, ('Coulomb', 'VDW'), (5, 16)),
                              ])
    def dataset(self, request):
        return super().dataset(request)
