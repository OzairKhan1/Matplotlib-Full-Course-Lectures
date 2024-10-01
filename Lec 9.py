"""                               Title
        Syntax:    plt.plot("Title",fontdict,loc,pad,**kwargs)

1) Title: is used to name the Figure
2) fontdict: is used to customize the font of title. like x-label and y-label
3) loc: is used to choose location for title. it can takes 3 values.
    a) loc = "left"        b) loc = "center"        c) loc = "right"     :: default value is center
4) pad is used to choose to position of title w.r.t above axis.
    the +ve value will move the title above the upper x-axis and -ve will bring it below
5) The **kwargs is used to customize the font as explained in x-label and y-label




"""

import matplotlib.pyplot as plt
import  numpy as np

a = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

plt.plot(a,"yd-",lw = 6,mfc = 'black',ms = 10,markevery = 2)
plt.xlabel("x-axis",{"size":20},labelpad=4, size = 'medium',style="italic")
plt.ylabel("y-axis",{"size":20}, size = 'x-large',style="italic",family = 'monospace')
plt.title("My Figure",{"color":"black","style":"italic"},loc="center",pad=10,weight = "bold")
plt.show()


fdict = {'size': 10,
    'color': 'yellow',
    'family': 'monospace',
    'weight': 10,
    'style': 'italic',
    'backgroundcolor': 'black'}

d = np.arange(10,14)
plt.plot(d,"yo-",lw = 10,mfc = "k",ms = 10)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Simple Figure",fontdict=fdict,loc='right',pad=20,family = "monospace")
plt.show()