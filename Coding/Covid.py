import os
from datetime import datetime
import pandas 
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection

##Login to GIS
gis = GIS()

##ID for the Unacast map 
id = "ab72fb3e9bf24d9594f0b942718bffeb"

##Gets the content listed at the given id 
test = gis.content.get(id)
unacast_layer = FeatureLayerCollection(test.url)

##Pulls the individual layer out of the collection
layer = unacast_layer.layers
layer = layer[0]

##Pulls the entire set of data within that layer
query_result1 = layer.query()

##Converts the query results into a dataframe. 
frame = query_result1.sdf
##Date format = 2020-04-06 15:32:29.533999919, so drop the millisec section.
frame[['last_updated']] = datetime.strptime((str(max(frame.last_updated)).split(".")[0]), "%Y-%m-%d %H:%M:%S")
print(frame.last_updated[0])
frame.to_csv("../Data/UnacastSocialDistancing.csv", index=False)