#                                         Matplotlib Lecture 2
"""
    Matplotlib has a module called Pyplot that is used to plot the graph and customize it
 The basic of plot.
 * Two axis are required::: x_axis and y_axis.     :: x_axis is not important but has to be given
 * We can work with numpy array or simple list.

 Basic Commands
 1) plt.plot()   : To plot the Figure.
 2) plt.show()    : To Show the Figure
 3) plt.xlabel("x-axis")      for x_axis  : you need to specify axis in the double or single quotes
 4) plt.ylabel("y-axis")      for naming y_axis
 5) plt.title ("MY first Plot")          : This is used to name the plot


 Note:: plt.show() is needed to be at the last of all the labeling otherwise it won't show on
 the Figure.

 """
import matplotlib.pyplot as plt
import numpy as np


a = [1,2,3,4]
b = [5,6,7,8]

c = np.arange(4)
d = np.arange(5,9)

e = np.array([2,4,6,8])
f = np.array([12,14,16,18])

plt.plot(a,b)
plt.xlabel("x-axis")
plt.ylabel("y_axis")
plt.title("My First Figure")
plt.show()

plt.xlabel("x-axis")
plt.ylabel("y_axis")
plt.title("My Second Figure")
plt.plot(c,d)
plt.show()


plt.xlabel("x-axis")
plt.ylabel("y_axis")
plt.title("My Third Figure")
plt.plot(e,f)
plt.show()




