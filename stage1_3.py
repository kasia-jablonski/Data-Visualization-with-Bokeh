#import numpy as np
import pandas as pd

#from bokeh.charts import Bar
#from bokeh.plotting import hbar
from bokeh.plotting import ColumnDataSource, figure
from bokeh.io import output_file, show

output_file('pop-life.html')

file = 'country-pops.csv'

countries = pd.read_csv(file, nrows=5)
countries_array = np.array(countries.head)

#print(countries_array)
#bar_chart = hbar(countries, 'Country_English', values='Population', title='Population', legend=False)
#show(bar_chart)

country_data = ColumnDataSource(countries)

plot = figure(x_axis_label='Population', y_axis_label='Life Expectancy')

plot.circle(x='Population', y='Life_expectancy', source=country_data, size=15)
show(plot)