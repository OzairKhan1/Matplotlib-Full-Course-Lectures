"""                                     Legend 5
How to change the 'fontsize' and 'color' of the Legend

1) fontsize: keyword is used to change the size of legend font. This can take. string,int,or float
Strings are "small", "medium", "large","x-small","xx-small","x-large","xx-large"
beside these string. it can take int, or float to change the font size

2) color: We can change use the keyword facecolor (bg color) . which is used to change the bg
of legend.  & we can use keyword edgecolor to change the boundry of legend

"""

import matplotlib.pyplot as plt
import numpy as np

c = np.array([1,2,3,4])

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(fontsize = 'x-large',edgecolor = 'y',facecolor = 'k',loc = "upper center",ncol = 2)
plt.show()


#Exple 2
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(fontsize = 30,edgecolor = 'k',facecolor = 'y',loc = "best")
plt.show()