class DataPreProcessingService:
    variables_count: int
    instances_count: int
    avg_variable_values: list[float]

    def __init__(self, variables_count, instances_count):
        self.variables_count = variables_count
        self.instances_count = instances_count
        self.avg_variable_values = []

    def pre_process_data_set(self, data_set):
        self.__calculate_avg_variable_values(data_set)
        self.__complete_missing_data_using_avg_variable_values(data_set)

    def __calculate_avg_variable_values(self, data_set):
        for i in range(self.variables_count):
            sum: float = 0
            for j in range(self.instances_count):
                current_variable_value = data_set[j][i]
                if current_variable_value != '?':
                    sum += float(current_variable_value)
            self.__add_avg_variable_value(round(sum / self.instances_count, 3))

    def __add_avg_variable_value(self, avg_variable_value):
        self.avg_variable_values.append(avg_variable_value)

    def __complete_missing_data_using_avg_variable_values(self, data_set):
        for i in range(self.variables_count):
            for j in range(self.instances_count):
                current_variable_value = data_set[j][i]
                if current_variable_value == '?':
                    data_set[j][i] = self.avg_variable_values[i]
