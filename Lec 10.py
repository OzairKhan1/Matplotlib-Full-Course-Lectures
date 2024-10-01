"""                                         plt.show()
This function has a default value of block = False;
This means if the value of block = False. The program will not execute further until the current
window of graph is closed.
once the figure window is closed the program will proceed further.

For Example. if we write     "Hello World!" after    plt.show()   it will not be executed until
the figure window is closed.

so if we want to change this behaviour we need to change the vlaue of block = True in the show()

"""

import matplotlib.pyplot as plt

plt.plot([5,10,15,20],lw = 7)
plt.show()
print("Hello World!")


plt.plot([5,10,15,20],lw = 7)
plt.show(block = True)
print("Hello World!")