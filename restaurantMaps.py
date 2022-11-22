import pandas as pd
import folium

df = pd.read_csv("Restaurants_Geo.csv", encoding='utf-8')

m = folium.Map(location=[52.52,13.40], tiles='OpenStreetMap', zoom_start=11)

for i, row in df.iterrows():
    lat = df.at[i,'lat']
    lng = df.at[i,'long']

    restaurant = df.at[i,'restaurant']
    popupText = (str(df.at[i,'restaurant']) + '<br>' + str(df.at[i,'street'])
                    + '<br>' + str(df.at[i,'zip']) + ' ' + str(df.at[i,'city']))

    if restaurant=='Subway':
        color='lightgreen'
    elif restaurant=='Starbucks':
        color='darkgreen'
    else:
        color='orange'

    folium.Marker(location=[lat, lng],popup=popupText, icon=folium.Icon(color=color)).add_to(m)

m.save("index.html")