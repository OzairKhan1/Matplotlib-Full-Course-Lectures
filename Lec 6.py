"""                               Alpha  & Zorder
Both Alpha and Zorder are Keyword Argument
1) Alpha is used to adjust the transparency  of a graph.
******  The value for Alpha is b/w 0 and 1 and the default value is 1. ******

Note: As the value of Alpha is 1 the graph is at its full brightness/transparent
as the value of Alpha is close to Zero the brightness becomes dull and evern the color assign
to line with formatting will not be visible.

Remember: if the value of Alpha is 0 for a particular plot. that plot won't be visible at all

2)  Zorder. This keyword is used to change the order of a graph. It means which one will be at the
top of the other. The one with higher value will be at the front and the others will be at the back
and so on.

Example: for three plotting values . z = 3, z= 2, z= 1. the plot with z = 3 will be at the front
then z = 2 and finally the z = 1.

Normally the last graph will be at the top, but we can change it using zorder argument.
if z = same for all the graph. the one at the last will override others.
"""


import matplotlib.pyplot as plt
import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
b = np.array([0, 11, 12, 13, 17, 20, 26, 30, 40, 50, 70, 80, 90, 100])
c = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

plt.plot(a, "g-.", alpha=1, lw=10)  # Fully opaque
plt.plot(b, alpha=0.5, lw=10)       # 50% transparent
plt.plot(c, 'r-', alpha=0, lw=10)   # Invisible
plt.show()


plt.plot([0, 0], [-1, 1], "g-.", alpha=1, lw=10, zorder=1)  # Behind others
plt.plot([-1, 1], [-1, 1], "y", alpha=1, lw=10, zorder=3)   # On top
plt.plot([-1, 1], [1, -1], 'r-', alpha=1, lw=10, zorder=2)  # Middle
plt.show()

plt.show()

"""                                          Chat Gpt
Alpha
Purpose: Adjusts the transparency of a graph.
Range: The value ranges between 0 and 1.
Default Value: 1 (fully opaque).The graph can be easily seen 
Behavior:
Alpha = 1: Graph is fully opaque (full brightness ).
Alpha < 1: Graph becomes more transparent.
Alpha = 0: Graph becomes fully transparent (invisible).

Zorder
Purpose: Changes the order of graphs (which one appears on top of others).
Behavior:
Graphs with higher zorder values appear in front of those with lower values.
If zorder values are the same, the graph plotted last appears on top.




"""