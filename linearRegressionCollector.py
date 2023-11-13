import numpy as np
from matplotlib import pyplot as plt

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
            # for j in range(i, variables_count, 1):
            for j in range(variables_count):
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

            square_sum = 0.001 if square_sum == 0.0 else square_sum  # TODO
        return round(sum / square_sum, 3)

    def show_plot(self, column_names: list[str]):
        fig, ax = plt.subplots()
        im = ax.imshow(np.random.randint(1, 5, size=(len(column_names), len(column_names))))



        # Show all ticks and label them with the respective list entries
        ax.set_xticks(np.arange(len(self.linear_regression_coefficient_variable_stairs)), labels=column_names)
        ax.set_yticks(np.arange(len(self.linear_regression_coefficient_variable_stairs)), labels=column_names)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(self.linear_regression_coefficient_variable_stairs)):
            for j in range(len(self.linear_regression_coefficient_variable_stairs)):
                text = ax.text(j, i, self.linear_regression_coefficient_variable_stairs[i][j],
                               ha="center", va="center", color="w")

        ax.set_title("Wykres korelacji")
        # fig.tight_layout()
        plt.show()

