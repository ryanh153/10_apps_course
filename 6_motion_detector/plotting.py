from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource

from motion_detector import df


df["Start_str"] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_str"] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")

print(df['Start'].dt)
print(type(df['Start'].dt))

cds = ColumnDataSource(df)

f = figure(x_axis_type='datetime', title='Motion Graph')
f.yaxis.minor_tick_line_color = None
f.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_str"), ("End", "@End_str")])
f.add_tools(hover)

quads = f.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)

output_file("Graph.html")
show(f)