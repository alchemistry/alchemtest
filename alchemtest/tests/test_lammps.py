'''Tests for all the NAMD datasets'''
import pytest

from alchemtest.namd import load_tyr2ala, load_idws, load_restarted, load_restarted_reversed

from . import BaseDatasetTest


class TestNAMD(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_tyr2ala, ('forward', 'backward'), (1, 1)),
                              (load_idws, ('forward', ), (2,)),
                              (load_restarted, ('both', ), (15,)),
                              (load_restarted_reversed, ('both', ), (19,))
                              ])
    def dataset(self, request):
        return super(TestNAMD, self).dataset(request)
