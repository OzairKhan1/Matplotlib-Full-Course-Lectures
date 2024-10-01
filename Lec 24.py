"""                        Sine and Cosine Grap                    """

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0,10)  # The value are automatically in degrees
plt.plot(a,np.sin(a))
plt.plot(a,np.cos(a))
plt.show()

#for more smooth graph we can have

fondic = {"size":10,
          'color':'g',
          'style':'italic',
          'family':'monospace',
          'backgroundcolor': 'y',
          'weight':'bold'}
x = np.arange(0,361,90)
b = np.arange(0,361,30)
plt.plot(b,np.sin(b),label = 'sin(b)',lw = 2,ls = '--',marker = 'o',ms = 5,mfc = 'y',mec = 'k')
plt.plot(b,np.cos(b),label = ('cos(b)'),lw = 1,ls = ':',color = 'k')
plt.xlabel("Teta in Degrees",fontdict=fondic,labelpad = 10)
plt.ylabel("Range of sin and cos",fontdict=fondic)
plt.title("Plot of Sine and Cosine",fontdict=fondic,pad = 20)
plt.legend(loc = (1.1,1.1))
plt.grid(color = 'g',which = 'major',alpha = 0.2)
plt.xlim(0,360)
plt.ylim(-1,1)
plt.xticks(x,color = 'g',fontsize = 'xx-large')
plt.tick_params(axis = 'x',pad = 6,length = 10,width = 5,direction= 'inout',which = 'major',rotation = 30)
plt.tight_layout()
plt.show()



d = np.linspace(0,360,1000)
rad = np.deg2rad(d)
fondic = {"size":10,
          'color':'g',
          'style':'italic',
          'family':'monospace',
          'weight':'bold'}
plt.plot(d,np.sin(rad),label = 'sin(b)',lw = 2,ls = '--',marker = 'o',ms = 5,mfc = 'y',mec = 'k')
plt.plot(d,np.cos(rad),label = ('cos(b)'),lw = 1,ls = ':',color = 'k')
plt.xlabel("Teta in Degrees",fontdict=fondic,labelpad = 10)
plt.ylabel("Range of sin and cos",fontdict=fondic)
plt.title("Plot of Sine and Cosine",fontdict=fondic,pad = 20)
plt.legend(loc = (1.1,1.1))
plt.grid(color = 'g',which = 'major',alpha = 0.2)
plt.xlim(0,360)
plt.ylim(-1,1)
plt.xticks(x,color = 'g',fontsize = 'xx-large')
plt.tick_params(axis = 'x',pad = 6,length = 10,width = 5,direction= 'inout',which = 'major',rotation = 30)
plt.tight_layout()
plt.show()