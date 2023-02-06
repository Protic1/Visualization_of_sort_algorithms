import time
from VISUALIZATION import *

class SELECTION_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "SELECTION SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    def sort(self):
        array = self.array_for_sorting.copy()
        time_start = time.time()
        for i in range(len(array)):
            min = i
            for j in range(i + 1, len(array)):
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                if array[min] > array[j]:
                    min = j
            array[i], array[min] = array[min], array[i]
            self.number_of_array_access += 1
        self.time_duration = time.time() - time_start

    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    def __iter__(self):
        for i in range(len(self.array_for_sorting)):
            min = i
            for j in range(i + 1, len(self.array_for_sorting)):
                self.__reset_colors()
                if self.array_for_sorting[min] > self.array_for_sorting[j]:
                    min = j
                for x in range(i):
                    self.higlight_color[x] = GREEN
                self.higlight_color[i] = RED
                self.higlight_color[j] = BLUE
                self.higlight_color[min] = YELLOW
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
            self.array_for_sorting[i], self.array_for_sorting[min] = self.array_for_sorting[min], self.array_for_sorting[i]