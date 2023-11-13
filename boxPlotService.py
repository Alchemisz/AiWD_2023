import matplotlib.pyplot as plt


class BoxPlotService:

    def __init__(self, data_set, variable_x_index: int, variable_y_index: int):
        classes = []
        for instance_index in range(len(data_set)):
            classes.append(data_set[instance_index][variable_x_index])

        classes = list(set(classes))

        plot_data_set = []
        for i in range(len(classes)):
            plot_data_set.append([])

        instances_count = range(len(data_set))
        classes_count = range(len(classes))

        for instance_index in instances_count:
            for class_index in classes_count:
                instance_class = data_set[instance_index][variable_x_index]
                if classes[class_index] == instance_class:
                    plot_data_set[class_index].append(data_set[instance_index][variable_y_index])

        plt.boxplot(plot_data_set, vert=True)

        # Dodawanie tytułu i etykiet na osiach
        plt.title("Wykres pudełkowy dla zmiennych: Typ wina i alkohol")
        plt.ylabel("Alkohol")
        plt.xlabel("Typ wina")

    def show_plot(self):
        plt.show()
