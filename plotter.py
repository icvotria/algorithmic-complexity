import matplotlib.pyplot as plt
import random
from bubble_sort import bubble_sort
from timer import timer
from shuffle import shuffle
from quicksort import quicksort

def reversed_number_generator(x):
    numbers = [i for i in range(x)]
    num_list = numbers[::-1]
    return num_list

def shuffled_number_generator(x):
    numbers = [i for i in range(x)]
    random.shuffle(numbers)
    return numbers

def shuffled_input_generator():
    values = []
    for i in range(0, 30001, 50):
        values.append(shuffled_number_generator(i))
    return values

def input_generator(type):
    values = []
    for i in range(0, 60001, 50):
        values.append(type(i))
    return values

def find_length(inputs):
    return [len(i) for i in inputs]

def algo_timer(algo, input):
    output = []
    for i in input:
        output.append(timer(algo, i))
    return output

def plotter(x_values, y_values, name):
    plt.plot(x_values, y_values)
    plt.xlabel('size')
    plt.ylabel('time')
    plt.title(name)
    plt.show()

def plot_bubble_sort():
    inputs = input_generator(reversed_number_generator)
    y = algo_timer(bubble_sort, inputs)
    x = find_length(inputs)
    plotter(x, y, 'bubble')

def plot_shuffle():
    inputs = input_generator(reversed_number_generator)
    y = algo_timer(shuffle, inputs)
    x = find_length(inputs)
    plotter(x, y, 'shuffle')
    
def plot_quicksort():
    inputs = input_generator(shuffled_number_generator)
    y = algo_timer(bubble_sort, inputs)
    x = find_length(inputs)
    plotter(x, y, 'quicksort')