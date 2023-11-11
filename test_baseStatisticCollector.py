import unittest

from baseStatisticCollector import BaseStatisticCollector


class TestBaseStatisticCollector(unittest.TestCase):

    def test_calculate_min_values(self):
        # given
        data_set = [
            [1, 2, 3],
            [5, 6, 8],
            [2, 1, 2]
        ]
        base_statistic_collector = BaseStatisticCollector()
        # when
        base_statistic_collector.calculate_base_statistic(data_set)
        # then
        self.assertEqual(base_statistic_collector.min_variable_values, [1, 1, 2])

    def test_calculate_max_values(self):
        # given
        data_set = [
            [1, 2, 3],
            [5, 6, 8],
            [2, 1, 2]
        ]
        base_statistic_collector = BaseStatisticCollector()
        # when
        base_statistic_collector.calculate_base_statistic(data_set)
        # then
        self.assertEqual(base_statistic_collector.max_variable_values, [5, 6, 8])

    def test_calculate_avg_values(self):
        # given
        data_set = [
            [1, 2, 3],
            [5, 6, 8],
            [2, 1, 2]
        ]
        base_statistic_collector = BaseStatisticCollector()
        # when
        base_statistic_collector.calculate_base_statistic(data_set)
        # then
        self.assertEqual(base_statistic_collector.avg_variable_values, [2.667, 3, 4.333])

    def test_calculate_standard_deviation_values(self):
        # given
        data_set = [
            [1, 2, 3],
            [5, 6, 8],
            [2, 1, 2]
        ]
        base_statistic_collector = BaseStatisticCollector()
        # when
        base_statistic_collector.calculate_base_statistic(data_set)
        # then
        self.assertEqual(base_statistic_collector.standard_deviation_variable_values, [1.7, 2.16, 2.625])


if __name__ == '__main__':
    unittest.main()
