"""                                   Annotation
Syntax::                plt.annotation(s, xy,*args,**kwargs)

1) s : is the string or the text  that we want to add to the plot
2) xy is the point to annotate. or xy is the data coordinate where we want our text to be

*********          Both the above parameter are compulsory       *********

Another Syntax::     plt.annotate(s,xy,xytext,xycoord,textcoordinate,arrowprops,


***      Annotation is a note or comment to explain a certain point in a graph.
1) s : is the string or the text  that we want to add to the plot
2) xy is the point to annotate.
3) xytext is the point where the text will be placed.
Remember: if xytext is an optional and if not given the text will be placed on xy data coordinate
4) xycoord,textcoordinate are optional parameter
5) arrowprops is an empty dictionary that is used to plot a arrow b/w text and annotation point
6) annotation_clip: Takes a bool value. If the annotation point is outside the data coordinate
it will not show that text. But if we make this value of annotation_clip False. it will shown then


"""
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(1,4)
plt.plot(a,marker = 'o')
plt.annotate('Point',(1,2)) # Simple Example`
plt.title("Text & Data Coordinate Only",color = 'g')
plt.show()

#Example 2
a = np.arange(1,4)
plt.plot(a,marker = 'o')
plt.annotate('Point',(1,2),(1,2.5),color = 'r',size = 20) # The text is place at (1,2.5)
plt.title("Text,Data Coordinate and Text coordinate",color = 'b')
plt.show()


#Example 3
a = np.arange(1,4)
plt.plot(a,marker = 'o')
plt.annotate('Point',(1,2),(1,2.5),arrowprops={}) # Empty dict will draw a default arrow b/w text & point
plt.title("Text and arrow Annotating to the data coordinate",color = 'c')
plt.show()

#Expm 4
a = np.arange(1,4)
plt.plot(a,marker = 'o',lw=4,ls = '--',color = 'orange',mfc = 'k',ms = 9)
plt.annotate('Point',(1,2),(1,2.5),arrowprops={'arrowstyle':'<->'})
plt.title("Arrow Style <--->",color = 'red')
plt.show()

"""We can customize the arrow. Refere to documentation. 
Remember we can use the below attribute as a dict keys only if we don't use arrowstyle.
we cannot do both of them together
1) width
2) headwidth
3) headlength
4) shrink


"""
#Exp 5
a = np.arange(1,4)
plt.plot(a,marker = 'o',lw=4,ls = '--',color = 'orange',mfc = 'k',ms = 9)
plt.annotate('Point',(1,2),(1,2.5),arrowprops={'width':10,'headwidth':20,'headlength':30})
plt.title("Arrow Customization")
plt.show()


#Last Example is about annotation_clip.
""" if the data coordinate is outside the figure then the text will not be shown
The default value is None. but to show the text even if the coordinate is outside, we need
to change it to False
"""
a = np.arange(1,4)
plt.plot(a,marker = 'o',lw=4,ls = ':',color = 'g',mfc = 'k',ms = 10)
plt.annotate('Point',(1,3.4),annotation_clip=False)
plt.title("Annotation_clip is False.",size = 10,color = 'red')
plt.show()

#Remember when data coordinate is beyond the graph we can't use arrowprops with it.
#