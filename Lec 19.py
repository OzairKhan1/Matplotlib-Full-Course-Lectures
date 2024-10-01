"""                                            Legend 7
                &&&  All are Keyword Arguments &&&

1) Title Customization  of Legend: default argument is None
we can use title keyword to title the legend. We can aslo use title_fontsize to change size

2) borderpad: this can be  used to increase border spacing b/w (marker + label) and border

3) labelspacing: this can be used to increse the spacing b/w different labels

"""

import matplotlib.pyplot as plt
import numpy as np

# for title and title_fontsize
c = np.array([1,2,3,4])
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(title = "My legend",title_fontsize = 20)
# the label is first and then the marker once the markerfirst is False
plt.title("Legend Title Customization")
plt.show()


#Exmple 2: borderpad
c = np.array([1,2,3,4])
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(title = "My legend",title_fontsize = 20,borderpad = 5)
# the label is first and then the marker once the markerfirst is False
plt.title("Legend Borderpad")
plt.show()


#Legend labelspacing
c = np.array([1,2,3,4])
plt.plot(c**2,label = "square")
plt.plot(c**3,label = "cube")
plt.legend(title = "My legend",title_fontsize = 20,labelspacing = 4)
# the label is first and then the marker once the markerfirst is False
plt.title("Legend labelspacing")
plt.show()
