import numpy


class QuartileCollector:

    def __init__(self):
        self.firstQuartileVariableValues = []
        self.secondQuartileVariableValues = []
        self.thirdQuartileVariableValues = []
        self.interQuartileRangeVariableValues = []
        self.zeroOneQuantileVariableValues = []
        self.zeroNineQuantileVariableValues = []

    def calculate_quartiles(self, dataset):
        transposed_data_set = self.__transpose_data_set(dataset)  # transposition
        transposed_sorted_data_set = self.__sort_columns(transposed_data_set)
        for row in transposed_sorted_data_set:
            self.__add_first_quartile(round(numpy.percentile(row, 25), 3))
            self.__add_second_quartile(round(numpy.percentile(row, 50), 3))
            self.__add_third_quartile(round(numpy.percentile(row, 75), 3))
            self.__add_zero_one_quantile(round(numpy.percentile(row, 10), 3))
            self.__add_zero_nine_quantile(round(numpy.percentile(row, 90), 3))
        self.__calculate_inter_quartile_ranges()

    @staticmethod
    def __transpose_data_set(dataset):
        return list(map(list, zip(*dataset)))

    @staticmethod
    def __sort_columns(dataset):
        for column in dataset:
            column.sort()
        return dataset

    def __calculate_inter_quartile_ranges(self):
        for i in range(len(self.firstQuartileVariableValues)):
            self.__add_inter_quartile_range(
                round(self.thirdQuartileVariableValues[i] - self.firstQuartileVariableValues[i], 3))

    def __add_first_quartile(self, first_quartile_value):
        self.firstQuartileVariableValues.append(first_quartile_value)

    def __add_second_quartile(self, second_quartile_value):
        self.secondQuartileVariableValues.append(second_quartile_value)

    def __add_third_quartile(self, third_quartile_value):
        self.thirdQuartileVariableValues.append(third_quartile_value)

    def __add_inter_quartile_range(self, inter_quartile_range):
        self.interQuartileRangeVariableValues.append(inter_quartile_range)

    def __add_zero_one_quantile(self, zero_one_quantile):
        self.zeroOneQuantileVariableValues.append(zero_one_quantile)

    def __add_zero_nine_quantile(self, zero_nine_quantile):
        self.zeroNineQuantileVariableValues.append(zero_nine_quantile)
