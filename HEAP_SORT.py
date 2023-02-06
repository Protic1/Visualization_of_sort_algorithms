import time
from VISUALIZATION import *

class HEAP_SORT:
    def __init__(self, array, screen_size_x, screen_size_y):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "HEAP SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    def __reset_colors_heap(self):
        x = 1
        sum = 0
        self.higlight_color = []
        level = 0
        level_color = [PURPLE, YELLOW, CYAN, ORANGE, DARKGREEN, DARKPURPLE, DARKBLUE, BROWN, LIGHTPURPLE, DARKRED]
        while sum + x < len(self.array_for_sorting):
            sum += x
            self.higlight_color.extend([level_color[level]] * x)
            x *= 2
            level += 1
        if sum < len(self.array_for_sorting):
            self.higlight_color.extend([level_color[level]] * (len(self.array_for_sorting) - sum))

    #function that sorts an array using specific algorithm, later will be used for performance testing
    def sort(self):
        time_start = time.time()
        array = self.array_for_sorting.copy()
        #making heap from the given array
        for i in range(1, len(array)):
            nhe = array[i]
            self.number_of_array_access += 1
            s = i
            f = (s - 1) // 2
            self.number_of_array_access += 1
            self.number_of_compariosons += 1
            while s > 0 and array[f] < nhe:
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                array[s] = array[f]
                s = f
                f = (s - 1) // 2
            self.number_of_array_access += 1
            array[s] = nhe

        #using generated heap for sorting
        for i in range(len(array) - 1, 0, -1):
            self.number_of_array_access += 1
            last = array[i]
            self.number_of_array_access += 1
            self.array_for_sorting[i] = self.array_for_sorting[0]
            self.number_of_array_access += 1
            self.array_for_sorting[0] = last
            f = 0
            while f < i and 2 * f + 1 < i:
                s = 2 * f + 1
                self.number_of_array_access += 1
                self.number_of_compariosons += 1
                if array[s + 1] > array[s] and s + 1 < i:
                    s = s + 1

                self.number_of_compariosons += 1
                self.number_of_array_access += 1
                if array[f] < array[s]:
                    self.number_of_array_access += 1
                    array[f], array[s] = array[s], array[f]
                else:
                    break
                f = s

        self.time_duration = time.time() - time_start

    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    #making class iterable so it could be used with function next, this is used so every step could be visualized
    def __iter__(self):
        #making heap from the given array
        for i in range(1, len(self.array_for_sorting)):
            nhe = self.array_for_sorting[i]
            s = i
            f = (s - 1) // 2
            while s > 0 and self.array_for_sorting[f] < nhe:
                self.array_for_sorting[s] = self.array_for_sorting[f]
                s = f
                f = (s - 1) // 2
                self.__reset_colors()
                self.higlight_color[s] = RED
                self.higlight_color[f] = RED
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
            self.__reset_colors()
            self.higlight_color[s] = RED
            self.higlight_color[f] = RED
            self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
            yield self
            self.array_for_sorting[s] = nhe

        self.__reset_colors_heap()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
        yield self

        #using generated heap for sorting
        for i in range(len(self.array_for_sorting) - 1, 0, -1):
            last = self.array_for_sorting[i]
            self.array_for_sorting[i] = self.array_for_sorting[0]
            self.array_for_sorting[0] = last
            f = 0
            while f < i and 2 * f + 1 < i:
                s = 2 * f + 1
                if self.array_for_sorting[s + 1] > self.array_for_sorting[s] and s + 1 < i:
                    s = s + 1
                if self.array_for_sorting[f] < self.array_for_sorting[s]:
                    self.array_for_sorting[f], self.array_for_sorting[s] = self.array_for_sorting[s], self.array_for_sorting[f]
                else:
                    break

                self.__reset_colors_heap()
                self.higlight_color[f] = RED
                self.higlight_color[s] = RED
                for x in range(i , len(self.array_for_sorting)):
                    self.higlight_color[x] = GREEN
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
                f = s