"""                                      Stacked Histogram

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100,3)
print(x)
plt.hist(x,bins = 'auto',ec ='k', range=(min(x.flatten()),max(x.flatten())),stacked=True)
plt.show()


"""------------------------------------------------------------------------------------
This below example is not the example of histgram but the example of stacked bar chart. 
from Chat Gpt

"""
import matplotlib.pyplot as plt
import numpy as np

# Generate a 100x3 array of random values from a standard normal distribution
x = np.random.randn(100, 3)
print(x)

# Define the range for the histogram
hist_range = (x.min(), x.max())

# Calculate the histograms and bin edges for each column separately
hist1, bins = np.histogram(x[:, 0], bins='auto', range=hist_range)
hist2, _ = np.histogram(x[:, 1], bins=bins, range=hist_range)
hist3, _ = np.histogram(x[:, 2], bins=bins, range=hist_range)

print("bins are ", bins)
# Define the bin centers for plotting
bin_centers = (bins[:-1] + bins[1:]) / 2

# Plot the stacked histograms
plt.bar(bin_centers, hist1, width=np.diff(bins), edgecolor='k', label='Column 1')
plt.bar(bin_centers, hist2, width=np.diff(bins), bottom=hist1, edgecolor='k', label='Column 2')
plt.bar(bin_centers, hist3, width=np.diff(bins), bottom=hist1+hist2, edgecolor='k', label='Column 3')

# Add labels, title, and legend for better understanding
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Random Values for Each Column')
plt.legend()

# Display the plot
plt.show()
"""-----------------------------------------------------------------------------------------
The below example is the example of hist(stacked = True) is stacked historam.
in the data we have 100 rows and 3 columns. Each column is plot with the help of a different color


"""


import matplotlib.pyplot as plt
import numpy as np

# Generate a 100x3 array of random values from a standard normal distribution
x = np.random.randn(100, 3)
print(x)

# Plot the stacked histograms
plt.hist(x, bins='auto', edgecolor='k', stacked=True)

# Add labels, title, and legend for better understanding
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram of Random Values for Each Column')
plt.legend(['Column 1', 'Column 2', 'Column 3'])

# Display the plot
plt.show()
