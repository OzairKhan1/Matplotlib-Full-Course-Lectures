"""                           How to use FORMATTING in Plot Function
    NOTE: There is not space b/w specifying formatting in double or single quotes

#       Example:  plt.plot(a,b,"ro-")  This is the correct formatting. leaving space b/w
r: red   o:Circle  and   -: solid line         will throw an error

In Formatting we have this combination of *args
[color line Marker] any combination of these 3. None of them are compulsory.
We can give 1 or 2 or 3 or none of them. If None of them is given it will be selected by default
from color cycle and the line style will be of Solid Pattern. As mentioned in Lecture 3

We can even specify them using keyword arguments. by specifying. name as we will discussed below
"""
# No need of x coordinate
import matplotlib.pyplot as plt
import numpy as np

a = [1,2,3,4]
b = [5,6,7,8]
c = np.arange(4)
d = np.arange(10,14)


e = np.array([2,4,6,8])
f = np.array([14,16,18,20])

plt.plot(a,"c*-.")       # the color is cyan, The marker is *, and the line is dash-dot
plt.plot(b,"+k--")       # The marker is +, The color is black, and the line is dash dash
plt.plot(f,"-yo")        # The line is solid, the color is yellow, and the marker is Circle
plt.title("Simple Formatting")
plt.show()

plt.plot(e,color = 'green',marker = "*", linestyle = "-.",linewidth = 5, markersize = 10,markeredgecolor = "k",markerfacecolor = "b")
plt.title("KeyWord Argument Properly Named")
plt.show()

# or we can use shortcut symbol instead of writing whole name of the color
plt.plot(f,c = 'g',marker = "d", ls = "-",lw = 4, ms = 10,mec = "y", mfc = "b")
plt.title("**Kwargs  Shortcut Used")
plt.show()

# There is no shortcut symbole for marker. While the rest is represented with symbols

""" Remember whenever there is a conflict b/w *args and **kwargs. the **keyars has a high precedence
 and will override the *args. as shown in the example  """

plt.plot(e,"r",color = "yellow") # Here color = Yellow has high precedence and will override the red
plt.title("High Precednce of **kwargs")
plt.show()
# Example 2 is the best example of **kwargs high precedence. all the color and marker overrides
plt.plot(e,"*g--",e**2,"yo:",e**3,color = "red",ls = "-",lw = 3)
plt.title("High Precednce of **kwargs")
plt.show()

plt.plot(e,"*g--",e**2,"yo:",e**3,'c-.')
plt.title("Multpiple Plots in single Window")
plt.show()

"""  
                                            From Chat Gpt 
                                            
plt.plot(x, y, markerfacecolor="yellow", color="purple", linestyle="--", markersize=12, marker="o")

Remeber:: 
In matplotlib, when you use keyword arguments like color, linestyle, marker, markerfacecolor,
 and markersize with the plt.plot() function, the order of these arguments does not matter. 
 
                                        OR
plt.plot(x, y, markerfacecolor="yellow", color="purple", linestyle="--", markersize=12, marker="o")

                                        OR
plt.plot(x, y, color="purple", linestyle="--", marker="o", markerfacecolor="yellow", markersize=12)


"""