import unittest

from dataPreProcessingService import DataPreProcessingService


class TestDataPreProcessingService(unittest.TestCase):

    def test_calculate_linear_correlation(self):
        # given
        data_set = [
            [1, 2, '?'],
            [5, '?', 8],
            [2, 1, 2]
        ]
        expected_result = [
            [1, 2, 3.333],
            [5, 1, 8],
            [2, 1, 2]
        ]
        data_pre_processing_service = DataPreProcessingService(3, 3)
        # when
        data_pre_processing_service.pre_process_data_set(data_set)
        # then
        self.assertEqual(data_set, expected_result)


if __name__ == '__main__':
    unittest.main()
