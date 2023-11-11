import math
import sys


class BaseStatisticCollector:

    def __init__(self):
        self.variables_count: int = 0
        self.instances_count: int = 0
        self.min_variable_values: list[float] = []
        self.max_variable_values: list[float] = []
        self.avg_variable_values: list[float] = []
        self.standard_deviation_variable_values: list[float] = []

    def calculate_base_statistic(self, dataset):
        self.variables_count = len(dataset[0])  # with class
        self.instances_count = len(dataset)

        for i in range(self.variables_count):
            min_variable_value = sys.maxsize
            max_variable_value = -sys.maxsize - 1
            sum = 0
            for j in range(self.instances_count):
                current_variable_value = dataset[j][i]
                if current_variable_value < min_variable_value:
                    min_variable_value = current_variable_value
                if current_variable_value > max_variable_value:
                    max_variable_value = current_variable_value
                sum += current_variable_value
            self.__add_avg_variable_value(round(sum / self.instances_count, 3))
            self.__add_min_variable_value(min_variable_value)
            self.__add_max_variable_value(max_variable_value)
        self.__calculate_standard_deviation(dataset)

    def __calculate_standard_deviation(self, data_set):
        for i in range(self.variables_count):
            current_variable_avg = float(self.avg_variable_values[i])
            sum = 0
            for j in range(self.instances_count):
                current_variable_value = float(data_set[j][i])
                sum += pow((current_variable_value - current_variable_avg), 2)
            self.__add_standard_deviation_variable_value(round(math.sqrt(sum / self.instances_count), 3))

    def __add_min_variable_value(self, min_variable_value):
        self.min_variable_values.append(min_variable_value)

    def __add_max_variable_value(self, max_variable_value):
        self.max_variable_values.append(max_variable_value)

    def __add_avg_variable_value(self, avg_variable_value):
        self.avg_variable_values.append(avg_variable_value)

    def __add_standard_deviation_variable_value(self, standard_deviation_variable_value):
        self.standard_deviation_variable_values.append(standard_deviation_variable_value)
