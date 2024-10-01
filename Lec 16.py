"""                                        Legend  4
Placing legend outside the box using 'loc'

We can simply provide  tuple of x and y coordinate. We know that the max value of x and y coordinate
is 1, and the min value of x and y coordinate is 0
so (1,1) will be the top right corner of Figure.

Remember:: The coordinate that we provide is always the lower left coordinate of the Legend
"""

import matplotlib.pyplot as plt
import numpy as np

c = np.array([1,2,3,4])
a = c**2
b = c**3
plt.plot(c,a,label = 'square')
plt.plot(c,b,label = 'cube')
plt.xlim(0,4)
plt.ylim(0,75)
plt.legend(loc = (1,1)) # Here we can't see the legend properly. We need to include 1 more function
# and that function is plt.tight_layout()
plt.tight_layout()
plt.title("Legend at (1,1)")
plt.grid()
plt.show()

#Example 2: Placing at (0.5,1)
c = np.array([1,2,3,4])
a = c**2
b = c**3
plt.plot(c,a,label = 'square')
plt.plot(c,b,label = 'cube')
plt.xlim(0,4)
plt.ylim(0,75)
plt.legend(loc = (0.5,1)) # Here we can't see the legend properly. We need to include 1 more function
# and that function is plt.tight_layout()
plt.tight_layout()
plt.title("Legend at (0.5,1)",loc = 'left',pad = 10,color = 'red',weight = 'bold',size = 20)
plt.grid()
plt.show()

#Example 3:: To place legend completely outside. either x or y should be greater than 1

c = np.array([1,2,3,4])
a = c**2
b = c**3
plt.plot(c,a,label = 'square')
plt.plot(c,b,label = 'cube')
plt.xlim(0,4)
plt.ylim(0,75)
plt.legend(loc = (1.1,1)) # Here we can't see the legend properly. We need to include 1 more function
# and that function is plt.tight_layout()
plt.tight_layout()
plt.title("Legend at (1.1,1)")
plt.grid()
plt.show()

# Example 4
c = np.array([1,2,3,4])
a = c**2
b = c**3
plt.plot(c,a,label = 'square')
plt.plot(c,b,label = 'cube')
plt.xlim(0,4)
plt.ylim(0,75)
plt.legend(loc = (1.1,0.5)) # Here we can't see the legend properly. We need to include 1 more function
# and that function is plt.tight_layout()
plt.tight_layout()
plt.title("Legend at (1,0.5)")
plt.grid()
plt.show()