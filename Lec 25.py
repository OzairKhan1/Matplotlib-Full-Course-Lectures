"""                                Adding Text to Figure
Other than xlabel, ylabel and title

                Syntax:
            plt.text(x,y,s,fontdict,withdash,**kwargs)
1) x and y are the coordinate where we want to place the text
2) s is the string or text that we want to add
3) fontdict: is used to customize the text as we have seen in xlabel and title earlier
4) **kwargs do the same like customization

"""

import numpy as np
import matplotlib.pyplot as plt


fondic = {"size":10,
          'color':'k',
          'style':'italic',
          'family':'monospace',
          'backgroundcolor': 'y',
          'weight':'bold'}
a = np.arange(0,4)
plt.plot(a)  #I am ploting only y. so x will take the default value from 0 to 3
plt.text(2,2,'MYText',fontdict=fondic)
plt.show()


#exple2
a = np.arange(1,4)
plt.plot(a,marker = 'o')  #x is the default value from 0 to 3
plt.xlim(0)
plt.ylim(0)
plt.text(0,0,'MYText',fontdict=fondic)
plt.show()


"""  In the above example the text is not showing because (0,0) is not available.so to do this 
  we need to either use transform function or xlim and ylilm, shown above
   or The transform has shown below"""

a = np.arange(1,4)
plt.plot(a,marker = 'o')  #x is the default value from 0 to 3
current_axis = plt.gca()       # gca stands for get current axis
plt.text(0.5,.5,'MYText',fontdict=fondic,transform = current_axis.transAxes)
plt.show()

# Now Remember that after the trnasfom we have min (0,0) and max (1,1) for x and y axis