import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
from timer import timer

def number_generator(x):
    numbers = [i for i in range(x)]
    num_list = numbers[::-1]
    return num_list

def input_generator():
    values = []
    for i in range(0, 100001, 5000):
        values.append(number_generator(i))
    return values

def find_length(inputs):
    return [len(i) for i in inputs]

def output_generator(algo, input):
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

inputs = input_generator()
y = output_generator(bubble_sort, inputs)
x = find_length(inputs)

plotter(x, y, 'bubble sort')