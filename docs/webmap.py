import folium
import pandas

data = pandas.read_csv("ca_updated.csv")
lat = list(data["lat"])
lon = list(data["lng"])
name = list(data["city"])
pop = list(data["population"])

def color_generator(ppl):
    if ppl < 150000:
        return 'green'
    elif 150000 <= ppl < 750000:
        return 'orange'
    else:
        return 'red'
    return

map = folium.Map(location=[51.04, -114.062], zoom_start=3)

fgp = folium.FeatureGroup(name="Top 20 Canadian Cities by Population")

for lt, ln, pp, nm in zip(lat, lon, pop, name):
    fgp.add_child(folium.CircleMarker(location=[lt,ln], popup=nm, color='grey', radius=3, fill_color=color_generator(pp), fill_opacity=1))

fgw = folium.FeatureGroup(name="World Layer")
fgw.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))




map.add_child(fgp)
map.add_child(fgw)
map.add_child(folium.LayerControl())
map.save("webmap.html")