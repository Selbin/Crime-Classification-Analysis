
import pandas as pd
import json
import csvtogeojson as call
#creating a geojson file for heatmap
cols=['GEO_LON','GEO_LAT']
pot=pd.read_csv("murder.csv")
plot = call.df_to_geojson(pot,cols)
with open('murder.geojson','w') as out:
    json.dump(plot,out)