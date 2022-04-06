# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [i for i in range(50)]
# corresponding y axis values
y = [i**2 for i in x]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
