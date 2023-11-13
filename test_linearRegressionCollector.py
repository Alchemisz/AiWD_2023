import unittest

from linearRegressionCoefficient import LinearRegressionCoefficient
from linearRegressionCollector import LinearRegressionCollector


class TestLinearRegressionCollector(unittest.TestCase):

    def test_calculate_linear_regression(self):
        # given
        data_set = [
            [2, 2],
            [6, 8],
            [1, 2]
        ]
        linear_regression_collector = LinearRegressionCollector(
            [3, 4]
        )
        # when
        linear_regression_collector.calculate_linear_regression(data_set)
        # then

        #TODO sprawdzic ręcznie bo nie wiadomo czy to dobrze
        self.assertEqual(
            linear_regression_collector.linear_regression_coefficient_variable_stairs,
            [
                [LinearRegressionCoefficient(0.0, 1.0), LinearRegressionCoefficient(-0.572, 1.286)],
                [LinearRegressionCoefficient(0.0, 1.0)]
            ]
        )


if __name__ == '__main__':
    unittest.main()
