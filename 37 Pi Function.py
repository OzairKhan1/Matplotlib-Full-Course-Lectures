"""                                 Pi Function

                                Syntax::
    plt.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)

Parameters:
1) data represents the array of data values to be plotted, the fractional area of each slice
is represented by data/sum(data). If sum(data)<1, then the data values returns the fractional
area directly, thus resulting pie will have empty wedge of size 1-sum(data).

2) labels is a list of sequence of strings which sets the label of each wedge.
3) colors:  attribute is used to provide color to the wedges.
4) autopct:  is a string used to label the wedge with their numerical value. Syntax: "%1.1f%%"
5) shadow:  is used to create shadow of wedge. It takes a bool Value. shadow = True enables it.
6) frame: is used to make a frame around the circular pie. frame takes a bool value.
7) startangle: it means that the first element will be plot from that position
8) wedgeprops: is a dict and is used for customization. like edgecolor, linewidth:


A Pie Chart is a circular statistical plot that can display only one series of data.
The area of the chart is the total percentage of the given data. Pie charts are commonly used
in business presentations like sales, operations, survey results, resources, etc. as they provide
a quick summary.

"""
from matplotlib import pyplot as plt
import numpy as np

# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']
explode = np.zeros(len(cars))
explode[1] = 0.2
explode[3] = 0.3

data = [23, 17, 35, 29, 12, 41]
color = ['k','g','lightblue','m','c','pink']

# Creating plot
# plt.figure(figsize=(10, 7))
plt.figure(figsize=(8,5))
plt.pie(data, labels=cars,autopct="%1.1f%%",colors=color,startangle=0)
plt.legend(loc = (1,1.1),title = 'Cars',title_fontsize = 20,borderpad = 1,labelspacing = 0.5)
plt.tight_layout()
plt.title("Pie Basic Customization. labels,colors, start Angle and Percentage shown above")
plt.show()

#Example 2: frame, shadow, explode
plt.figure(figsize=(10,6))
plt.pie(data, labels=cars,autopct="%1.1f%%",explode = explode,shadow=True,frame = True )
plt.title("Fram , Shadow and Explode",pad = 10)
plt.show()

#Example 3: wedgeprops: linewidth and linestyle, edgecolor
plt.pie(data,labels=cars,autopct="%1.1f%%",wedgeprops={'ec':'b','lw':6,'ls':'-'} )
plt.title("Wedge properties")
plt.show()





