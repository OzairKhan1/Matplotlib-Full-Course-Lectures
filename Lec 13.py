"""                               Legend  1
The legend is used to identify vaious cureves in a Figure having colored marker and label
    We can use three ways to Use Labels in Python

1) using "label" key word.
while using plt.plot() we need to use the keyword label = "name of the curve"
This is a safe method to use the legend

2) We can use iterable of strings. That Iterable could be in tuple or list.
But in this method We should be very careful to used iterable of strings. Any exchange in the names
will assign a Wrong label to curve.

3) In this method we use (handles & labels) to assign Legend.
Remember:: Both must be iterable. the former is handle and the later must be iterable of string.
"""

import matplotlib.pyplot as plt
import numpy as np

# Method 1: We have used labels while plotting the curves
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,label = 'sin(x)')
plt.plot(x,z,label = 'cos(x)')
plt.legend()
plt.show()

# Method 2
a = np.tan(x)
b = np.sin(x)
plt.plot(x,a,'c*-')
plt.plot(x,b,'kD:',markevery = 100)
plt.legend(['tan(x)','sin(x)'])
plt.show()

#Method 3:
""" In this Method we use (handles and labels) both are iterable. It means they could either be
tuple or list. 
Remember:: The plt.plot() return a single list object. we need to unpack that as a tuple. 
and that would be our handle. then we use that handle with our iterable string. 
"""

c = np.array([1,2,3,4])
a = c**2
b = c**3
square, = plt.plot(c,a)
cube, = plt.plot(c,b)
plt.legend([square,cube],['square','cube'])
plt.show()

# we can use one handle or both or more but they must be iterable
c = np.array([1,2,3,4])
e = c**2.17
f = c**5
exponential, = plt.plot(c,e)
fifthPower, = plt.plot(c,f)
plt.legend((exponential,),["Expo"])
plt.show()

#More legend in a single Figure
y = np.sin(x)
z = np.cos(x)
c = np.exp(x)
l1, = plt.plot(x,y)
l2,= plt.plot(x,z)
square, = plt.plot(x,x**2)
cube, = plt.plot(x,x**3)
expo, = plt.plot(x,c)
plt.legend([l1,l2,square,cube,expo],['sin(x)','cos(x)','square','cube','expo'])
plt.show()
