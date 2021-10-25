'''Tests for all the generic dataset'''
import pytest

from alchemtest.generic import load_MBAR_BGFS

from . import BaseDatasetTest

class TestGeneric(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_MBAR_BGFS, ('u_kn', 'N_k'), (1, 1)),
                              ])
    def dataset(self, request):
        return super(TestGeneric, self).dataset(request)
