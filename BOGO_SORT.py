from VISUALIZATION import *
import random

class BOGO_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "BOGO SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    #function that sorts an array using specific algorithm, later will be used for performance testing
    def sort(self):
        done = False
        while done == False:
            if self.__is_sorted() == False:
                random.shuffle(self.array_for_sorting)
            else:
                done = True

    def __is_sorted(self):
        flag = 0
        i = 1
        while i < len(self.array_for_sorting):
            if (self.array_for_sorting[i] < self.array_for_sorting[i - 1]):
                flag = 1
            i += 1
        if flag == 1:
            return False
        else:
            return True

    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with function next, this is used so every step could be visualized
    def __iter__(self):
        done = False
        while done == False:
            if self.__is_sorted() == False:
                random.shuffle(self.array_for_sorting)
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
            else:
                done = True