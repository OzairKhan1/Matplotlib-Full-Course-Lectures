"""                       Fill between

                            Syntax
    plt.fill_between(x, y1, y2=0, where=None, interpolate=False, step=None, *, data=None, **kwargs)

1) x : is the x-axis
2) y1: is the first curve that you have drawn like a line graph
3) y2: it is 0 by default. so the Area b/w the curve and the x - axis will be filled with the color




"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data Language DevData.csv")
Age = data['Age']
All_Devs = data['All_Devs']
Pyton = data['Python']
Js = data['JavaScript']
overall_median = 57287

# plotting simple line

plt.plot(Age,All_Devs,linewidth = 5,color = 'k')
plt.fill_between(Age,All_Devs,color = 'lightgreen')
plt.title("The Area b/w x-axis and first Curve is Filled")
plt.show()

# Example 2: Plot the second Curve and fill the area b/w two curves
plt.plot(Age,All_Devs,linewidth = 5,color = 'k',label = 'All_Devs')            # First Curve
plt.plot(Age,Pyton,linewidth = 3,color = 'orange',ls = '-',label = 'Python')  # Second Curve
plt.fill_between(Age,Pyton,overall_median,color = "grey")
plt.title("Area b/w Overall Median and Python is Filled But with one color")
plt.legend()
plt.show()

# WE can do the coloring on the basis of certain condtion
# like python < over with red color and other with lighgreen color

plt.plot(Age,All_Devs,linewidth = 5,color = 'k',label = 'All_Devs')            # First Curve
plt.plot(Age,Pyton,linewidth = 3,color = 'b',ls = '-',label = 'Python')  # Second Curve
plt.fill_between(Age,Pyton,overall_median,where= (Pyton > overall_median),interpolate=True, color = "lightgreen",label = "Python above Overall Median")
plt.fill_between(Age,Pyton,overall_median,where= (Pyton < overall_median), color = "red",label = "Pyton below Overall Median")
plt.title("Area b/w Overall Median and Python is Filled But with different color")
plt.legend()
plt.show()

"""Remember with one conditional only one part where the condition is true will be shown
To show more such parts we need to use multiple full_between() with different condition as
shown in the above example. But the below example will show the fill_between() b/w two curves
and not b/w curve and a fix value as shown above. """

plt.plot(Age,Js,linewidth = 5,color = 'k',label = 'Js')            # First Curve
plt.plot(Age,Pyton,linewidth = 3,color = 'b',ls = '-',label = 'Python')  # Second Curve
plt.fill_between(Age,Pyton,Js,where= (Pyton > Js),interpolate=True, color = "lightgreen",label = 'Python Above Js')
plt.fill_between(Age,Pyton,Js,where= (Pyton < Js), color = "red",label = "Python below Js")
plt.title("Fill Between two Curves on the basis of condition")
plt.legend()
plt.show()