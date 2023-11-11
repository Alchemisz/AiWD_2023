import csv

from baseStatisticCollector import BaseStatisticCollector
from distantPointsCollector import DistantPointsCollector
from linearCorrelationCollector import LinearCorrelationCollector
from quantileCollector import QuartileCollector

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

def main():
    file = open('wine.csv')
    type(file)

    csv_reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')

    data_set = []
    for row in csv_reader:
        data_set.append(row)

    file.close()

    print("--------------------2----------------------")
    base_statistic_collector = BaseStatisticCollector()
    base_statistic_collector.calculate_base_statistic(data_set)

    print("Min variable values: ")
    print(base_statistic_collector.min_variable_values)
    print("Max variable values: ")
    print(base_statistic_collector.max_variable_values)
    print("Avg variable values: ")
    print(base_statistic_collector.avg_variable_values)

    print("Standard deviation variable values: ")
    print(base_statistic_collector.standard_deviation_variable_values)

    quartile_collector = QuartileCollector()
    quartile_collector.calculate_quartiles(data_set)
    print("Q1 variable values: ")
    print(quartile_collector.firstQuartileVariableValues)
    print("Median variable values: ")
    print(quartile_collector.secondQuartileVariableValues)
    print("Q3 variable values: ")
    print(quartile_collector.thirdQuartileVariableValues)
    print("IRQ variable values: ")
    print(quartile_collector.interQuartileRangeVariableValues)
    print("Quantile 0.1 variable values: ")
    print(quartile_collector.zeroOneQuantileVariableValues)
    print("Quantile 0.9 variable values: ")
    print(quartile_collector.zeroNineQuantileVariableValues)

    print("---------------------3--------------------")
    distant_points_collector = DistantPointsCollector(
        quartile_collector.firstQuartileVariableValues,
        quartile_collector.firstQuartileVariableValues,
        quartile_collector.interQuartileRangeVariableValues
    )
    distant_points_collector.calculate_distant_point(data_set)
    for row in distant_points_collector.distantPointVariableValues:
        print(row)

    print("---------------------4---------------------")
    linear_correlation_collector = LinearCorrelationCollector(
        base_statistic_collector.avg_variable_values,
        base_statistic_collector.standard_deviation_variable_values
    )
    linear_correlation_collector.calculate_linear_correlation(data_set)

    for row in linear_correlation_collector.correlation_variable_stairs:
        print(row)

    # fig, ax = plt.subplots()
    # im = ax.imshow(linear_correlation_collector.correlation_variable_stairs)
    #
    # # Show all ticks and label them with the respective list entries
    # ax.set_xticks(np.arange(len(linear_correlation_collector.correlation_variable_stairs)))
    # ax.set_yticks(np.arange(len(linear_correlation_collector.correlation_variable_stairs)))
    #
    # # Loop over data dimensions and create text annotations.
    # for i in range(len(linear_correlation_collector.correlation_variable_stairs)):
    #     for j in range(len(linear_correlation_collector.correlation_variable_stairs[i])):
    #         text = ax.text(j, i, linear_correlation_collector.correlation_variable_stairs[i, j],
    #                        ha="center", va="center", color="w")
    #
    # ax.set_title("Harvest of local farmers (in tons/year)")
    # fig.tight_layout()
    # plt.show()
    #




    print("---------------------5---------------------")


if __name__ == "__main__":
    main()
