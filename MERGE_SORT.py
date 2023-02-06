import time
from VISUALIZATION import *

class MERGE_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "MERGE SORT", self.array_for_sorting)
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
        width = 1
        n = len(array)
        while width < n:
            l = 0
            while l < n:
                r = min(l + (width * 2 - 1), n - 1)
                m = min(l + width - 1, n - 1)
                n1 = m - l + 1
                n2 = r - m
                L = [0] * n1
                R = [0] * n2
                for i in range(0, n1):
                    self.number_of_array_access += 1
                    L[i] = array[l + i]
                for i in range(0, n2):
                    self.number_of_array_access += 1
                    R[i] = array[m + i + 1]

                i, j, k = 0, 0, l
                while i < n1 and j < n2:
                    if L[i] <= R[j]:
                        self.number_of_array_access += 1
                        array[k] = L[i]
                        i += 1
                    else:
                        self.number_of_array_access += 1
                        array[k] = R[j]
                        j += 1
                    self.number_of_compariosons += 1
                    k += 1

                while i < n1:
                    self.number_of_compariosons += 1
                    array[k] = L[i]
                    i += 1
                    k += 1

                while j < n2:
                    self.number_of_array_access += 1
                    array[k] = R[j]
                    j += 1
                    k += 1
                l += width * 2
            width *= 2
        self.time_duration = time.time() - time_start

    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with funtion next, this is used so every step could be visualized
    def __iter__(self):
        old_array = self.array_for_sorting.copy()
        width = 1
        n = len(self.array_for_sorting)
        while width < n:
            l = 0
            while l < n:
                r = min(l + (width * 2 - 1), n - 1)
                m = min(l + width - 1, n - 1)
                n1 = m - l + 1
                n2 = r - m
                L = [0] * n1
                R = [0] * n2
                for i in range(0, n1):
                    L[i] = self.array_for_sorting[l + i]
                for i in range(0, n2):
                    R[i] = self.array_for_sorting[m + i + 1]

                i, j, k = 0, 0, l
                while i < n1 and j < n2:
                    if L[i] <= R[j]:
                        self.array_for_sorting[k] = L[i]
                        i += 1
                    else:
                        self.array_for_sorting[k] = R[j]
                        j += 1
                    k += 1
                    self.__reset_colors()
                    self.higlight_color[r - i] = RED
                    self.higlight_color[m - j] = RED
                    self.visualizer.render_frame(old_array, self.higlight_color)
                    yield self

                while i < n1:
                    self.array_for_sorting[k] = L[i]
                    self.__reset_colors()
                    self.higlight_color[r - i] = RED
                    self.higlight_color[m - j] = RED
                    self.visualizer.render_frame(old_array, self.higlight_color)
                    yield self
                    i += 1
                    k += 1

                while j < n2:
                    self.array_for_sorting[k] = R[j]
                    self.__reset_colors()
                    self.higlight_color[r - i] = RED
                    self.higlight_color[m - j] = RED
                    self.visualizer.render_frame(old_array, self.higlight_color)
                    yield self
                    j += 1
                    k += 1
                old_array = self.array_for_sorting.copy()
                l += width * 2
            width *= 2
