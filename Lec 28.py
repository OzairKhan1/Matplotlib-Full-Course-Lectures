"""
                                    Types of Plot in pyhon
Line plot
Bar Plot
Scatter Plot
Histogram
Pie Chart
Area Plot
Box Plot
Violin Plot
Heatmap
Pair Plot
Joint Plot
Strip Plot
Swarm Plot
KDE Plot
Count Plot
Rug Plot
Step Plot
Error Bar Plot
Stem Plot
3D Plot
Bubble Plot
Polar Plot

We will be using the first 6 mostly


1)
Line Plot
Description:
A line plot is a type of chart that displays information as a series of data points called
'markers' connected by straight
line segments. It is particularly useful for visualizing trends over time or continuous data.
"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Creating the line plot
plt.plot(x, y,ls = '-',lw = 5,color = 'y',marker = 'o',ms = 10,mfc = 'k',mec = 'g')

# Adding titles and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis',labelpad=10,family = 'fantasy',style = 'italic',weight = 'bold',size = 30,color = 'y')
plt.ylabel('Y-axis',labelpad= 20,family = 'fantasy',style = 'italic',weight = 'bold',color = 'c')
plt.tight_layout()
# Displaying the plot
plt.show()
