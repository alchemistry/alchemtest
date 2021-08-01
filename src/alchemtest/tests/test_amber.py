'''Tests for all the AMBER datasets'''
import pytest

from alchemtest.amber import (load_bace_improper, load_bace_example,
                              load_simplesolvated, load_invalidfiles, )



from . import BaseDatasetTest

class TestAMBER(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_bace_improper, ('vdw',), (12,)),
                              (load_simplesolvated, ('charge', 'vdw'), (5, 12)),
                              ])
    def dataset(self, request):
        return super(TestAMBER, self).dataset(request)


# difficult -- has sub dicts under 'complex'/'solvated' -> 'decharge', 'recharge', 'vdw'
# class TestBACEexample(BaseDatasetTest):
#     @pytest.fixture(scope="class",
#                     params = [(load_bace_example, ('complex',), (12,)),
#                               ])
#     def dataset(self, request):
#         return super().dataset(request)


# class TestInvalidFiles(BaseDatasetTest):
#     # can't get the list of list in data
#     @pytest.fixture(scope="class",
#                     params = [(load_invalidfiles, (slice(None),), (6,)),
#                               ])
#     def dataset(self, request):
#         return super().dataset(request)



