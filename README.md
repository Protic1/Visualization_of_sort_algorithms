This is a project made to visualize sort algorithms using Python and Pygame. All sorts of algorithms are made in separate files, so they could be upgraded or changed individually without breaking the code.
Project is suposed to be run from terminal in which case it could be called with:
'''console
...Visualisation_of_sort_algorithms>python main.py -h
usage: sort_visualization [-h] [-len [ARRAY_LEN]] [-t [TYPE]] [-p [SHELL_PARAM]]

optional arguments:
  -h, --help            show this help message and exit
  -len [ARRAY_LEN], --array-len [ARRAY_LEN]
                        Input len of the array for sorting, for best result chose number 500 % num = int
  -t [TYPE], --type-of-array [TYPE]
                        Chose a type of array for sorting
                        Options:
                        0)Random array with repetition
                        1)Random array without repetition
                        2)Almost sorted array
                        3)Sorted array
  -p [SHELL_PARAM], --shell-sort-increment-sequence [SHELL_PARAM]
                        Chose increment set for shell sort
                        Options:
                        0)Shell's original sequence:N/2, N/4,...,1
                        1)Knuth's increments:1,4,13,...
                        2)Sedgewick's increments:1,8,23,77,281,...
                        3)Hibbard's increments:1,3,7,15,31,63,...
                        4)Papernov & Stasevich increment:1,3,5,9,17,33,65,...
                        5)Pratt:1,2,3,4,6,8,9,12,16,18,24,27,...
'''
