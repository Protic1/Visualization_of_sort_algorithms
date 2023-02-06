import time
from VISUALIZATION import *

class SHELL_SORT:
    def __init__(self, array, screen_size_x, screen_size_y, increment_selection = 0):
        #initialization of array for sorting
        self.array_for_sorting = array.copy()
        #making object of visualizator for specific sorting algorithm
        self.visualizer = visualize_sort(screen_size_x, screen_size_y, "SHELL SORT", self.array_for_sorting)
        self.higlight_color = [WHITE] * len(self.array_for_sorting)
        #making increment sequence from selected option
        self.increment_sequence = []
        #Shell's original sequence
        if increment_selection == 0:
            increment = len(self.array_for_sorting) // 2
            while increment > 0:
                self.increment_sequence.append(increment)
                increment = increment // 2
        #Knuth's increments
        elif increment_selection == 1:
            increment = 1
            while increment < len(self.array_for_sorting):
                self.increment_sequence.append(increment)
                increment = increment * 3 + 1
            self.increment_sequence.reverse()
        #Sedgewick's increments
        elif increment_selection == 2:
            self.increment_sequence.append(1)
            k = 1
            increment = pow(4, k) + 3 * pow(2, k - 1) + 1
            while increment < len(self.array_for_sorting):
                self.increment_sequence.append(increment)
                k += 1
                increment = pow(4, k) + 3 * pow(2, k - 1) + 1
            self.increment_sequence.reverse()
        #Hibbard's increments
        elif increment_selection == 3:
            k = 1
            while True:
                increment = pow(2, k) - 1
                if(increment <= len(self.array_for_sorting)):
                    self.increment_sequence.append(increment)
                else:
                    break
                k += 1
            self.increment_sequence.reverse()
        #Papernov & Stasevich increment
        elif increment_selection == 4:
            k = 1
            self.increment_sequence.append(1)
            while True:
                increment = pow(2, k) + 1
                if (increment <= len(self.array_for_sorting)):
                    self.increment_sequence.append(increment)
                else:
                    break
                k += 1
            self.increment_sequence.reverse()
        #Pratt
        elif increment_selection == 5:
            self.increment_sequence.append(1)
            for i in range(2, len(self.array_for_sorting)):
                set = self.__prime_factors(i)
                if max(set) <= 3:
                    self.increment_sequence.append(i)
            self.increment_sequence.reverse()

        self.time_duration = 0
        self.number_of_compariosons = 0
        self.number_of_array_access = 0

    def __prime_factors(self, num):
        array = set()
        while num % 2 == 0 and num != 0:
            array.add(2)
            num = num / 2
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0 and num != 0:
                array.add(int(i))
                num = num / i
        if num > 2:
            array.add(num)
        return array

    def __reset_colors(self):
        self.higlight_color = [WHITE] * len(self.array_for_sorting)

    #function to sort array using specific algorithm, later will be used for performance testing
    def sort(self):
        array = self.array_for_sorting.copy()
        time_start = time.time()
        for inc in self.increment_sequence:
            j = inc
            while j < len(array):
                i = j - inc
                while i >= 0:
                    self.number_of_array_access += 1
                    self.number_of_compariosons += 1
                    if array[i + inc] > array[i]:
                        break
                    else:
                        self.number_of_array_access += 1
                        array[i + inc], array[i] = array[i], array[i + inc]
                    i = i - inc

                j += 1
        self.time_duration = time.time() - time_start
    #setting behavior when final iteration is complited
    def finished(self):
        self.__reset_colors()
        self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)

    # making class iterable so it could be used with funtion next, this is used so every step could be visualized
    def __iter__(self):
        for inc in self.increment_sequence:
            j = inc
            while j < len(self.array_for_sorting):
                i = j - inc
                while i >= 0:
                    if self.array_for_sorting[i + inc] > self.array_for_sorting[i]:
                        break
                    else:
                        self.array_for_sorting[i + inc], self.array_for_sorting[i] = self.array_for_sorting[i], \
                                                                                     self.array_for_sorting[i + inc]
                    i = i - inc
                    self.__reset_colors()
                    self.higlight_color[i + inc] = RED
                    self.higlight_color[i] = RED
                    self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                    yield self
                self.__reset_colors()
                self.higlight_color[i + inc] = RED
                self.higlight_color[i] = RED
                self.visualizer.render_frame(self.array_for_sorting, self.higlight_color)
                yield self
                j += 1