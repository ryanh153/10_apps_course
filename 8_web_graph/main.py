from pandas_datareader import data
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN


def up_down(close_price, open_price):
    if close_price > open_price:
        return 'Increase'
    else:
        return 'Decrease'


start = datetime(2018, 1, 1)
end = datetime(2019, 1, 1)
df = data.DataReader(name="VTI", data_source="yahoo", start=start, end=end)

hours_12 = 12*60*60*1000
df["Status"] = [up_down(c, o) for c, o in zip(df.Close, df.Open)]
df['Middle'] = [(c+o)/2.0 for c, o in zip(df.Close, df.Open)]
df["Height"] = [abs(c-o) for c, o in zip(df.Close, df.Open)]
up = df.index[df.Status == 'Increase']  # indices of gray quads
down = df.index[df.Status == 'Decrease']  # indices of red quads

p = figure(x_axis_type='datetime', height=400, sizing_mode='stretch_width')
p.title.text = 'Candlestick Chart'
p.grid.grid_line_alpha = 0.3

p.segment(df.index, df.High, df.index, df.Low, color='black')

p.rect(up, df.Middle[up], hours_12, df.Height[up], fill_color="#00FF7F", line_color='black')
p.rect(down, df.Middle[down], hours_12, df.Height[down], fill_color="#FFA07A", line_color='black')

output_file("CS.html")
show(p)

# script1, div1 = components(p)
# cdn_js = CDN.js_files
# cdn_css = CDN.css_files
