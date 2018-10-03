import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[51.04, -114.062], zoom_start=4)

fg = folium.FeatureGroup(name="Base")

fg.add_child(folium.Marker(location=[51.04, -114.062], popup="Hi! this is snowing Calgary!", icon=folium.Icon(color='red')))
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=el, icon=folium.Icon(color='orange')))


map.add_child(fg)

map.save("webmap.html")