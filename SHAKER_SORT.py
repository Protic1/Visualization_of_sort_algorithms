import time
from VISUALIZATION import *

class SHAKER_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "SHAKER SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    #function that sorts an array using specific algorithm, later will be used for performance testing
    def sort(self):
        array = self.array_for_sorting.copy()
        change = True
        start = 0
        end = len(array) - 1
        time_start = time.time()

        while change:
            change = False

            for i in range(start, end):
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                if(array[i] > array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
                    self.number_of_array_access += 1
                    change = True

            if change == False:
                break

            change = False

            end = end - 1
            for i in range(end - 1, start - 1, - 1):
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                if(array[i] > array[i + 1]):
                    self.number_of_compariosons += 1
                    array[i], array[i + 1] = array[i + 1], array[i]
                    change = True

            start = start + 1

        self.time_duration = time.time() - time_start

    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with function next, this is used so every step could be visualized
    def __iter__(self):
        change = True
        start = 0
        end = len(self.array_for_sorting) - 1

        while change:
            change = False

            for i in range(start, end):
                if (self.array_for_sorting[i] > self.array_for_sorting[i + 1]):
                    self.array_for_sorting[i], self.array_for_sorting[i + 1] = self.array_for_sorting[i + 1], self.array_for_sorting[i]
                    change = True

                self.__reset_colors()
                self.higlight_color[i] = RED
                self.higlight_color[i + 1] = BLUE
                for j in range(start):
                    self.higlight_color[j] = GREEN
                for j in range(end + 1, len(self.array_for_sorting)):
                    self.higlight_color[j] = GREEN
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self

            if change == False:
                break

            change = False

            end = end - 1
            for i in range(end - 1, start - 1, - 1):
                if (self.array_for_sorting[i] > self.array_for_sorting[i + 1]):
                    self.array_for_sorting[i], self.array_for_sorting[i + 1] = self.array_for_sorting[i + 1], self.array_for_sorting[i]
                    change = True

                self.__reset_colors()
                self.higlight_color[i + 1] = RED
                self.higlight_color[i] = BLUE
                for j in range(start):
                    self.higlight_color[j] = GREEN
                for j in range(end + 1, len(self.array_for_sorting)):
                    self.higlight_color[j] = GREEN
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self

            start = start + 1