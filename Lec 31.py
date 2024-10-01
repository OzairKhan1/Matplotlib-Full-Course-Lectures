"""                                Stacked bar graph
    this is used to represent different groups on top of each other
"""

# Example 1:
import matplotlib.pyplot as plt
import numpy as np


gold = [12,32,4,56,7]
silver = [20,30,25,40,15]
bronze = [25,45,15,30,50]
country = ['USA','UK','PAK','IND','CHINA']
w = 0.5
bot = np.add(gold , silver)
plt.bar(country,gold,width=w,bottom=0,label = "gold")
plt.bar(country,silver,width=w,bottom=gold,label = "silver")
plt.bar(country,bronze,width=w,bottom=bot, label = "bronze")
plt.xlabel("Conntry")
plt.ylabel("Medals Earned")
plt.title("Simple Method 1")
plt.legend()
plt.yticks(np.arange(0,100,10))
plt.tight_layout()
plt.show()

#Same example with loop
gold = [12,32,4,56,7]
silver = [20,30,25,40,15]
bronze = [25,45,15,30,50]
medals = ['gold',"silver",'bronze']
country = ['USA','UK','PAK','IND','CHINA']
w = 0.5
record = [gold,silver,bronze]
bottom = [0] * len(gold)
for idx in range(len(medals)):
    plt.bar(country,record[idx],width=w,bottom = bottom,label = medals[idx])
    bottom = np.add(bottom,np.array(record[idx]))
plt.legend()
plt.title("Simple Method 2. Using Loop & indexes as labels",color = 'g')
plt.show()




#Example2

data = [
    [5, 25, 35],  # Values for category A
    [15, 15, 25],  # Values for category B
    [20, 20, 30],  # Values for category C
    [10, 15, 10]   # Values for category D
]
A,B,C,D = data
print(list(zip(A,B,C,D)))  #Refers to zip function explained in the same playlist by OK

#We can use Another way to transpose it by using *data within the zip fucntion b/c of list of lists
print(list(zip(*data)))

""" The Above is a bg for Stacked bar graph. we can use the above typle of example.

Stacked bar graph is used to represent
"""



categories = ['A', 'B', 'C', 'D']
subcategories = ['Sub1', 'Sub2', 'Sub3']
w = 0.5
newdata = list(zip(*data))
bottom = [0] * len(categories)
bottom = np.array(bottom)
for i, subcategories in enumerate(subcategories):
    print("subcate is ",subcategories)
    plt.bar(categories,newdata[i],width = w,label = subcategories, bottom = bottom)
    bottom = np.add( bottom ,np.array(newdata[i]))
plt.legend()
plt.title("Simple Method 3. Using Enumerate for labels",color = 'r')
plt.show()
