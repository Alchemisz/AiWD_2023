import csv

import matplotlib.pyplot as plt
import numpy as np

from baseStatisticCollector import BaseStatisticCollector
from dataPreProcessingService import DataPreProcessingService
from distantPointsCollector import DistantPointsCollector
from linearCorrelationCollector import LinearCorrelationCollector
from linearRegressionCollector import LinearRegressionCollector
from quantileCollector import QuartileCollector


def main():
    file = open('wine.csv')
    type(file)

    csv_reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')

    data_set = []
    for instance_index in csv_reader:
        data_set.append(instance_index)

    file.close()

    print("--------------------1----------------------")
    data_pre_processing_service = DataPreProcessingService(len(data_set[0]), len(data_set), )
    data_pre_processing_service.pre_process_data_set(data_set)

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
    for instance_index in distant_points_collector.distantPointVariableValues:
        print(instance_index)

    print("---------------------4--------------------- CORRELATION")
    linear_correlation_collector = LinearCorrelationCollector(
        base_statistic_collector.avg_variable_values,
        base_statistic_collector.standard_deviation_variable_values
    )
    linear_correlation_collector.calculate_linear_correlation(data_set)
    # linear_correlation_collector.show_plot()

    for instance_index in linear_correlation_collector.correlation_variable_stairs:
        print(instance_index)

    print("---------------------6---------------------")
    linear_regression_collector = LinearRegressionCollector(base_statistic_collector.avg_variable_values)
    linear_regression_collector.calculate_linear_regression(data_set)

    for instance_index in linear_regression_collector.linear_regression_coefficient_variable_stairs:
        for element in instance_index:
            print(str(element), end="\t\t\t")
        print()

    print("---------------------HISTOGRAM---------------------")
    response = []
    for instance_index in data_set:
        response.append(instance_index[0])

    # plt.style.use('_mpl-gallery')
    #
    # fig, ax = plt.subplots()
    #
    # ax.hist(response, bins=5, linewidth=0.5, edgecolor="white") #wine - 3 muschorms - 2 bins
    #
    # ax.set(xlim=(0, 3), xticks=np.arange(1, 5),
    #        ylim=(0, 100), yticks=np.linspace(0, 100, 5))

    # plt.show()

    # classes = []
    # for instance_index in range(len(data_set)):
    #     classes.append(data_set[instance_index][0])
    #
    # classes = list(set(classes))
    # print(classes)
    #
    # plot_data_set = []
    # for i in range(len(classes)):
    #     plot_data_set.append([])
    #
    # instances_count = range(len(data_set))
    # classes_count = range(len(classes))
    #
    # for instance_index in instances_count:
    #     for class_index in classes_count:
    #         instance_class = data_set[instance_index][0]
    #         if classes[class_index] == instance_class:
    #             plot_data_set[class_index].append(data_set[instance_index][1])
    #
    #
    # plt.boxplot(plot_data_set, vert=True)
    #
    # # Dodawanie tytułu i etykiet na osiach
    # plt.title("Wykres pudełkowy dla zmiennych: Typ wina i alkohol")
    # plt.ylabel("Alkohol")
    # plt.xlabel("Typ wina")
    #
    # # Wyświetlanie wykresu
    # plt.show()


    x = np.linspace(0, 10, 11)
    y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1, 9.9, 13.9, 15.1, 12.5]

    # fit a linear curve and estimate its y-values and their error.
    a, b = np.polyfit(x, y, deg=1)
    y_est = a * x + b

    fig, ax = plt.subplots()
    ax.plot(x, y_est, '-')
    ax.plot(x, y, 'o', color='tab:brown')

    plt.show()



if __name__ == "__main__":
    main()
