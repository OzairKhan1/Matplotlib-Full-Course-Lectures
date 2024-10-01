"""                                    Legend  6
How to change the look of a Legend in Python

1) markerfirst : is a keyword that takes a bool value. by default markerfirst = True
In Legend we have two things. a) marker   b) label
by default the markerfirst = True. So we see the markerfirst and then label.
***      To change it change the bool value to False.

2) frameon: is a keyword that is used to to enable or disable the edge/boundery of a legend.
frameon has a bool value = True . (normally legend with a boundery)

3) Shadow: is a keyword that is used to draw a shadow of a legend.
by default this value is None.

4) columnspacing: is a keyword that is used to for spacing b/w column of legend.
The default value is none.



"""

import matplotlib.pyplot as plt
import numpy as np

c = np.array([1,2,3,4])

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(markerfirst = False,facecolor = 'y', fontsize = 25,edgecolor = "k")
# the label is first and then the marker once the markerfirst is False
plt.title("Label is First and then Marker")
plt.show()

#Exple 2

c = np.array([1,2,3,4])

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(markerfirst = False, frameon = False)  # the label is first and then the marker
plt.title("No boundery around the Legend")
plt.show()

#Exple 3

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(markerfirst = False,facecolor = "y",shadow = True,fontsize = 30)
plt.title("With Shadow",color = 'r',size = 20)
plt.show()

#Exple of Columnspacing

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.plot(c**4,label = "fourth")
plt.plot(c**5,label = "fifth")
plt.legend(ncol = 3,columnspacing = 5)
plt.title("Column spacing ",color = 'g',size = 20)
plt.show()