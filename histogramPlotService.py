import matplotlib.pyplot as plt


class HistogramPlotService:

    def __init__(self, data_set, variable_index: int):
        variable_values = []
        for instance_index in data_set:
            variable_values.append(instance_index[variable_index])

        fig, ax = plt.subplots()
        ax.hist(variable_values)
        plt.title('Liczba win w zależności od typu')

    def show_plot(self):
        plt.show()
