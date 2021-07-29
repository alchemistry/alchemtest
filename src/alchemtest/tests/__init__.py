import os

class BaseDatasetTest(object):
    # @pytest.fixture(scope="class",
    #                 params = [(load_tyr2ala, ('forward', 'backward'), (1, 1)),
    #                           ])
    # def dataset(self, reques):
    #   return super().dataset(request)

    def dataset(self, request):
        '''The input dataset is specified as:
        load_method: The method for loading the dataset.
        keys: The keys to the corresponding dataset.
        value_length: The expected number of file for each key.
        '''
        load_method, keys, value_length = request.param
        return load_method, keys, value_length

    def test_num_files(self, dataset):
        '''Test if the number of files matches with the expected number of
        files.'''
        load_method, keys, value_length = dataset
        for index, key in enumerate(keys):
            assert len(load_method().data[key]) == value_length[index]

    def test_file_exist(self, dataset):
        '''Test if files do exist.'''
        load_method, keys, value_length = dataset
        for key in keys:
            for file in load_method().data[key]:
                if not os.path.isfile(file):
                    raise AssertionError('Missing file in data set: {}'.format(file))
