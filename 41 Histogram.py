import  matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

data = pd.read_csv("data for histogram.csv")
ages = data['Age']
bins = np.arange(10,101,10)

values, bins, pathces = plt.hist(ages,bins=bins,ec = 'k',log = True) # The figure is not very clear so we enable log scale
plt.xticks(bins)
plt.xlabel("Ages")
plt.ylabel("Frequency ")
plt.title("Frequency Distribution of Ages")

# To label the curve
for i in range(len(values)):
    plt.text(bins[i],values[i],values[i],bbox = {"color": 'red','fc':'k'},color = 'y')

plt.show()


"""In the above example the labels are added to the bins. Remember we have 10 bins but 10 
values unlike bar plot, where bins and values are equal. In case of histogram the 
 values are 1 less than the bins because here we are looking for ranges and not a unique value.
 
There is no proper way to add labels to histogram, so we used the text function to do this task.
 """

