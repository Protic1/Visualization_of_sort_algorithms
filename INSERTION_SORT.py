import time
from VISUALIZATION import *

class INSERTION_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "INSERTION SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    #function that sorts an array using specific algorithm, later will be used for performance testing
    def sort(self):
        array_for_test = self.array_for_sorting.copy()
        start_time = time.time()
        for i in range(1, len(array_for_test)):
                K = array_for_test[i]
                self.number_of_array_access += 1
                j = i - 1
                self.number_of_compariosons += 1
                while j >= 0 and array_for_test[j] > K:
                    self.number_of_array_access += 1
                    self.number_of_compariosons += 1
                    array_for_test[j + 1] = array_for_test[j]
                    self.number_of_array_access += 1
                    j = j - 1
                array_for_test[j + 1] = K
                self.number_of_array_access += 1
        self.time_duration = time.time() - start_time

    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with function next, this is used so every step could be visualized
    def __iter__(self):
        for i in range(1, len(self.array_for_sorting)):
            K = self.array_for_sorting[i]
            j = i - 1
            while j >= 0 and self.array_for_sorting[j] > K:
                self.__reset_colors()
                #setting color to already sorted part of array
                for x in range(i):
                    self.higlight_color[x] = GREEN
                self.higlight_color[i] = RED
                self.higlight_color[j] = BLUE
                self.array_for_sorting[j + 1] = self.array_for_sorting[j]

                #calling visualization function for current frame
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
                j = j - 1
            self.array_for_sorting[j + 1] = K