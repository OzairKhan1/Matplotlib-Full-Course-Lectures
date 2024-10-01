"""                 Histotram 2
Here we will discussed the rest of parameter in the histogram function of pyplot

6) bottom : it is used to select one or more bottom for historgram

7) histtype: it could be one of the following:
    a) bar          b) barstacked               c) step         d) stepfilled

8) align: align is used to set alignment: default is left. preferable is left in the histogram
we have left, mid, and right as an alignment

9) rwidth: is used to change the width of the bins

10) log = False: by default. we use this argument when we have high value on the y-axis.
Remember when some of the value of y-axis is small and some are very large. then after plotting
the smaller values are not shown and apparently behaves like Zero value. To avoid this problem
we use the 'log' parameter to solve this Issue.

11) color: is use to change the color of bins: we can use fc -> facecolor: shown in all examples


12) label: is used in case of legend()

13) stacked: is used when we are plotting more than one data:
stacked = True  or we can use "histype" = barstacked to plot multiple data in stacked form.

                                Remember::
The hist function returns 3 things once we print it. out of 3 two are arrays and the third
is list of 3 objects if bins are 3. for more bins we will get more patches. patches = list[len(bins)]

                     called patches
1) the first array is bins: how many of them do we have
2) The second array is the edges
3) the third is list of 3 patch objects

"""
import matplotlib.pyplot as plt
import numpy as np

x = [3,9,11,19,18,23,25,29,30]
plt.hist(x = x,bins = 'auto', bottom = [5],ec = 'k',fc = 'pink') # the figure starts from 5
plt.title("Starts from a new BOTTOM like 5 in the figure")
plt.show()
# We can choose different bottom for different bins
bot = [3,5,7]
plt.hist(x = x,bins =3, bottom = bot,ec = 'k',fc = 'pink') # the figure starts from 5
plt.title("Different Bottom")
plt.show()

#histtype:  coule be bar, barstacked, step or stepfilled
plt.hist(x = x,bins = 'auto',ec = 'k',fc = 'grey', histtype='step',ls = ':',lw = 5) # the figure starts from 5
plt.title("step bar ")
plt.show()

plt.hist(x = x,bins = 'auto',ec = 'k',fc = 'red',histtype='stepfilled',lw = 5) # the figure starts from 5
plt.title("step filled")  # if bins are array it doesn't work at all
plt.show()

# Changing alignment from center to edge or edge to center. In new python default is edge
plt.hist(x = x,bins = 'auto',ec = 'k',fc = 'pink', align='mid') # the figure starts from 5
plt.title("alginment is mid: default is left ")
plt.show()

# Orientation: We have Vertical and Horizontal: Default is Vertical
plt.hist(x = x,bins = 'fd',ec = 'k',fc = 'pink',orientation= 'horizontal' ) # the figure starts from 5
plt.title("Orientation is Horizontal: default is vertical ")
plt.show()

# rwidth: is use to change the width of the bin
plt.hist(x = x,bins = 'auto',ec = 'k',fc = 'pink',rwidth=0.4) # the figure starts from 5
plt.title("Changing the width of the bins ")
plt.show()

#
