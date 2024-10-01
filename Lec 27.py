"""                             Drawing box Around Text or Annotation

syntax:            plt.text(xy,s, bbox = {})  or plt.annotation(s,xy,bbox = {})

1) bbox is a dictionary. we can use **kwargs to customize it.

We can use "fc" for bg color of box and "ec" for edge color of bbox.
We can also use the 'bbox style' keyword argumnet to use style from below list

Various Styles are available for bbox
1) round
2) round4
3) roundtooth
4) sawtooth
5) square

and
6) Circle
7) darrow
8) larrow
9) rarrow







"""
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,4)
plt.plot(a)  #I am ploting only y. so x will take the default value from 0 to 3
plt.text(0.4,2,'By Text',bbox = {'fc':'red', 'boxstyle':'circle','pad':0.5})
plt.annotate("By Annotate",(1.4,2),bbox = {'fc':'y','ec':'k','boxstyle':'sawtooth','pad':0.9})
plt.show()

#Expl 2 with Arrow props
a = np.arange(0,4)
plt.plot(a)  #I am ploting only y. so x will take the default value from 0 to 3
plt.text(1.4,2,'By Text',bbox = {'fc':'red', 'boxstyle':'circle','pad':0.5})
plt.annotate("By Annotate",(2,2),(2,3),arrowprops={}, bbox= {'fc':'y','ec':'k','boxstyle':'sawtooth','pad':0.9})
plt.show()