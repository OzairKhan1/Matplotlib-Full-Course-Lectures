"""                                  Multiple Bar Graph

In multiple bar graph the bars are placed next to each other instead of placing them over top of
each other. The same example can be solved as used in stacked bar graph.


                                Help from Chat Gpt

Multiple bar graphs are useful in a variety of scenarios where you need to compare different sets
of data across categories. Here are some common use cases:

Comparing Different Groups: When you want to compare the performance or characteristics of
different groups over the same categories. For example, comparing the sales of different
products over severa months.

Tracking Changes Over Time: When you need to show how different groups change over time. For
instance, showing the annual revenue of multiple companies over several years.

Displaying Part-to-Whole Relationships: When you want to show how different parts contribute to
 a whole within categories. For example, displaying the percentage of market share held by different
  brands in various regions.

Highlighting Comparisons Across Multiple Categories: When you want to compare multiple categories
 side by side for better visual comparison. For instance, comparing the test scores of students in
  different subjects.

Segmented Data Analysis: When analyzing data that can be segmented by different dimensions, such
 as demographic information (age, gender) across various metrics (income, expenditure).

Example Scenarios
Educational Data: Comparing the test scores of students from different schools across various
subjects.
Financial Analysis: Comparing quarterly profits of different companies across multiple years.
Market Research: Comparing customer satisfaction ratings for different products across different
 age groups.
Healthcare: Comparing the incidence rates of different diseases across various regions and time
 periods.

"""

import matplotlib.pyplot as plt
import numpy as np


gold = [12,32,4,56,7,10]
silver = [20,30,25,40,15,0]
bronze = [25,45,15,30,50,0]
country = ['USA','UK','PAK','IND','CHINA','iran']

bar1 = np.arange(len(country))
w = 0.2
plt.bar(bar1,gold,width=w,label = "gold",color = 'orange')
bar2 = bar1 + w
plt.bar(bar2,silver,width=w,label = 'silver',color = 'm')
bar3 = bar2 + w
plt.bar(bar3,bronze,width=w,label = 'bronze',color = 'c')
plt.xlabel("Conntry")
plt.ylabel("Medals Earned")
plt.title("Simple Method 1")
plt.legend(loc = 'upper left')
plt.xticks(bar1+w,country)
plt.show()

#To solve the same example using loop
records = [gold,silver,bronze]
medals = ['gold',"silver",'bronze']
side = np.arange(len(country))
for i in range(len(records)):
    plt.bar(side,records[i],width=w,label = medals[i])
    side = side + w
plt.legend()
plt.xticks(bar1 + w, country)
plt.show()


"""                Using Chat Gpt to solve the problem more efficiently                  """

import matplotlib.pyplot as plt
import numpy as np

# Data
medals = {
    'gold': [12, 32, 4, 56, 7, 10],
    'silver': [20, 30, 25, 40, 15, 0],
    'bronze': [25, 45, 15, 30, 50, 0]
}
countries = ['USA', 'UK', 'PAK', 'IND', 'CHINA', 'iran']

bar_width = 0.2
bar_positions = np.arange(len(countries))  # array([0, 1, 2, 3, 4, 5])

# Plotting
for i, (medal, counts) in enumerate(medals.items()):
    plt.bar(bar_positions + i * bar_width, counts, width=bar_width, label=medal)

# Labels and Title
plt.xlabel("Country")
plt.ylabel("Medals Earned")
plt.title("Medals by Country")
plt.legend(loc='upper left')
plt.xticks(bar_positions + bar_width, countries)

# Display
plt.tight_layout()
plt.show()


"""                          More Advance bar graph using chat gpt                   """

import matplotlib.pyplot as plt
import numpy as np

# Data
medals = {
    'gold': [12, 32, 4, 56, 7, 10],
    'silver': [20, 30, 25, 40, 15, 20],
    'bronze': [25, 45, 15, 30, 50, 50]
}
colors = ['orange', 'm', 'c']
countries = ['USA', 'UK', 'PAK', 'IND', 'CHINA', 'Iran']

bar_width = 0.2
bar_positions = np.arange(len(countries))

# Plotting
for i, (medal, color) in enumerate(zip(medals.keys(), colors)):
    plt.bar(bar_positions + i * bar_width, medals[medal], width=bar_width, label=medal, color=color)

# Labels and Title
plt.xlabel("Country")
plt.ylabel("Medals Earned")
plt.title("Medals by Country")
plt.legend(loc='upper left')
plt.xticks(bar_positions + bar_width, countries)

# Display
plt.tight_layout()
plt.show()
