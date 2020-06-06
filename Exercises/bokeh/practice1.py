"""Making a basic bokeh line graph"""
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


df = pandas.read_csv(open("stock_data.csv", "r+b"), parse_dates=['Date'])
print(df)

output_file('line1.html')  # output file
f = figure(x_axis_type='datetime')  # figure object
f.title.text = "Closing Price"
f.xaxis.axis_label = 'Date'
f.yaxis.axis_label = 'Price ($)'
f.line(df['Date'], df['Close'], color='Orange')
f.segment(df['Date'], df['Low'], df['Date'], df['High'], color='Black', line_alpha=0.5)
show(f)
