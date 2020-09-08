import folium
import webbrowser
# from parser import origin, destination
from parser import api_get

coordinates_list = api_get()

# coordinates_list = coordinates_list[0]
print(coordinates_list)

map = folium.Map(location=[coordinates_list[0][0], coordinates_list[0][1]], zoom_start=8)

colors = ['red', 'blue']

for coordinates in coordinates_list:
    c = colors[coordinates_list.index(coordinates)]
    folium.Marker(location=coordinates, icon=folium.Icon(color=c)).add_to(map)

map.save("map1.html")
webbrowser.open('file://' + '/home/plvc73/PycharmProjects/aod4/venv/map1.html')
