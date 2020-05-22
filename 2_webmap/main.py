import folium
import pandas
import base64
from PIL import Image


def get_visited_color(visited):
    if visited:
        return "green"
    else:
        return "orange"


fmap = folium.Map(location=[38, 0], zoom_start=8, tiles="Stamen Terrain")

visited_group = folium.FeatureGroup(name="Visited Layer")
geo_json = open("world.json", "r", encoding="utf-8-sig").read()
visited_group.add_child(folium.GeoJson(data=geo_json,
                                   style_function=lambda x: {"fillColor": get_visited_color(x["properties"]["visited"])}))

fgi = folium.FeatureGroup(name="Image Markers")
im_data = pandas.read_json(open('image_data.json', 'r'))
for lat, lon, file in zip(im_data[:]['lat'], im_data[:]['lon'], im_data[:]['file']):
    encoded = base64.b64encode(open(file, 'rb').read())
    image_html = '<img src="data:image/jpeg;base64,{}">'.format
    width, height = Image.open(file).size
    iframe = folium.IFrame(image_html(encoded.decode('UTF-8')), width=width+20, height=height+20)
    popup = folium.Popup(iframe)
    icon = folium.Icon(color="red", icon="ok")
    marker = folium.Marker(location=[lat, lon], popup=popup, icon=icon)
    fgi.add_child(marker)

fmap.add_child(fgi)
fmap.add_child(visited_group)
fmap.add_child(folium.LayerControl())

fmap.save("map1.html")
