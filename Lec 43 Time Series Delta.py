"""                         Ploting TimeDelta

1) Warning: if we use plt.plot_date() we get a warning or error. we should use plt.plot() instead
2) we need to beautify our axis.
We need to run the command on the Figure instead of plt.plot
                    For that we need to run this command
                                plt.gcf().autofmt_xdate()
it actullay rotates the labels and alignment properly

3) To change the formatting of our dates, we can use a matplotlib time imported as mpl_dates
the method of is:
        dt = mpl_dates.DateFormatter("%b %d, %y") . this is string from Python Documentation
        plt.gca().xaxis.set_major_formatter(dt)

"""


import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('bmh')
#
# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
#
# y = [0, 1, 3, 4, 6, 5, 7]

# plt.plot(dates,y,linewidth = 3)
# plt.gcf().autofmt_xdate()
#
# dt = mpl_dates.DateFormatter("%b %d, %y")
# plt.gca().xaxis.set_major_formatter(dt)
# plt.show()



"""                         To Plot the Real data of Bitcoin on daily basis                   """

data = pd.read_csv('data Time Delta.csv')

new_date = '2019-05-17'  # Replace with your desired date
new_close_value = 8059.129883

# Create a new row with specified values and NaN for others
new_row = {
    'Date': new_date,
    'Open': pd.NA,
    'High': pd.NA,
    'Low': pd.NA,
    'Close': new_close_value,
    'Adj Close': pd.NA,
    'Volume': pd.NA
}

# Convert the new row to a DataFrame
new_row_df = pd.DataFrame([new_row])

# Ensure no columns with only NA values in the new row DataFrame
new_row_df = new_row_df.loc[:, new_row_df.notna().any()]

# Append the new row to the DataFrame
updated_data = pd.concat([data, new_row_df], ignore_index=True)

''' The date was treated as a string so we first conveted them to dates using pd.to_datetim()'''
updated_data['Date'] = pd.to_datetime(updated_data['Date'])
updated_data.sort_values('Date',inplace = True)

priceDates = updated_data['Date']
priceClose = updated_data['Close']

plt.plot(priceDates,priceClose,lw = 3,marker = 'o',ms = 10,mfc = 'y')
plt.gcf().autofmt_xdate()
plt.show()


