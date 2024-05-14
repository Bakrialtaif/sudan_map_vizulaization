#Sudan State Map with Attribute Density Visualization (Python)
#Created by: Ahmed Fat'hAlalim (https://www.facebook.com/allooord/)
#Date Created: May 14, 2024
#Last Updated: May 14, 2024
#This Python code generates a choropleth map of Sudan, visualizing the density of a specific attribute across its states. Users can provide data about each state (ID, value) and a GeoJSON file containing Sudan's administrative boundaries.

#Functionality:
#Leverages the Folium library to create an interactive map.
#Uses a GeoJSON file to define the state boundaries.
#Assigns colors to states based on the provided attribute values.

#Requirements:
#Python 3 (tested with 3.x)
#Folium library (pip install folium)

#input:
#CSV/JSON file contains  data about each state (ID, value)
#output:Sudan State Map with Attribute Density Visualization as HTML file

import folium
import json
import pandas as pd
# initialize the map and store it in a m object
m = folium.Map(location=[33.877805391320727, 18.967476932741064], zoom_start=5)

# show the map
#m

geojson_file = 'sdadmbndaadm1.geojson'
states ='SD.csv' 
state_geo = json.load(open(geojson_file))
state_data = pd.read_csv(states)
#print(state_data.head())

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "value"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Numer Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)
m.save('sudan_kidney_density.html')
m