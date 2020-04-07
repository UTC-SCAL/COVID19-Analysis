import os
from  datetime import datetime
import pandas 
import arcgis.gis
from arcgis.features import FeatureLayer
from IPython.display import display
from arcgis.mapping import WebMap

# Log into ArcGIS Online
gis = arcgis.gis.GIS("home")

gis = arcgis.gis.GIS()


search_result = gis.content.search("title:Unacast County by County Grade for Social Distancing, owner:UOdocent", item_type = "Web Map")
display(search_result)

layer = search_result[0]

web_map_obj = WebMap(layer)

num=1
for lyr in web_map_obj.layers:
    print(num, "\n")
    print(lyr.title + " " + lyr.url)
    print(lyr.properties.capabilities)
    num = num+1

# print(my_content)

# layer = FeatureLayer(url = "https://disasterresponse.maps.arcgis.com/sharing/rest/content/items/ab72fb3e9bf24d9594f0b942718bffeb/info/metadata/metadata.xml?format=default&output=html")

# print(layer)

