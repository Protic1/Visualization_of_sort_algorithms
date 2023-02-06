import time
from VISUALIZATION import *

class BUBBLE_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "BUBBLE SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    #function that sorts an array using specific algorithm, later will be used for performance testing
    def sort(self):
        array = self.array_for_sorting.copy()
        time_start = time.time()
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                if(array[j] > array[j + 1]):
                    self.number_of_array_access += 1
                    array[j], array[j + 1] = array[j + 1], array[j]
        self.time_duration = time.time() - time_start

    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with function next, this is used so every step could be visualized
    def __iter__(self):
        for i in range(len(self.array_for_sorting)):
            for j in range(0, len(self.array_for_sorting) - i - 1):
                if (self.array_for_sorting[j] > self.array_for_sorting[j + 1]):
                    self.array_for_sorting[j], self.array_for_sorting[j + 1] = self.array_for_sorting[j + 1], \
                                                                               self.array_for_sorting[j]
                self.__reset_colors()
                for x in range(len(self.array_for_sorting) - i, len(self.array_for_sorting)):
                    self.higlight_color[x] = GREEN
                self.higlight_color[j] = RED
                self.higlight_color[j + 1] = BLUE
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self