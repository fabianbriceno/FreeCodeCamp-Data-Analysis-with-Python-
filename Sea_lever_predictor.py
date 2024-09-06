import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data from the CSV file
data = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot using 'Year' as the x-axis and 'CSIRO Adjusted Sea Level' as the y-axis
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data')

# Calculate the line of best fit for all data
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
sea_level_pred = intercept + slope * years_extended
plt.plot(years_extended, sea_level_pred, 'r', label='Best Fit Line (1880-2050)')

# Filter data from the year 2000 to the most recent year
recent_data = data[data['Year'] >= 2000]

# Calculate the line of best fit for data since 2000
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
recent_years_extended = pd.Series(range(2000, 2051))
recent_sea_level_pred = intercept_recent + slope_recent * recent_years_extended
plt.plot(recent_years_extended, recent_sea_level_pred, 'g', label='Best Fit Line (2000-2050)')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save the plot
plt.savefig('sea_level_plot.png')

# Show the plot
plt.show()
