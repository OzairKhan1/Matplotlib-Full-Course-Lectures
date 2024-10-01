"""                                Legend()   2
In this lecture we will be studing the location and number of columns in the legend

1) Keyword  "loc" is used to specify the location of legend in the boundry box.
The default value for loc is "best" or code = 0
2) Keyword "ncol" is used to specify the number of columns we want in our legend
The default value for ncol is 1

Best: plt.legend(loc='best') or plt.legend(loc=0)
Upper right: plt.legend(loc='upper right') or plt.legend(loc=1)
Upper left: plt.legend(loc='upper left') or plt.legend(loc=2)
Lower left: plt.legend(loc='lower left') or plt.legend(loc=3)
Lower right: plt.legend(loc='lower right') or plt.legend(loc=4)
Right: plt.legend(loc='right') or plt.legend(loc=5)
Center left: plt.legend(loc='center left') or plt.legend(loc=6)
Center right: plt.legend(loc='center right') or plt.legend(loc=7)
Lower center: plt.legend(loc='lower center') or plt.legend(loc=8)
Upper center: plt.legend(loc='upper center') or plt.legend(loc=9)
Center: plt.legend(loc='center') or plt.legend(loc=10)

The above are the common location along with their codes.
***** The default code is 0 or loc = best.
**** It is easy to call with their names instead of codes

"""
import matplotlib.pyplot as plt
import numpy as np


c = np.array([1,2,3,4])
a = c**2
b = c**3
square, = plt.plot(c,a)
cube, = plt.plot(c,b)
plt.legend([square,cube],['square','cube'],loc = "upper left",ncol = 1)
plt.show()

# Example 2
x = np.linspace(0, 10, 100)
y = np.tan(x)
z = np.cos(x)
c = np.exp(x)
l1, = plt.plot(x,y,lw = 5,color = 'k')
l2,= plt.plot(x,z)
square, = plt.plot(x,x**2)
cube, = plt.plot(x,x**3)
plt.legend([l1,l2,square,cube],['tan(x)','cos(x)','square','cube'],loc = "upper center",ncol =3)
plt.show()

# In the above example we have 3 cols for 4 legends
