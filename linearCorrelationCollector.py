class LinearCorrelationCollector:

    def __init__(self, avg_variable_values, standard_deviation_variable_values):
        self.standard_deviation_variable_values = standard_deviation_variable_values
        self.avg_variable_values = avg_variable_values
        self.correlation_variable_stairs = []

    def calculate_linear_correlation(self, data_set):
        variables_count: int = len(data_set[0])  # with class
        instances_count: int = len(data_set)
        for i in range(variables_count):
            correlation_variable_values = []
            for j in range(i, variables_count, 1):
                covariance = self.__calculate_covariance(data_set, i, j, instances_count)
                correlation = covariance / (self.standard_deviation_variable_values[i]
                                            * self.standard_deviation_variable_values[j])
                correlation_variable_values.append(round(correlation, 3))
            self.correlation_variable_stairs.append(correlation_variable_values)

    def __calculate_covariance(self, data_set, x_index, y_index, instances_count) -> float:
        sum: float = 0.0
        for instance_index in range(instances_count):
            x_variable_difference = data_set[instance_index][x_index] - self.avg_variable_values[x_index]
            y_variable_difference = data_set[instance_index][y_index] - self.avg_variable_values[y_index]
            sum += x_variable_difference * y_variable_difference
        return round(sum / instances_count, 3)
