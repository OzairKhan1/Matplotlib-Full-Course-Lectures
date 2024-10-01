"""                                  Scatter Plot

                            Syntax::
 plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None,
  alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

1) x and y are array like compulsory values
2) s : is used for size. it could be a float or array optional
3) marker: by default the miarker is circle (o) and can be used various markers explained in lec 3
4) c : is used for color. it could be a single color or array like optional
5) cmap: is used  to impose the mentioned color on  the marker
6) alpha: is used for transperacy of the plot
7) plotnonfinitebool, default: False
Whether to plot points with nonfinite c (i.e. inf, -inf or nan). If True the points are drawn
 with the bad colormap color (see Colormap.set_bad).


A scatter plot is a type of data visualization that uses dots to represent values for two
 different numerical variables. The position of each dot on the horizontal and vertical axis
indicates values for an individual data point.

Key Characteristics of Scatter Plots:

1) Two Numerical Variables:
Each point on the scatter plot represents an observation from the dataset, with its
x-coordinate corresponding to the value of one variable and its y-coordinate corresponding
to the value of another variable.

2) Visualization of Relationships:
Scatter plots are used to observe and show relationships between two numerical variables.
They can help to identify correlations, trends, and patterns in the data.

3) Identifying Outliers:
Outliers, or points that deviate significantly from the other data points, can be easily
identified on a scatter plot.

4) Clusters and Patterns:
Scatter plots can reveal clusters of points, which might indicate the presence
of different groups or patterns within the data.

5) Correlation:
Scatter plots can indicate the strength and direction of a relationship between two
 variables. A positive correlation is indicated when the dots trend upwards from left to
 right, while a negative correlation is indicated when the dots trend downwards.
"""

import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# plt.scatter(x,y,s = 200,c = 'red',ec = 'y',marker='d',linewidths=3,alpha=0.7)
plt.title("Common Customization of Scatter Plot")
# plt.show()


# we can use different size and points for corresponding points.
# we don't know which one is corresponds to which value. so we use colorbar() from plt
# plt.scatter(x,y,s = sizes,c = colors,ec = 'y',cmap='Set2')
plt.title("Various Size and Colors: Used cmap to")
# cbar = plt.colorbar()
# cbar.set_label("Youtube Data")
plt.xscale('log')
plt.yscale('log')
# plt.show()


# Real data from Youtube APi

data = pd.read_csv("data Scatter plot.csv")
views = data['view_count']
likes = data['likes']
ratio = data['ratio']

# print("before: ",len(data))      len is
# data.drop(data[data['view_count'] == views.max()].index,axis = 0,inplace = True) # delete video with max views
# print(f"the data is {len(data)}")

plt.scatter(views,likes,ec = 'y')
plt.title("Various Size and Colors: Used cmap to")
cbar = plt.colorbar()
cbar.set_label("Satisfication")
cbar.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
cbar.set_ticklabels(['0%', '25%', '50%', '75%', '100%'])
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Youtube Views")
plt.ylabel("Youtube Likes")
plt.title("View Vs Like. Trending videos has high like with high views")


y_min, y_max  = plt.ylim()
x_min, x_max = plt.xlim()

x = np.linspace(x_min, x_max, 200)
slope = (y_max - y_min) / (x_max - x_min)
y = y_min + slope * (x - x_min)
plt.plot(x,y)
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)

plt.show()



"""                Help from Chat Gpt about Cbar
1) in the example shown below the cbar.set_ticks can be used without labels but labels 
can't be used without ticks. 
2)                   
                      """


# Sample data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

# Create scatter plot with color mapping
scatter = plt.scatter(x, y, c=colors, cmap='viridis')

# Add color bar with specified padding
cbar = plt.colorbar(scatter, pad=0.1)

# Customize color bar
cbar.set_label("Satisfaction", fontsize=12,color = 'red')
cbar.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
cbar.set_ticklabels(['0%', '25%', '50%', '75%', '100%'])
cbar.outline.set_edgecolor('b')
cbar.ax.invert_yaxis()
cbar.ax.set_aspect(10)
# plt.clim(0,1)

# Show plot
# plt.show()


