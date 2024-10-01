"""                 In This Lecture We will focus on this SYNTAX of the plot

**  plot([x],y,format,keyword Argument)   :: The [x] means that x is optional.
Remember if x is not present it will automatically starts from 0 up to num of elems in y.

*** Multiple plots can be drawn on the same figure.
plt.plot(y1,'r',y2,'g')         # No Need to mention the x values if not necessary
plot(x1,y1,"r",linewidth = 3)
plt.plot(x2,y2, "k+",markersize = 4)

Remember If no format string is given. Only the color is chosen from default Color Cycle.
it has been demonstrated with the help of example

***    in this color cycle the first color is blue, orange,grenn and so on. The line style will be
solid for all
"""


import matplotlib.pyplot as plt
import numpy as np


a = [1,2,3,4]
b = [5,6,7,8]

c = np.arange(4)
d = np.arange(10,14)


e = np.array([2,4,6,8])
f = np.array([14,16,18,20])

# Color Cycle
plt.plot(a,b,c,d,e,f)
plt.show()
plt.plot(a,b,'r',linewidth = 10)
plt.plot(c,d,"c+:",markersize = 10)
plt.plot(e,f,"ko-.")
plt.show()
# In all the above case the x coordinate is mentioned. We can plot without x as well

plt.plot(b,'r_', d, 'c:', f, 'k--',markersize = 20,linewidth = 4)
plt.show()


# Remeber whenever there is a conflict b/w *args and **kwargs. the **keyars has a high precedence
# and will override the *args. as shown in the example

plt.plot(e,"r",color = "yellow") # Here color = Yellow has high precedence and will override the red
plt.show()

"""  Extra Assingment from Chat Gpt

Color:            
"r": Red
"g": Green
"b": Blue
"c": Cyan
"m": Magenta
"y": Yellow
"k": Black
"w": White


Line Styles:

"-": Solid line
"--": Dashed line
"-.": Dash-dot line
":": Dotted line


Markers:

".": Point marker
",": Pixel marker
"o": Circle marker
"v": Triangle down marker
"^": Triangle up marker
"<": Triangle left marker
">": Triangle right marker
"1": Tri-down marker
"2": Tri-up marker
"3": Tri-left marker
"4": Tri-right marker
"s": Square marker
"p": Pentagram marker
"*": Star marker
"h": Hexagon1 marker
"H": Hexagon2 marker
"+"": Plus marker
"D": Diamond marker
"d": Thin diamond marker
"|": Vertical line marker
"_": Horizontal line marker

Note: In symbol/Characters the following symbol has been used as a marker

       *     ^    |       +             _          .      , 
       
In Number the following number has been used as a Marker

         1      2      3       4              Tri down, up, left, right
         
In letters following number has been used as a Marker
 
    "d": Thin diamond marker
    "D": Diamond marker
    "s": Square marker
    "p": Pentagram marker
    "h": Hexagon1 marker
    "H": Hexagon2 marker
    "v": Triangle down marker
    "x": Cross marker
    
     
              Examples from CHAT GPT
              
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, "r--")  # Red dashed line
plt.plot(x, y, "bs")   # Blue squares
plt.plot(x, y, "g^")   # Green triangles up

plt.show()


plt.plot(x, y, markerfacecolor="yellow", color="purple", linestyle="--", markersize=12, marker="o")

Remeber:: 
In matplotlib, when you use keyword arguments like color, linestyle, marker, markerfacecolor,
 and markersize with the plt.plot() function, the order of these arguments does not matter. 

"""