import csv

from baseStatisticCollector import BaseStatisticCollector
from boxPlotService import BoxPlotService
from dataPreProcessingService import DataPreProcessingService
from distantPointsCollector import DistantPointsCollector
from histogramPlotService import HistogramPlotService
from linearCorrelationCollector import LinearCorrelationCollector
from linearRegressionCollector import LinearRegressionCollector
from linearRegressionPlotService import LinearRegressionPlotService
from quantileCollector import QuartileCollector

# WINES
WINE_TYPE_VARIABLE_INDEX: int = 0
ALCOHOL_VARIABLE_INDEX: int = 1
CAP_SHAPE: int = 1


def main():
    file = open('grzybki.csv')
    type(file)

    csv_reader = csv.reader(file, delimiter=',')
    column_names = next(csv_reader)

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
        print(len(instance_index))

    print("---------------------4--------------------- CORRELATION")
    linear_correlation_collector = LinearCorrelationCollector(
        base_statistic_collector.avg_variable_values,
        base_statistic_collector.standard_deviation_variable_values
    )
    linear_correlation_collector.calculate_linear_correlation(data_set)
    linear_correlation_collector.show_plot(column_names)

    for instance_index in linear_correlation_collector.correlation_variable_stairs:
        print(instance_index)

    print("---------------------6---------------------")
    linear_regression_collector = LinearRegressionCollector(base_statistic_collector.avg_variable_values)
    linear_regression_collector.calculate_linear_regression(data_set)
    linear_regression_collector.show_plot(column_names)

    for instance_index in linear_regression_collector.linear_regression_coefficient_variable_stairs:
        for element in instance_index:
            print(str(element), end="\t\t\t")
        print()

    print("---------------------HISTOGRAM---------------------")
    histogram_plot_service = HistogramPlotService(data_set, CAP_SHAPE)
    histogram_plot_service.show_plot()

    print("---------------------BOX PLOT---------------------")
    box_plot_service = BoxPlotService(data_set, WINE_TYPE_VARIABLE_INDEX, ALCOHOL_VARIABLE_INDEX)
    box_plot_service.show_plot()

    print("---------------------LINEAR REGRESSION---------------------")
    linear_regression_plot_service = LinearRegressionPlotService(
        data_set,
        WINE_TYPE_VARIABLE_INDEX,
        ALCOHOL_VARIABLE_INDEX,
        linear_regression_collector.linear_regression_coefficient_variable_stairs[WINE_TYPE_VARIABLE_INDEX][
            ALCOHOL_VARIABLE_INDEX]
    )
    linear_regression_plot_service.show_plot()


if __name__ == "__main__":
    main()
