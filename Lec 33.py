"""                            Histogram()

Syntax::        plt.hist(large number of arguments)
and will be discussed one by one.
1) x is the only compulsory argument, and is the data distribution values/data
2) bins: they could be an int, array or string. The default value is None and 10 will be taken
if bins are an int value. it means we will get that number of bars
if bins are array  the bars will be chosen and whould be len(lst) - 1.
e.g: lst = [1,11,21,31,41,51] will have 5 bars from 1-10, 11-20,21-30,31-40,41-50
if bins are sting: it takes the following values

a) auto     b) fd    c) rice     d) stone    e) sqrt    f) scoot   g) sturges   h)doane
the auto is the best option

3) range: range is used to determine the width of a bar. if not taken
then the range is calculated by taking the min and max value from the data x and divide by
number of bins for w of a single bar
***    When the bins is a sequence of an array then range doesn't work  ***

4) weight:: w should be the same array size as x
every element in x can be assing a same or different value
The number of element falls in the range of x. the corresponding w will be added.

5) Commulative: takes a bool value. If it is true it will take the count of a range
and plus the smaller value.
and if we take it -1 . the process will be reversed.
it means .   count + larger value


Histograms are widely used in various fields for visualizing and analyzing the distribution of data.
 Here are some main applications of histograms:

Understanding Data Distribution: Histograms provide a visual representation of how data is
distributed across different intervals or bins. This helps in understanding the central tendency
 (mean, median) and dispersion (spread) of the data.


Data Analysis and Exploration: Histograms are fundamental tools for exploratory data analysis (EDA).
They reveal patterns, trends, and outliers in datasets, aiding in identifying data characteristics
 that may influence further analysis or decision-making.

Frequency Analysis: Histograms show the frequency (or count) of data points falling within each bin. This is crucial for understanding the occurrence or prevalence of specific values or ranges within the dataset.

Statistical Inference: In statistics, histograms are used to assess assumptions about the
distribution of data, such as normality. They help determine if data conforms to expected patterns
and can guide the selection of appropriate statistical tests.

Quality Control and Process Improvement: Histograms are used in quality control processes to monitor
 and improve product or process quality. They help identify variations and deviations from expected
  standards, enabling corrective actions.

Image Processing: In image processing, histograms visualize the distribution of pixel intensities
 within an image. This is useful for tasks such as contrast enhancement, thresholding, and
  equalization to improve image quality or extract specific features.

Market Research and Business Analytics: In business and marketing analytics, histograms analyze
 customer demographics, purchase patterns, and market trends. They assist in segmenting customer
 profiles and optimizing marketing strategies based on data insights.

Education and Research: Histograms are used in educational settings to teach statistical concepts
 and in research to present data distributions in scientific studies across disciplines such as
 biology, economics, and social sciences.

Risk Management and Finance: In finance and risk management, histograms analyze financial data
distributions, market volatility, and risk factors. They inform decision-making processes related
to investments, portfolio management, and risk assessment.

Predictive Modeling and Machine Learning: Histograms are used in feature engineering and data
preprocessing for machine learning models. They help preprocess data by visualizing feature
 distributions and identifying skewness or outliers that may affect model performance.

"""


import matplotlib.pyplot as plt
import numpy as np

# x is the age of 100 different people b/w 0 and 100
x = [3, 22, 5, 87, 49, 63, 34, 46, 28, 80, 44, 13, 47, 69, 54, 51, 3, 35, 72,
     20, 31, 89, 26, 6, 54, 9, 72, 46, 23, 84, 7, 65, 40, 56, 97, 21, 40, 58, 11,
     82, 35, 73, 46, 22, 92, 27, 64, 39, 77, 8, 91, 99, 67, 14, 15, 60, 88, 24, 48,
     93, 6, 25, 49, 62, 23, 7, 41, 66, 87, 9, 25, 6, 10, 55, 30, 4, 81, 38, 74, 17,
     47, 79, 23, 59, 84, 3, 71, 12, 86, 83, 5, 98, 36, 89, 75, 87, 1, 94, 2, 100
]



# Example 1:
plt.hist(x = x,ec = 'k')
plt.title("Simplest Histogram")
plt.show()

#Example 2: bins gives the number of bars
plt.hist(x = x,bins = 5,ec = 'y',color = 'k',rwidth=0.5)
plt.title("bins as an int number")
plt.show()

#Example 3: bins as a list of range:: Equals width bins will be given

rnge = np.arange(0,101,10)
lst = [i+1 for i in rnge]
plt.hist(x = x,bins = lst,ec = 'k',color = 'lightgrey')
plt.title("bins as a sequence of  numbers")
plt.xticks(lst)
plt.yticks(np.arange(1,18))
plt.show()

#Exmpl 4: bins is a string value. it can take any one value mentioned above.
#auto is common used

plt.hist(x = x,bins = 'auto',ec = 'k',color = 'lightblue')
plt.title("bins as a String Value")
plt.show()

# Example 5: When range is given
plt.hist(x = x,bins = 10,range=(0,100),ec = 'k',color = 'lightgrey')
plt.title("Range as an Argument")
plt.show()

#Example 6: 2 value falls in range of 1-10, and the w =2 so we have 2 * 2 = 4, 2 * 4 = 8 for 20-30
x = [3,9,11,19,18,23,25,29,30]
w = [2] * len(x)
plt.hist(x = x,bins = 3, range=(0,30),ec = 'k',color = 'lightgrey',weights=w)
plt.title("Same weight is assign ")
plt.show()
# We can also assing different w to different ranges or even element in the same range
a = [4,11,3,23,14,29]
wd = [1,2,4,4,5,5]
plt.hist(x = a,bins = 3, range=(0,30),ec = 'k',color = 'grey',weights=wd)
plt.title("Different weight is assign ")
plt.text(0,12,"Range(1-10) has 2 values, and the w is 1 + 4.")
plt.text(0,11,"Range 20-30 has 2 values and the w is 4 + 5")
plt.ylim(0,14)
plt.show()

#Example 7:: Commulative = True
x = [3, 9, 11, 19, 18, 23, 25, 29, 30]
plt.hist(x, bins=3, range=(0, 30), edgecolor='k', color='grey', cumulative=True)
plt.title("Cummulative = True: it takes count + smaller value ")
plt.text(0,8,"count + smallest value from that count range")
plt.show()

# Now to make the cummulative = -1 the process will be reversed
x = [3, 9, 11, 19, 18, 23, 25, 29, 30]
plt.hist(x, bins=3, range=(0, 30), edgecolor='k', color='grey', cumulative=-1)
plt.title("Cummulative = -1: the process Reversed ")
plt.text(14,8,"count + largest value from that count range")
plt.show()
