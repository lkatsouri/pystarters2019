"""
Programming is essentially a list of commands that are executed in order to produce some output
To keep track of the data, and to make it human-readable, we give names to the outputs at various points. These named
data are called variables.

There are lots of different kinds of variables types that you will encounter. We will cover some simple ones.

- Variables
A variable is something you declare, just a name you give to some value/computation so that you can read your code
"""
from numpy.core.multiarray import ndarray

a = 5
b = 10
c = a * b
a = b = 5
a, b = 5, 10
a, b = b, a

print(a)

""" try printing the sum of two variables"""

"""coding is more than just integers"""

print(type(5))

"""- Data types
    basic types (integers, floats, strings)
    data types behave differently and do different things
    
    https://docs.python.org/3/library/stdtypes.html
    
    """

my_string_variable = 'heyyyyyyyyya'
print(my_string_variable)
print(type(my_string_variable))
print(my_string_variable + ' playyya')

"""what happens if you try to add two different types?"""

"""dealing with many things (lists, tuples)"""

my_randomly_organised_stuff = [1, 55, 218, 'cheese', 14, my_string_variable, 55, 1]
my_number_list = [1, 55, 218, 555, 222, 2123, 55, 1]

"""indexing - i.e. getting stuff out of lists/arrays/etc"""

my_randomly_organised_stuff[0]

"""get the 3rd element of the list"""

my_randomly_organised_stuff[-1]

"""get the 3rd element from the end of the list"""

"""assign """

"""tuples"""
my_randomly_organised_tuple = (1, 55, 218, 'cheese', 14, my_string_variable, 55, 1)
my_randomly_organised_tuple[3]

list_tuple = tuple(my_randomly_organised_stuff)
print(type(list_tuple))

"""- mutability"""
my_randomly_organised_stuff[3] = 'gouda'

"""- print the list, see that is has changed
   - what happens if you do the same thing for my_randomly_organised_tuple?"""

my_randomly_organised_tuple[3] = 'gouda'

""""- tuple unpacking"""
my_tuple = (1, 5, 6, 60, 200, 20)
a, b, c, d, e, f = my_tuple
a, *b, c = my_tuple

""" try to split the tuple such that the first three elements go into a single variable"""

"""- dictionaries, arrays and sets"""

my_set_of_randomly_organised_stuff = set(my_randomly_organised_stuff)  # casting from a list to a set
my_number_set = set(my_randomly_organised_stuff)
my_set_of_randomly_organised_stuff.intersection(my_number_set)

my_dictionary_of_stuff = {'stringy_things': ['cheese', my_string_variable],
                          'numerical_things': [1, 55, 218, 14],
                          'the number one': 1}
my_dictionary_of_stuff.keys()
my_dictionary_of_stuff.values()
my_dictionary_of_stuff.items()

my_own_dictionary = {1: ['apple', 'orange', 'pear'],
                     2: ['dog', 'cat', 'mouse', 'sheep'],
                     3: ['yellow', 'black', 'red', 'green', 'blue']}
my_own_dictionary.get(1)[0]

"""indexing: can you get the cheese out?

my_dictionary_of_stuff.get(1)[0

Answer: my_dictionary_of_stuff['stringy_things'][0] - the key is a string therefore u need to use quotes"""

""" make a dictionary of your own that uses numbers as keys and strings as values"""

"""- Loops
    - what if we have lots of numbers to add together
    - loop through each element in a list
    - for each vs for i in
"""

for number in my_number_list:
    print(number)

for x in my_number_list:
    print(number)
"""maybe this does not work as expected. what result do you get? can you figure out what is happening?"""

"""another cool thing is it can iterate from the end bhy using [::-2]"""

"""getting the loop iteration"""

for item in my_dictionary_of_stuff.items():
    print(item)

for i, item in enumerate(my_dictionary_of_stuff.items()):
    print(i, item)

for i, item in enumerate(my_number_list):
    if i > 4:
        print(i, item)  # this will print only iterations that are after the 5th iteration

"""Conditional statements
    - what if we only want to add numbers that fulfil some specific criteria?"""

total = 0
for x in my_number_list:
    if x > 200:
        print(x)
        total += x
    elif x < 200:
        print('this number is too small to print')
    elif x == 200:
        print('200')
    else:
        print('if you are seeing this something has gone wrong')

"""what if instead of the number list you do this with my_randomly_organised_stuff
    - can you modify this code so that it still works?"""

total = 0
for i, x in enumerate(my_randomly_organised_stuff):
    if isinstance(x,int):
        if x > 200:
            print(i, x)
            total += x
        elif x < 200:
            print('this number is too small to print')
        elif x == 200:
            print('200')
    else:
        print('if you are seeing this something has gone wrong')

"""can you make it subtract 50 from the total if the value is a string? """

total = 0
for i, x in enumerate(my_randomly_organised_stuff):
    if isinstance(x,int):
        if x > 200:
            print(i, x)
            total += x
        elif x < 200:
            print('this number is too small to print')
        elif x == 200:
            print('200')
    else:
        print('if you are seeing this something has gone wrong')
        total -= 50
print(total)


"""Installing packages with pip
install numpy, matplotlib and pandas
    add some lines to the script that use numpy as matplotlib
    run the script."""

import numpy as np
import matplotlib.pyplot as plt
# this is the interactive window for plt
#matplotlib.use('tkAgg')

x = np.random.normal(np.ones(5000))
y = np.random.normal(np.ones(5000))

plt.figure()
plt.scatter(x, y, color='k')
plt.show()

"""replot the data, but plot making sure the top left quadrant is red and the bottom left quadrant black"""

import matplotlib.pyplot as plt
import  numpy as np
x = np.random.normal(np.ones(5000))
y = np.random.normal(np.ones(5000))
plt.figure()
# for each x value and its index "i"
for x_index, x_val in enumerate(x):
    if x_val < 1 and y[x_index] > 1:
            plt.scatter(x_val, y[x_index], color='r')
    else:
        plt.scatter(x_val, y[x_index], color='k')
plt.show()

"""Python can be executed in different ways. Integrated Development Environments (IDEs) allow you do to this in a user
friendly way (think Pycharm, or MATLAB). However, the simplest thing we can do is run python ourselves from the
command line."""

x = np.random.normal(np.ones(5000))
y = np.random.normal(np.ones(5000))
plt.figure()
both = np.logical_and(x<1, y>1)
plt.scatter(x[both], y[both], color='r')
plt.scatter(x[~both], y[~both], color='k')
plt.show()


"""
make a script
the data is a track (x,y positions) of a mouse running around a box
    - load using numpy
    - plot the data
    - cut the data down to the first minute and plot that on top in a different color
    - find the points where the mouse crosses the 200 line in x
    - plot a red dot at these x, y locations 
    - print the estimated x_speed to the console (hint the x speed is in the csv) 
    - save the figure

"""
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
tracks = pd.read_csv('/Users/loukia/Code/pystarters-assignments/pystarters2019-master/data/tracks.csv')
plt.figure()
plt.scatter(x, y, color='k')
plt.show()
