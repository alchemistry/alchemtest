'''Tests for all the GOMC dataset'''
import pytest

from alchemtest.gomc import load_benzene

from . import BaseDatasetTest

class TestGOMC(BaseDatasetTest):
    # note that the GOMC data does not use a dict for data but directly returns
    # a list; we can work around this peculiarity by using a slice instead of a key
    @pytest.fixture(scope="class",
                    params = [(load_benzene, (slice(None),), (23,)),
                              ])
    def dataset(self, request):
        return super(TestGOMC, self).dataset(request)
