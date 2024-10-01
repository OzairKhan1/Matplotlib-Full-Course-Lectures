"""
                                2) Vertical Bar Graph

            Syntax::   plt.bar(x,h,w,bottom = None ,align = 'center', data = None, **kwargs )

1) x and height is compulsory parameter
2) width w by default is 0.8. it could even be an array of data. so every bar will have different w
3) bottom can also be an array, so every bar will have different bottom
4) allgin: for tick is center and can we change it to edge. using align = 'edge' it will go to left
to take it to the right edge we need to make w = -ve
5) kwargs use for color customization and e.t.c


Note: To Represents the data on the bars we need to use another function from Matplotlib
Syntax::  bar_label(container, labels=None, *, fmt='%g', label_type='edge', padding=0, **kwargs)
1) container: is returned by plt.bar() once we use this statement
2) labels: Remember this keyword is a labels & not a label which is used to show on the bars
3) padding: is used for distance
4) **kwargs for customization. shown in the example 1





Description:
A vertical bar graph (or vertical bar chart) is a type of plot that presents categorical
data with rectangular bars with heights proportional to the values they represent. The bars
 are plotted vertically, making it easy to compare different categories.

Key Characteristics:
Bars: Rectangular bars that represent different categories.
Height: The height of each bar is proportional to the value it represents.
Axes: The x-axis typically represents the categories, while the y-axis represents the values.
Common Uses:
Categorical Data: Comparing the values of different categories.
Frequency Distribution: Displaying the frequency of different categories in a dataset.
Surveys and Polls: Representing responses to survey questions.


"""

import numpy as np
import matplotlib.pyplot as plt

#Exp1            :   Simplist Bar Graph
h = np.array([200,300,150,400,300])
h2 = np.array([20,40,60,80,100])
courses = ['Mech','Elec','Cse','Civil','Chemical']
barplot = plt.bar(courses,h)
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Students Per Course")
plt.bar_label(barplot,label = h,label_type='edge',size = 20,color = 'r',padding=5,rotation = 90)
plt.ylim(0,500)
plt.yticks(np.arange(0,501,50))
plt.show()


#Example 2: The Width is changed and the color of bar graph from default to yellow
plt.bar(courses,h,width = 0.4,color = 'y')
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Changed Width and Colors for all the Bars")
plt.show()

#Exp3:: Different colors for different courses
colors = ['orange','g','y','c','k']
plt.bar(courses,h,width = 0.4,color = colors)
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Different Colors for every bar")
plt.show()

#Exp4:: We can have different width, different colors and different bottom for all the bars

bottom = [10,20,30,40,50]
colors = ['orange','g','y','c','k']
w = [0.4,0.6,0.7,0.8,1]
plt.bar(courses,h,width = w,color = colors,bottom = bottom)
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Different Width, Color, and Bottom")
plt.show()

""" In all the above case the allignment was center. Now to change the alignment we can 
use the keyword 'align' = 'edge', """
# Example 5: alignment to left edge
plt.bar(courses,h, width = w, color = colors,align='edge')
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Left Edge Alignment")
plt.tick_params(axis = 'x', length = 10,width = 5,color = 'm')
plt.show()

# Example 6:: To change the alignment into right edge we need to make w negative
plt.bar(courses,h, width = -0.2, color = colors,align='edge')
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Right Edge Alignment")
plt.tick_params(axis = 'x', length = 10,width = 5,color = 'm') #to see ticks clearly
plt.xticks()
plt.show()

#Example 7:: To change the linewidth we can use 'linewidth' keyword and 'edgecolor'
plt.bar(courses,h, width = -0.2,align='edge',linewidth = 3,edgecolor = 'm' )
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Changing linewidth and Edge Color")
plt.tick_params(axis = 'x', length = 10,width = 5,color = 'm') #to see ticks clearly
plt.xticks()
plt.show()

