import pandas as pd

from bokeh.plotting import ColumnDataSource, figure
from bokeh.io import output_file, show
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.layouts import column, row

output_file('pop-life.html')

file = 'country-pops.csv'

countries = pd.read_csv(file)

country_data = ColumnDataSource(countries)

color_mapper = CategoricalColorMapper(factors=['Asia', 'Africa', 'Antarctica', 'Australia', 'Central America','Europe', 'North America', 'Oceania', 'South America'], 
                                    palette=['#00FF00', '#FFD343', 'darkgray', 'brown', 'cyan', 'crimson', 'red',   '#0000FF', 'purple'])

TOOLTIPS = 'pan, wheel_zoom,box_zoom, reset, hover,save'

plot_life_expect = figure(x_axis_label='Population', y_axis_label='Life Expectancy', tools= TOOLTIPS, title= 'Population vs. Life Expectancy')

plot_birth_rate = figure(x_axis_label='Population', y_axis_label='Birth Rate', title='Population vs. Birth Rate',  tools=TOOLTIPS)

plot_death_rate = figure(x_axis_label='Population', y_axis_label='Death Rate', title='Population vs. Death Rate',  tools=TOOLTIPS)

plot_birth_rate.circle(x='Population', y='Birthrate', source=country_data, size=10, color=dict(field='Continent',     transform=color_mapper), legend='Continent')

plot_death_rate.triangle(x='Population', y='Deathrate', source=country_data, size=10, color=dict(field='Continent',     transform=color_mapper), legend='Continent')

plot_life_expect.diamond(x='Population', y='Life_expectancy', source=country_data, size=10, color=dict(field='Continent',     transform=color_mapper), legend='Continent')

hover = plot_life_expect.select_one(HoverTool)
hover_birth = plot_birth_rate.select_one(HoverTool)
hover_death = plot_death_rate.select_one(HoverTool)

hover.tooltips = [('Country Name English', '@Country_English'), ('Population', '@Population'), ('Life Expectancy (years)', '@Life_expectancy')]

hover_birth.tooltips = [('Country Name English', '@Country_English'), ('Population', '@Population'), ('Birth Rate', '@Birthrate')]

hover_death.tooltips = [('Country Name English', '@Country_English'), ('Population', '@Population'), ('Death Rate', '@Deathrate')]

plot_life_expect.legend.location = 'bottom_right'
plot_life_expect.legend.background_fill_color = 'lightgrey'

plot_birth_rate.legend.location = 'bottom_right'
plot_birth_rate.legend.background_fill_color = 'lightgrey'

plot_death_rate.legend.location = 'bottom_right'
plot_death_rate.legend.background_fill_color = 'lightgrey'

plot_birth_rate.x_range = plot_life_expect.x_range
plot_death_rate.x_range = plot_life_expect.x_range

show(row(column(plot_life_expect, plot_birth_rate), column(plot_death_rate)))