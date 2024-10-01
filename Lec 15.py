"""                                   Legend    3
How to change the location of Legend ( Extension of Lec 14  )

****        Adjusting location of Legend any where in the Figure. usind "loc" and bbox_to_anchor()

2) using bbox_to_anchor() we can create a new box and place our legend over there.
It takes 2 or 4 values. in case of 2 values the height and width of bbox is zero and the whole
bbox is considered a single point.
while in case of 4 (float) values height and width are also given


In the previous lecture we have discussed how we can put a legend in 10 different position using
Keyword "loc" with its value or code. But what if we want to place somewhere else other than those
position. Then we use
                          tuple of two values. (x and y coordinates) to place the legend
For this we need to make sure the grid is on, so we can easily find the coordinates

Remember:The highest value of x and y are considered 1.we have to put legend according to them
"""

import matplotlib.pyplot as plt
import numpy as np

c = np.array([1,2,3,4])
a = c**2
b = c**3
plt.plot(c,a,label = 'square')
plt.plot(c,b,label = 'cube')
plt.xlim(0,4)
plt.ylim(0,75)
plt.legend(loc = (0.5,0.8))
plt.title("Tuple for legend")
plt.grid()
plt.show()

# To place legend as per our own choice. We need to get max and min value of x and y coordinate
# in a Figure. We can do this using xlim and ylim function


c = np.array([1, 2, 3, 4])
a = c**2
b = c**3

# Plot with labels
plt.plot(c, a, label='square')
plt.plot(c, b, label='cube')
left, right = plt.xlim()
bottom,top = plt.ylim()
print(left,right,bottom,top)

x_coord = (3 - left) / (right - left)     # eq ----------- (1)
y_coord = (50 - bottom) / (top - bottom)  # eq ----------- (2)

"""With the help of the above formula we can easily place the legend by just replacing the 
coordinate of x and y in the above eq 1 and eq 2.
Remember:: The coordinate represents the lower left location of the legend
"""
plt.title("Customize coordinate for Legend")
plt.legend(loc = (x_coord,y_coord))
plt.grid()
plt.show()

# Now show the plot
plt.show()


# plt.bbox_to_anchor()
c = np.array([1, 2, 3, 4])
a = c**2
b = c**3
# Plot with labels
plt.plot(c, a, label='square')
plt.plot(c, b, label='cube')
plt.title("bbox_to_anchor() with  height and width")
plt.grid(color = 'y')
plt.legend(loc = "center right",bbox_to_anchor = (0.5,0.5,0.5,0.5))
plt.show()

#bbox_to_anchor() with not height and width
c = np.array([1, 2, 3, 4])
a = c**2
b = c**3
# Plot with labels
plt.plot(c, a, label='square')
plt.plot(c, b, label='cube')
plt.title("bbox_to_anchor() with not height and width")
plt.grid(color = 'y')
plt.legend(loc = "center",bbox_to_anchor = (0.5,0.5))
plt.show()


