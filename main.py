import sys
import time
import argparse
from argparse import RawTextHelpFormatter

import numpy as np
import pygame
import random
import numpy
import pygame_widgets

from INSERTION_SORT import *
from SELECTION_SORT import *
from BUBBLE_SORT import *
from SHAKER_SORT import *
from SHELL_SORT import *
from HEAP_SORT import *
from QUICK_SORT import *
from MERGE_SORT import *
from BOGO_SORT import *
from BUTTON import *
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider

parser = argparse.ArgumentParser("sort_visualization", formatter_class = RawTextHelpFormatter)
parser.add_argument("-len","--array-len", dest="array_len", type=int, nargs='?', default = 100, help="Input len of the array for sorting, for best result chose number 500 %% num = int")
parser.add_argument("-t", "--type-of-array", dest="type", type=int, nargs='?', default=0, help="Chose a type of array for sorting\nOptions:\n0)Random array with repetition\n1)Random array without repetition\n2)Almost sorted array\n3)Sorted array")
parser.add_argument("-p", "--shell-sort-increment-sequence", dest="shell_param", type=int, nargs='?', default=0, help="Chose increment set for shell sort\nOptions:\n0)Shell's original sequence:N/2, N/4,...,1\n1)Knuth's increments:1,4,13,...\n2)Sedgewick's increments:1,8,23,77,281,...\n3)Hibbard's increments:1,3,7,15,31,63,...\n4)Papernov & Stasevich increment:1,3,5,9,17,33,65,...\n5)Pratt:1,2,3,4,6,8,9,12,16,18,24,27,...")
args = parser.parse_args()

sort_array = []
if args.type == 0:
    sort_array = numpy.random.randint(0, 100, args.array_len)
elif args.type == 1:
    sort_array = []
    while len(sort_array) < args.array_len:
        n = random.randint(0, 500)
        if n not in sort_array:
            sort_array.append(n)
elif args.type == 2:
    sort_array = []
    for i in range(args.array_len):
        sort_array.append(random.randint(0, 500))
    sort_array.sort()
    for i in range(random.randint(10, 15)):
        pos = random.randint(0, args.array_len - 6)
        sort_array[pos], sort_array[pos + random.randint(1, 5)] = sort_array[pos + random.randint(1, 5)], sort_array[pos]
elif args.type == 3:
    sort_array = []
    for i in range(args.array_len):
        sort_array.append(random.randint(0, 500))
    sort_array.sort()

if args.array_len <= 0:
    print("Wrong value for array len")
    exit()
if args.shell_param < 0 or args.shell_param > 5:
    print("Wrong value for shell sort parameter")
    exit()
if args.type < 0 or args.type > 3:
    print("Wrong value for array type")
    exit()

pygame.init()
clock = pygame.time.Clock()
screen_size = pygame.display.set_mode([1700, 960], pygame.RESIZABLE)
screen = pygame.Surface([1700,960])

insertion_sort = INSERTION_SORT(sort_array, 500, 300)
insertion_sort_process = iter(insertion_sort)

selection_sort = SELECTION_SORT(sort_array, 500, 300)
selection_sort_process = iter(selection_sort)

bubble_sort = BUBBLE_SORT(sort_array, 500, 300)
bubble_sort_process = iter(bubble_sort)

shaker_sort = SHAKER_SORT(sort_array, 500, 300)
shaker_sort_process = iter(shaker_sort)

shell_sort = SHELL_SORT(sort_array, 500, 300, args.shell_param)
shell_sort_process = iter(shell_sort)

heap_sort = HEAP_SORT(sort_array, 500, 300)
heap_sort_process = iter(heap_sort)

quick_sort = QUICK_SORT(sort_array, 500, 300)
quick_sort_process = iter(quick_sort)

merge_sort = MERGE_SORT(sort_array, 500, 300)
merge_sort_process = iter(merge_sort)

bogo_sort = BOGO_SORT(sort_array, 500, 300)
bogo_sort_process = iter(bogo_sort)


#PART THAT CHECKS FOR PERFORMANCE
print("INSERTION SORT PERFORMANCE")
insertion_sort.sort()
print("Time: " + str(insertion_sort.time_duration))
print("Number of comparisons: " + str(insertion_sort.number_of_compariosons))
print("Number of array access: " + str(insertion_sort.number_of_array_access))
print()

print("SELECTION SORT PERFORMANCE")
selection_sort.sort()
print("Time: " + str(selection_sort.time_duration))
print("Number of comparisons: " + str(selection_sort.number_of_compariosons))
print("Number of array access: " + str(selection_sort.number_of_array_access))
print()

print("BUBBLE SORT PERFORMANCE")
bubble_sort.sort()
print("Time: " + str(bubble_sort.time_duration))
print("Number of comparisons: " + str(bubble_sort.number_of_compariosons))
print("Number of array access: " + str(bubble_sort.number_of_array_access))
print()

print("SHAKER SORT PERFORMANCE")
shaker_sort.sort()
print("Time: " + str(shaker_sort.time_duration))
print("Number of comparisons: " + str(shaker_sort.number_of_compariosons))
print("Number of array access: " + str(shaker_sort.number_of_array_access))
print()

print("SHELL SORT PERFORMANCE")
shell_sort.sort()
print("Time: " + str(shell_sort.time_duration))
print("Number of comparisons: " + str(shell_sort.number_of_compariosons))
print("Number of array access: " + str(shell_sort.number_of_array_access))
print()

print("HEAP SORT PERFORMANCE")
heap_sort.sort()
print("Time: " + str(heap_sort.time_duration))
print("Number of comparisons: " + str(heap_sort.number_of_compariosons))
print("Number of array access: " + str(heap_sort.number_of_array_access))
print()

print("QUICK SORT PERFORMANCE")
quick_sort.sort()
print("Time: " + str(quick_sort.time_duration))
print("Number of comparisons: " + str(quick_sort.number_of_compariosons))
print("Number of array access: " + str(quick_sort.number_of_array_access))
print()

print("MERGE SORT PERFORMANCE")
merge_sort.sort()
print("Time: " + str(merge_sort.time_duration))
print("Number of comparisons: " + str(merge_sort.number_of_compariosons))
print("Number of array access: " + str(merge_sort.number_of_array_access))
print()

if args.array_len > 500:
    pygame.quit()
    print("Visualisation for such big data set is not possible")
    exit()

running = True
paused = False
def change_paused():
    global paused
    paused = not paused

pause = Button(screen_size, 1530, 5, 160, 100, text="PAUSE", onClick=change_paused)
speed = Slider(screen_size, 1580, 150, 20, 150, min=8, initial=17, max=100, handleColour=(255,0,0), vertical=True)

while running:
    if paused == False:
        screen_size.fill(BLACK)
        screen.fill(BLACK)
        next(insertion_sort_process, insertion_sort.finished())
        next(selection_sort_process, selection_sort.finished())
        next(bubble_sort_process, bubble_sort.finished())
        next(shaker_sort_process, shaker_sort.finished())
        next(shell_sort_process, shell_sort.finished())
        next(heap_sort_process, heap_sort.finished())
        next(quick_sort_process, quick_sort.finished())
        next(merge_sort_process, merge_sort.finished())
        next(bogo_sort_process, bogo_sort.finished())

        screen.blit(insertion_sort.visualizer.final_surface, [0,0])
        screen.blit(selection_sort.visualizer.final_surface, [510,0])
        screen.blit(bubble_sort.visualizer.final_surface, [1020,0])
        screen.blit(shaker_sort.visualizer.final_surface, [0, 320])
        screen.blit(shell_sort.visualizer.final_surface, [510, 320])
        screen.blit(heap_sort.visualizer.final_surface, [1020, 320])
        screen.blit(quick_sort.visualizer.final_surface, [0, 640])
        screen.blit(merge_sort.visualizer.final_surface, [510, 640])
        screen.blit(bogo_sort.visualizer.final_surface, [1020, 640])

    curr_x, curr_y = screen_size.get_size()
    new_surface = pygame.transform.scale(screen, (curr_x, curr_y))
    pos_x = np.interp(1530, [0, 1700], [0, curr_x])
    pause._x = pos_x + 5
    pause._width = curr_x - pos_x - 5
    pause._height = np.interp(100, [0, 960], [0, curr_y])
    speed._x = int(pos_x + (curr_x - pos_x - 10) // 2)
    speed._y = int(np.interp(150, [0,960], [0, curr_y]))
    speed.handleRadius = int(np.interp(20, [0, 1700], [0, curr_x]))
    screen_size.blit(new_surface, [0,0])
    pause.draw()
    speed.draw()
    events = pygame.event.get()
    pygame_widgets.update(events)
    pygame.time.wait(speed.value)
    pygame.display.flip()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

pygame.quit()