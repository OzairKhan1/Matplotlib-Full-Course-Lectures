"""                 Adjusting the location of xticks and yticks
Syntax:::                 xticks(ticks  = None, label = None, **kwargs)

1) ticks: is an array like optional that is used to set the correct location of xticks
2) label: is an array like optional that is used to name the ticks on x or y-axis
3) **kwargs: is used to customize the ticks


*** Remember:: ticks lable can only be passed when the ticks array is passed. otherwise it will
take the default values.

Note:: To disable the ticks from the corresponding axis. we need to pass an empty list in the
xticks or yticks function
"""

import matplotlib.pyplot as plt
import numpy as np

#Exmple 1 :: basic ticks
c = np.arange(1,11)
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend()
plt.xticks(np.arange(0,12,2),color = 'red',size = 20,rotation = 30)
plt.title("Only ticks without Label", size= 'xx-large')
plt.grid()
plt.show()

#example 2 : tick position and labels
c = np.arange(1,11)
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend()
plt.xticks(np.arange(0,12,2),['zero','Two',"Four","Six","Eight","Ten"],color = 'red',size = 20)
plt.yticks(np.arange(0,1500,400),color = 'g',rotation = 90)
plt.title("Both ticks and Labels", size= 'xx-large')
plt.grid()
plt.show()


#Exple 3: To disable ticks
c = np.arange(1,11)
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend()
plt.xticks([])
plt.yticks([])
plt.title("Disable Ticks from both x and y axis", size= 'xx-large')
plt.grid()
plt.show()