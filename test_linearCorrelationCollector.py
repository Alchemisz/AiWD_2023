import unittest

from linearCorrelationCollector import LinearCorrelationCollector


class TestLinearCorrelationCollector(unittest.TestCase):

    def test_calculate_linear_correlation(self):
        # given
        data_set = [
            [1, 2, 3],
            [5, 6, 8],
            [2, 1, 2]
        ]
        linear_correlation_collector = LinearCorrelationCollector(
            [2.667, 3, 4.333],
            [1.7, 2.16, 2.625]
        )
        # when
        linear_correlation_collector.calculate_linear_correlation(data_set)
        # then
        self.assertEqual(
            linear_correlation_collector.correlation_variable_stairs,
            [
                [1, 0.908, 0.921],
                [1, 0.999],
                [1]
            ]
        )


if __name__ == '__main__':
    unittest.main()
