'''Tests for all the gromacs dataset'''
import pytest

from alchemtest.gmx import (load_benzene, load_ABFE, load_ethanol,
                            load_expanded_ensemble_case_1,
                            load_expanded_ensemble_case_2,
                            load_expanded_ensemble_case_3,
                            load_water_particle_without_energy,
                            load_water_particle_with_potential_energy,
                            load_water_particle_with_total_energy,
                            )

from . import BaseDatasetTest


class TestGROMACS(BaseDatasetTest):
    @pytest.fixture(scope="class",
                    params = [(load_benzene, ('Coulomb', 'VDW'), (5, 16)),
                              (load_ABFE, ('complex', 'ligand'), (30, 20)),
                              (load_ethanol, ('Coulomb', 'VDW'), (5, 7)),
                              (load_expanded_ensemble_case_1, ('AllStates', ), (1,)),
                              (load_expanded_ensemble_case_2, ('AllStates', ), (2,)),
                              (load_expanded_ensemble_case_3, ('AllStates', ), (32,)),
                              (load_water_particle_without_energy, ('AllStates', ), (38,)),
                              (load_water_particle_with_potential_energy, ('AllStates', ), (38,)),
                              (load_water_particle_with_total_energy, ('AllStates', ), (38,)),
                              ])
    def dataset(self, request):
        return super(TestGROMACS, self).dataset(request)


