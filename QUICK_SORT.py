import time

from VISUALIZATION import *

class QUICK_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "QUICK SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    #function that sorts an array using specific algorithm, later will be used for performance testing
    def sort(self):
        time_start = time.time()
        array = self.array_for_sorting.copy()
        size = len(array)
        stack = [0] * size
        top = 0
        stack[top] = 0
        top = top + 1
        stack[top] = len(array) - 1
        while top >= 0:
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            i = (l - 1)
            self.number_of_array_access += 1
            x = array[h]

            for j in range(l, h):
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                if array[j] <= x:
                    #increment index of smaller element
                    i = i + 1
                    self.number_of_array_access += 1
                    array[i], array[j] = array[j], array[i]

            self.number_of_array_access += 1
            array[i + 1], array[h] = array[h], array[i + 1]
            p = i + 1

            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1

            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
        self.time_duration = time.time() - time_start


    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with function next, this is used so every step could be visualized
    def __iter__(self):
        size = len(self.array_for_sorting)
        stack = [0] * size
        top = 0
        stack[top] = 0
        top = top + 1
        stack[top] = len(self.array_for_sorting) - 1
        while top >= 0:
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            i = (l - 1)
            x = self.array_for_sorting[h]
            j = 0
            for j in range(l, h):
                if self.array_for_sorting[j] <= x:
                    #increment index of smaller element
                    i = i + 1
                    self.array_for_sorting[i], self.array_for_sorting[j] = self.array_for_sorting[j], self.array_for_sorting[i]

                self.__reset_colors()
                self.higlight_color[j] = RED
                self.higlight_color[i] = RED
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
            p = i + 1
            self.__reset_colors()
            self.higlight_color[j] = RED
            self.higlight_color[i] = RED
            self.higlight_color[p] =BLUE
            self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
            self.array_for_sorting[i + 1], self.array_for_sorting[h] = self.array_for_sorting[h], self.array_for_sorting[i + 1]
            yield self


            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1

            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
