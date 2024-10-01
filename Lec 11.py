"""                          plt.grid()
The grid function in matplotlib.pyplot module is used to enable grid in the Figure.
The Syntax                  plt.grid(b = bool Value, which = "both", axis = "both, **kwargs)

1) b is a boolein value that is used to enable or disable the grid.
2) which is used to select major or minor gridlines or both. the default value is both
3) axis is used to select axis for gridlines. The axis can be 'x', 'y', or both. default is both
for axis = 'x' the grid lines will be parallel to y and vice versa
4) The **kwargs is used to customize the gridlines.

Remember:The b may not work. but the presence of **kwargs make sure the availability of gridlines
 We can use keyword argument to select color, size, line style,line width for our gridlines

Note:: To enable the minor gridlines we need to call plt.minorticks_on() function then we will be
able to see minor gridlines






"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y,lw = 5)

# Customize the grid
plt.grid(color='g', linestyle='--', linewidth=1, axis='both', which='major')
plt.title("Major gird lines with both axis")
plt.show()

b = np.tan(x)
plt.plot(x, b,lw = 5)
plt.minorticks_on()
plt.grid(color = "k", ls = '-', lw = 1,axis = 'both',which='minor')
plt.title("Minor Grid Lines with both axis")
plt.show()

d = np.cos(x)
plt.plot(x, d,lw = 5)
plt.minorticks_on()
plt.grid(color = "g", ls = '-', lw = 1,axis = 'x',which='both')
plt.title("both grid lines with axis = 'x'")
plt.show()


d = np.cos(x)
plt.plot(x, d,lw = 5)
plt.minorticks_on()
plt.grid(color = "y", ls = '-', lw = 1,axis = 'y',which='both')
plt.title("both grid lines with axis = 'y'")
plt.show()

f = np.cosh(x)
plt.plot(x, f,lw = 5)
plt.minorticks_on()
plt.grid(color = "c", ls = '-', lw = 1,axis = 'both',which='both')
plt.title("grid lines with both axis and both Major and Minor")
plt.show()