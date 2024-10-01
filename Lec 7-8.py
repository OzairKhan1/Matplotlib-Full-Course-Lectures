"""                        xlabel      &       ylabel
The Syntax for both xlabel and ylabel are same.

             plt.xlabel("Name to Graph",fontdict,labelpad,**kwargs)

fontdict: is a dictionary that is used to customize the the font family ,style,color, size and more
labelpad: use to move the text below or above the x-axis. +ve value moves the text below & viceversa
**kwargs: use to customize font. Instead of "fontdict" we can use this argument to do the same.
like chaning size,color,family,style e.t.c.

Remember:Whenever there is a conflict arises b/w fontdict and **kwargs. the later has high preference

"""

import matplotlib.pyplot as plt
import  numpy as np

a = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

plt.plot(a,antialiased = True, marker = "d",ms = 10,mfc = 'y',mec = 'k',ls = '--',lw = 10,alpha = 0.9)
plt.xlabel("x_axis Customization",{'size':20,'color':'yellow','family':'monospace','weight':'bold','style':'italic'},labelpad=-250,backgroundcolor = 'black')
plt.show()


# Define the font properties in a dictionary
font = {
    'size': 20,
    'color': 'green',
    'family': 'fantasy',
    'weight': 'bold',
    'style': 'oblique'
}

fontNew = {
    'size': 1,
    'color': 'yellow',
    'family': 'monospace',
    'weight': 10,
    'style': 'italic',
    'backgroundcolor': 'black'
}



# Create a plot
plt.plot([1, 2, 3], [4, 5, 6],ls = '-',lw = 9,color = 'c')

# Set the x-axis label with the custom font properties
# The backgroundcolor in the fontdict is not working, so we have to give it as a **kwargs.

plt.xlabel("x_axis Customization", fontdict=font,labelpad=3,backgroundcolor = 'black')
plt.ylabel("y_axis Customization", fontdict=font,labelpad=4,color = 'red',backgroundcolor = 'cyan')

""" Note::   Although the color mentioned in fontdict is green.but for y-axis it will be 
replaced by red due to high precedence of keyword Argument."""
# Show the plot
plt.show()
