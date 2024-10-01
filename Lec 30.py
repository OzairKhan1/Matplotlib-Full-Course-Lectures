"""                                      Horizantal Bar Graph

Syntax:          plt.barh(y,w,height, left = None, align = 'center',data = None,**kwargw)

1) here y axis is used to represent the unique data
2) w is used to represent the frequency
3) height is used to set the height for a bar
4) left work the same as bottom in vertical bar
5) align is used to change the position of tick
6) **kwargs is used to customize the bar like color, linewidth, and edgecolor

"""

import numpy as np
import matplotlib.pyplot as plt

#Exp1::    Simplist HBar Graph
w = np.array([200,300,150,400,300])
h2 = np.array([20,40,60,80,100])
courses = ['Mech','Elec','Cse','Civil','Chemical']
plt.barh(courses,w)
plt.xlabel("Student Enrolled")
plt.ylabel("Courses")
plt.title("Student Enrolled Per Course")
plt.tight_layout() # Without this the y axis will be showing
plt.show()

#Example 2: The Width is changed and the color of bar graph from default to yellow
plt.barh(courses,w,height = 0.4,color = 'y')
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Changed height and Colors for all the Bars")
plt.show()

#Exp3:: Different colors for different courses
colors = ['orange','g','y','c','k']
plt.barh(courses,w,color = colors)
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Different Colors for every bar")
plt.show()


#Exp4:: We can have different height, different colors and different left for all the bars

left = [10,20,30,40,50]
colors = ['orange','g','y','c','k']
h = [0.4,0.6,0.7,0.8,1]
plt.barh(courses,w,height = h,color = colors,left = left)
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Different Height, Color, and Left")
plt.show()

""" In all the above case the allignment was center. Now to change the alignment to bottom we can 
use the keyword 'align' = 'edge', """
# Example 5: alignment to left edge
left = [10,20,30,40,50]
colors = ['orange','g','y','c','k']
h = [0.4,0.6,0.7,0.8,1]
plt.barh(courses,w,height = h,color = colors,align='edge')
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Left Edge Alignment")
plt.tick_params(length = 30,width = 5,color = 'm',axis = 'y',direction = 'inout')
plt.show()

#To Shift the alignment to top we need to use the -ve height.

colors = ['orange','g','y','c','k']
plt.barh(courses,w,height = -0.4,color = colors,align='edge')
plt.xlabel('Courses')
plt.ylabel("Students Enrolled")
plt.title("Left Edge Alignment")
plt.tick_params(length = 30,width = 5,color = 'm',axis = 'y',direction = 'inout')
plt.show()