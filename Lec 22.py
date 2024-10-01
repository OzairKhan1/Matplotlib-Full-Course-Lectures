"""                         xticks and yticks Customization

We will be using. plt.tick_params()

                        Syntax::     plt.tick_params(axis = "both",**kwargs)
Noramlly all the changes will be reflected on both x and y axis, or we can change to any using
axis = 'x' for x-axis and   axis = 'y' for y-axis

The following are main common customization

1) length: this keyword argument will change the length of ticks on selected axis.
2) Width: this keyword argument will change the width of ticks on selected axis
3) color: this keyword argument will change the color
4) pad: this keyword argument will change the distance of labels from selected axis
5) direction: this keyword argument will change the direction.
In direction the default value is out. and we also we           "in" or "inout"
6) Which: this keyword argument is used to reflect changes on the ticks. default  value is 'major'

Remember:: The minorticks are in off position. To enable or reflect any changes on them we have
to enable them first using                 plt.minorticks_on()


7) The keyword:: left,right,bottom,top uses a bool value to select ticks on the axis.
the default value for left and bottom = True so we have ticks only available on them.
"""

#Exp 1: Changes reflects on both the axis with major tick

import matplotlib.pyplot as plt
import numpy as np

# for title and title_fontsize
c = np.arange(1,11)
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend()
plt.title("Ticks-params() with mostly default value",color = 'g',size = 15)
plt.grid()
plt.tick_params(axis ='both',length =10,width =5,pad =10,color ='y',which ='major',direction ='out')
#The axis,which and direction are default parameter.
plt.show()

#Exple 2: Minor ticks on and let select x - axis only
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend()
plt.title("Ticks changes on only x-axis",color = 'k',size = 15)
plt.grid()
plt.minorticks_on()
plt.tick_params(axis ='x',length =10,width =7,pad =10,color ='r',which ='minor',direction ='inout')
plt.show()

#Exple 3: ticks on all the axis

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend()
plt.title("ticks on all sides",color = 'g',size = 15)
plt.grid()
plt.minorticks_on()
plt.tick_params(axis ='both',length =5,width =7,pad =10,color ='r',which ='both',direction ='in',right = True,top = True)
plt.show()