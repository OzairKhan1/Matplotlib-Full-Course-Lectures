"""                              Legend 8
******        Multiple legends in a single Figure      ******

Normally when we used multiple curve with plt.plot() plus labeling. after calling legen() function
we get a single legend with only one specified position. But what if we want multiple legends
in a figure with different position. We can do this using an extra function called

                        plt.gca().add_artist(ADD HERE):
We know that plt.legend() return an object. we need to store that value and add to the
above function will help creating more legends in a single figure.

Note: We will be using handles and labels for legend in this case

"""

import matplotlib.pyplot as plt
import numpy as np

c = np.array([1,2,3,4])
squar, = plt.plot(c**2)
cube, = plt.plot(c**3)
fourt, = plt.plot(c**4)
fifth, = plt.plot(c**5)
l3 = plt.legend([squar],['square'],loc = 'upper left')
plt.gca().add_artist(l3)
l1 = plt.legend([cube],['cube'],loc = 'center')
plt.gca().add_artist(l1)
plt.legend([fourt,fifth],['four','fifth'],loc = "upper center")
plt.title("Multiple Legends ",color = 'g',size = 20)
plt.show()

