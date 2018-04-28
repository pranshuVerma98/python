import pandas
import folium

def co(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


df=pandas.read_csv("voca.txt")
lat=list(df["LAT"])
lan=list(df["LON"])
pop=list(df["ELEV"])
map=folium.Map(location=[26, 80],zoom_start=10,tiles="Mapbox Bright")
fgv= folium.FeatureGroup(name="My Map")
fgp= folium.FeatureGroup(name="Population")

for lt,lg,el in zip(lat,lan,pop):
			fgv.add_child(folium.CircleMarker(location=[lt,lg],radius=6,popup=str(el)+"m",color="yellow",fill=True,fill_color=co(el),fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))	
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
