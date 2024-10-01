"""             plt.xlim()          &            plt.ylim()
both xlim and ylim() are used to set the range of x-axis and y-axis respectively
Syntax::                      plt.xlim(*args, **kwargs)            plt.ylim(*args, **kwargs)

There are three ways to call them.
1) To get the default value set while figure execution we can get
left,right = plt.xlim() :This will return the l and r value. Remember left and right are variables only
Similarly for y-axis:          top,bottom  = plt.ylim()

2) to set the range of x-axis and y-axis.  we use        plt.xlim((2,6)) , plt.ylim((-1,10))
the low and high values are passed to the function as a tuple()

3) We can use **kwargs to set the value.
    plt.xlim(left = -4, right = 10)               plt.ylim(top = -10, bottom = 10)

Remember: in case of xlim() if 1 value is given that will be treated as the left value or we can
set one value and leave the other using **kwargs
        plt.xlim(right = -2)                         plt.ylim(top = 10)
        plt.xlim(2): this will be considered left value
        plt.ylim(-4): This will be considered the bottom value



"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x,y,lw = 3,ls = ':')

# left,right = plt.xlim()   # this is used to get the original value of x-axis
# print(left,right)
# bottom, top = plt.ylim() # this is used to get the original value of y-axis
# print(bottom, top)

plt.xlim((0,10))
plt.ylim((-2,2))
plt.xlabel("x")
plt.ylabel('y')
plt.title("Sin(x)")
plt.grid(color = 'y',axis='both', which='both',lw = 1,alpha = 0.5)
plt.show()


# Exmpl 2: to set one value for xlim and ylim
a = np.cos(x)
plt.plot(x,a)
plt.xlim(-1)
plt.ylim(-5)
plt.show()

# Expl 3: Using **kwargs to set xlim and ylim

b = np.tan(x)
plt.plot(x,b)
plt.xlim(left = 0, right= 6)
plt.ylim(bottom = -20, top =20)
plt.show()