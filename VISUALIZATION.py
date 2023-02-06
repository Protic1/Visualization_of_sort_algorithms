import pygame
import numpy as np
import math
from COLORS import *

class visualize_sort:
    def __init__(self, screen_size_x, screen_size_y, name, array_for_sorting):
        #dimensions allowed for visualization algorithm, possible update for window resizing and chosing algorithms to be shown
        self.size_x = screen_size_x
        self.size_y = screen_size_y
        #creating surface for one sorting algorithm(including boundary box and text)
        self.sort_surface = pygame.Surface((self.size_x, self.size_y))
        #selecting default system font to get around any missing font problems on other machines, size is fixed, possible problem
        self.font = pygame.font.Font(None, 25)
        #rendering name of sorting algorithm
        self.sort_name = self.font.render(name, True, WHITE, BLACK)
        #getting text boundaries for easier blitting(drawing) onto surface
        self.text_box = self.sort_name.get_rect()
        self.text_box.center = (self.size_x // 2, self.sort_name.get_size()[1] // 2)
        #making rectangle to house all bars for sorting algorithm
        self.bounding_box = pygame.Rect(0, self.sort_name.get_size()[1] // 2, self.size_x + 2 * 2, self.size_y + self.sort_name.get_size()[1] // 2 + 2)
        self.final_surface = pygame.Surface((self.size_x + 2 * 2, self.size_y + self.sort_name.get_size()[1] + self.sort_name.get_size()[1] // 2))
        #calculating maximum size for one column in algorithm, maximum value as height should be set maybe, but it would require scaling data, possible update in future
        self.bar_width = self.size_x // len(array_for_sorting)
        #remmember array for scaling
        self.backup_array = array_for_sorting.copy()
        #current array
        self.progress = array_for_sorting.copy()

    def __draw_bar(self, array, i, color):
        #scaling number to fill available space
        height = math.ceil(np.interp(array[i], [min(self.backup_array), max(self.backup_array)], [1, self.size_y]))
        x = self.bar_width * i
        y = self.size_y - height
        bar = pygame.Rect(x, y, self.bar_width, height)
        pygame.draw.rect(self.sort_surface, color, bar)

    def render_frame(self, frame_array, frame_array_colors):
        #clearing previously drawn surface, and saving array as progress
        self.progress = frame_array
        self.sort_surface.fill(BLACK)
        self.final_surface.fill(BLACK)
        #drawing boundary box and sorting algorithm name
        for bar in range(len(frame_array)):
            self.__draw_bar(frame_array, bar, frame_array_colors[bar])
        self.final_surface.blit(self.sort_surface, (2, self.sort_name.get_size()[1]))
        pygame.draw.rect(self.final_surface, WHITE, self.bounding_box, 2)
        self.final_surface.blit(self.sort_name, self.text_box)
