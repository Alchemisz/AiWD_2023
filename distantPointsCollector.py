class DistantPointsCollector:

    def __init__(
            self,
            first_quartile_variable_values,
            third_quartile_variable_values,
            inter_quartile_range_variable_values
    ):
        self.firstQuartileVariableValues = first_quartile_variable_values
        self.thirdQuartileVariableValues = third_quartile_variable_values
        self.interQuartileRangeVariableValues = inter_quartile_range_variable_values
        self.distantPointVariableValues = []

    def calculate_distant_point(self, data_set):
        variables_count = len(data_set[0])  # with class
        instances_count = len(data_set)
        for i in range(variables_count):
            current_variable_distant_points = []
            for j in range(instances_count):
                current_variable_value = data_set[j][i]
                if self.__is_distant_point(i, current_variable_value):
                    current_variable_distant_points.append(current_variable_value)
            self.distantPointVariableValues.append(current_variable_distant_points)

    def __is_distant_point(self, variable_index, variable_value):
        border = 1.5 * self.interQuartileRangeVariableValues[variable_index]
        lower_border = self.firstQuartileVariableValues[variable_index] - border
        upper_border = self.thirdQuartileVariableValues[variable_index] + border
        return variable_value < lower_border or variable_value > upper_border
