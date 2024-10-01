"""                               tick_params()  2
                Changing the appearance of label and gridlines

1) labelsize: To change the size of label only
2)labelcolor: To change the color of label only
3)colors: To change the color of both ticks and label
4)labelleft,labelright,labelbottom,labeltop: To enable ticks and labels on selected sides
the default value for labelleft, labelbottom = True.

                        For changing the grid Appearances
We have to pass the below parameter to                      plt.tick_params()

1) grid_color: To change the color of grid lines. We have already seen this in grid function
2) grid_linewidth: To change the width of gridlines
3) gird_linestyle: To select line style available in the matplotlib
4) grid_alpha: To choose the transparacy of gridlines. alpha can be b/w 0 and 1
1 means full opaque         0 full transparacy

"""

import matplotlib.pyplot as plt
import numpy as np

# for title and title_fontsize
c = np.arange(1,11)
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(loc = 'upper center')
plt.grid()
plt.tick_params(labelsize = 20,labelcolor = 'y',direction = 'inout',width = 10,length = 10)
plt.tight_layout()
plt.show()


#Use only colors to change both label and ticks color

plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(loc = 'upper center')
plt.grid()
plt.tick_params(labelsize = 20,colors = 'g',width = 10,length = 10)
plt.tight_layout()
plt.show()

#Enable labelrigh and label top only
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(loc = 'upper center')
plt.grid()
plt.title("top and right labels only")
plt.tick_params(labelright = True,labeltop = True,labelleft = False,labelbottom= False,colors = 'c')
plt.tight_layout()
plt.show()


# gridProperties

plt.plot(c**2,label = "square",lw = 5)
plt.plot(c**3,label = "cube",lw = 5)
plt.legend(loc = 'upper center')
plt.grid()
plt.tick_params(grid_color = 'g',grid_linestyle = '--',grid_alpha = 0.5,grid_linewidth = 8)
plt.tight_layout()
plt.show()