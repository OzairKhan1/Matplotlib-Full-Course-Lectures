"""                How to change the COLOR of Individual bin in hist function


The hist function returns 3 things once we print it. out of 3 two are arrays and the third
is list of 3 objects. called patches
1) the first array is bins: how many of them do we have
2) The second array is the edges
3) the third is list of 3 patch objects

"""

import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.rand(50) * 100
color = ['r','c','y','m','k','b','g','pink','grey','orange']
bins, edges, patches = plt.hist(x = x,bins = 10,ec = 'k',range=(0,100))
patches[0].set_fc('r')
patches[0].set_linewidth(4)
patches[1].set_facecolor('pink')
patches[2].set_linestyle("--")
patches[9].set_facecolor('y')
patches[5].set_facecolor('k')
print(bins)
print(edges)
plt.xticks(np.arange(0,101,10))
plt.title("Bins with colors assign Manually using Patch object")
plt.show()

# The above examples is to change the colors individually.
# We can use the patch object have n items in the list. the n depends the number of bins

bins, edges, patches = plt.hist(x = x,bins = 10,ec = 'k',range=(0,100))

for item in range(len(bins)):
    clr = color[item]
    patches[item].set_fc(clr)
    patches[item].set_linewidth(item)
plt.title("Bins with Unique colour picked from Colors")
plt.show()

# In the above example the last element has a width of 9:

# from the above list random colors can be picked using random module
linestyle = ['-','--',':','-.']
bins, edges, patches = plt.hist(x = x,bins = 10,ec = 'k',range=(0,100))
for item in range(len(bins)):
    clr = random.choice(color) # Repetation may be possible
    patches[item].set_fc(clr)
    patches[item].set_linewidth(random.randint(1,5)) # random linewidth b/w 2 - 50
    patches[item].set_linestyle(random.choice(linestyle)) # random line syle from linestyle
plt.title("Bins with randoms colours,linesyle and linewidth picked")
plt.show()