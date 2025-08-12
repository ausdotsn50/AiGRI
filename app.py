# Minimal flask app from doc: https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask
import geopandas
from geodatasets import get_path
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    # File containing both data and geometry: GeoPackage, GeoJSON, Shapefile
    # Reader: geopandas.read_file() returns GeoDataFrame
    # gdf = geopandas.read_file("/shp_files/Regions.shp.shp")

    path_to_data = get_path("nybb")
    # gdf = geopandas.read_file(path_to_data)

    gdf = geopandas.read_file(path_to_data)[['BoroName', 'Shape_Area']] # select only specific columns

    # print(type(gdf))
    # print(gdf)

    gdf_json = gdf.to_json() # converts to JSON string
    gdf_dict = json.loads(gdf_json) # converts to python dict

    return [{k:v} for k,v in gdf_dict.items()]