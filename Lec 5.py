"""                                     **kwargs     ( Keyword Argument )
The following keyword argument will be discussed here in this lecture 5

1) linewidth = int or float value.            To change the width of line
2) Antialiased  = bool Value                  To Smooth the curve shape
3) Color = "green"  or c = "yellow or y"      To mention color of the line
4) dashes: this is used to customize the dash line . It takes list or tuple (2 value int or float)
The first argument represnts the length of a dash and the second represent the space b/w dash

5) linestyle or ls is used to represents the style of line. We have only 4 styles available
mentioned in Lecture 3.
6) marker : if we use a keyword marker. The line will already be there and the default color will
be blue as for line. but if we want to change the color of the marker we can do this by using
"markeredgecolor"

7) markevery = 2. it will use the marker at every second point. if it is
markevery = 3 it will use the marker at every third point


"""

import matplotlib.pyplot as plt
import numpy as np
a = [1,2,3,4,5,6,7,8,9,10,12,15]
b = np.array([0,11,12,13,17,20,26,30,40,50,70,80,90,100])
c = np.array([3,6,9,12])

# plt.plot(a, lw = 10)
# plt.title("1: LineWidth")
# plt.show()

# plt.plot(a,antialiased = False , lw = 20)
# plt.title("2: Antialiased = False. The Edges are Blurry")
# plt.show()

# plt.plot(a,antialiased = True, lw = 20)
# plt.title("2: Antialiased = True. The Edges are Clear")
# plt.show()

# plt.plot(a,antialiased = True, ls = ":" ,lw = 4, color = "cyan",marker = "D",ms = 10,mfc = "y")
# plt.title("3: For Color")
# plt.show()

# plt.plot(a, c = 'g', dashes = [10,25])
# plt.plot(c,c = "b",dashes = (50,20))
# plt.title("4: Dash Line Customization ")
# plt.show()

# plt.plot(c,color = 'y',linestyle = ':')
# plt.title("5: LineStyle or ls")
# plt.show()

# plt.plot(c,marker = 'o')
plt.plot(b,lw = 6,marker = "d",markersize = 15, mec = "w",mfc = 'y',markevery = 3)
plt.plot(a,marker = "D",ms = 10,mfc = 'c',markevery = 2)
plt.title("6: Marker color changing")

plt.show()

# Note:: Make sure both a and b has same values of x and y wil make the graph properly


"""
CHAT GPT HELP

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y,
         linewidth=2.5,
         antialiased=True,
         color='green',
         dashes=(5, 2),
         linestyle='--',
         marker='o',
         markersize = 15,
         markeredgecolor='red',
         markerfacecolor = "c",
         markevery=2)

plt.title("Matplotlib Plot Customization")
plt.show()

"""