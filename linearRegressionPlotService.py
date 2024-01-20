import matplotlib.pyplot as plt
import numpy as np

from linearRegressionCoefficient import LinearRegressionCoefficient


class LinearRegressionPlotService:

    def __init__(self, data_set, variable_x_index: int, variable_y_index: int, linear_regression_coeeficient: LinearRegressionCoefficient):
        x = np.linspace(1, 2, len(data_set))
        y = []
        for instance_index in data_set:
            y.append(instance_index[variable_y_index])

        a, b = np.polyfit(x, y, deg=1)
        y_est = linear_regression_coeeficient.b * x + linear_regression_coeeficient.a
        # y_est = a * x + b

        fig, ax = plt.subplots()
        ax.plot(x, y_est, '-')
        ax.plot(x, y, 'o', color='tab:brown')
        plt.xlabel("Trujący")
        plt.ylabel("Kształt kapelusza")

    def show_plot(self):
        plt.show()
