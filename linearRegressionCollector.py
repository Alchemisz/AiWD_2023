from linearRegressionCoefficient import LinearRegressionCoefficient


class LinearRegressionCollector:

    def __init__(self, avg_variable_values):
        self.avg_variable_values = avg_variable_values
        self.linear_regression_coefficient_variable_stairs = []

    def calculate_linear_regression(self, data_set):
        variables_count: int = len(data_set[0])  # with class
        instances_count: int = len(data_set)
        for i in range(variables_count):
            linear_regression_variable_coefficients = []
            for j in range(i, variables_count, 1):
                regression_coefficient = self.__calculate_regression_coefficients(data_set, i, j, instances_count)
                free_word = data_set[0][j] - (regression_coefficient * data_set[0][i])
                linear_regression_variable_coefficients.append(
                    LinearRegressionCoefficient(round(free_word, 3), round(regression_coefficient, 3)))
            self.linear_regression_coefficient_variable_stairs.append(linear_regression_variable_coefficients)

    def __calculate_regression_coefficients(self, data_set, x_index, y_index, instances_count) -> float:
        sum: float = 0
        square_sum: float = 0
        for instance_index in range(instances_count):
            x_variable_difference = data_set[instance_index][x_index] - self.avg_variable_values[x_index]
            y_variable_difference = data_set[instance_index][y_index] - self.avg_variable_values[y_index]
            square_sum += pow(x_variable_difference, 2)
            sum += x_variable_difference * y_variable_difference
        return round(sum / square_sum, 3)
