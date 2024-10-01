"""                                      When to Use a Stack Plot

1) Cumulative Data: When you want to show how individual parts make up the whole over time.
2) Multiple Categories: When you have multiple categories that together form a total.
3) Trends Over Time: To visualize how each part changes over time in relation to the total.


"""

from matplotlib import pyplot as plt
import numpy as np

plt.style.use("ggplot")

# Example 1: with one set of data
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = np.array([1, 2, 3, 3, 4, 4, 4, 4, 5])
player2 = np.array([1, 1, 1, 1, 2, 2, 2, 3, 4])
player3 = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])
totalScore = np.sum([player3,player2,player1],axis=0)
labels = ['player1','player2','player3']
plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=['grey','lightblue','k'])
plt.bar(minutes,totalScore,alpha = 0.5,color = 'orange',zorder = 1)
plt.legend()
plt.yticks(np.arange(13))
plt.show()


# Example 2:: With another set of data
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=['g','lightblue','y'])
# plt.bar(minutes,)
# plt.legend()
# plt.show()





"""                            Example from Chat Gpt

import matplotlib.pyplot as plt
import numpy as np

# Example data
days = [1, 2, 3, 4, 5]

apples = [3, 2, 5, 3, 4]
bananas = [2, 3, 4, 2, 5]
cherries = [1, 4, 2, 3, 3]

# Stack plot
plt.stackplot(days, apples, bananas, cherries, labels=['Apples', 'Bananas', 'Cherries'],
 colors=['#FF9999', '#66B2FF', '#99FF99'])

plt.xlabel('Days')
plt.ylabel('Quantity')
plt.title('Fruit Consumption Over Time')
plt.legend(loc='upper left')

plt.show()

"""

