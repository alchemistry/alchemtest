'''Tests for all the NAMD datasets'''
import pytest

from alchemtest.namd import load_tyr2ala, load_idws

from . import BaseDatasetTest


class TestNAMD(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_tyr2ala, ('forward', 'backward'), (1, 1)),
                              (load_idws, ('forward', ), (2,)),
                              ])
    def dataset(self, request):
        return super(TestNAMD, self).dataset(request)
