'''Tests for all the free dataset'''
import pytest

from alchemtest.free import load_MBAR_BGFS

from . import BaseDatasetTest

class TestFree(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_MBAR_BGFS, ('u_kn', 'N_k'), (1, 1)),
                              ])
    def dataset(self, request):
        return super(TestFree, self).dataset(request)