import operator
from termcolor import colored

trunk = "||%|%||"
trunk_color = 'red'
trunk_count = 1
trunk_length = 6
leaf = "%%"
leaf_color = 'magenta'
leaves_width = 20
#leaf_count = [1, 3, 5, 7, 9, 12, 15, 17, 19, 21, 23, 25, 27, 29, 31]

SCREEN_WIDTH = 100
centered = operator.methodcaller('center', SCREEN_WIDTH)

#for number_of_leaves in leaf_count:
for number_of_leaves in range(1, leaves_width, 1):
    print(colored(centered(leaf * number_of_leaves), leaf_color))

while trunk_count <= trunk_length:
    print(colored(centered(trunk), trunk_color))
    trunk_count += 1
else:
    print("Wao .... Tree printed") #This else is printed when while loop is finished completely without "break" statement