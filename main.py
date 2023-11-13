import csv

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
    for row in csv_reader:
        data_set.append(row)

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
    for row in distant_points_collector.distantPointVariableValues:
        print(row)

    print("---------------------4---------------------")
    linear_correlation_collector = LinearCorrelationCollector(
        base_statistic_collector.avg_variable_values,
        base_statistic_collector.standard_deviation_variable_values
    )
    linear_correlation_collector.calculate_linear_correlation(data_set)
    linear_correlation_collector.show_plot()

    for row in linear_correlation_collector.correlation_variable_stairs:
        print(row)

    print("---------------------6---------------------")
    linear_regression_collector = LinearRegressionCollector(base_statistic_collector.avg_variable_values)
    linear_regression_collector.calculate_linear_regression(data_set)

    for row in linear_regression_collector.linear_regression_coefficient_variable_stairs:
        for element in row:
            print(str(element), end="\t\t\t")
        print()


if __name__ == "__main__":
    main()
