import geopandas as gpd
from geopandas import GeoSeries
import folium



#Plotting function

def iso_function(features):
    return {'fillOpacity': 0.1, 'weight': 3, 'fillColor': 'blue'}

def iso_function_shp(features):
    return {'fillOpacity': 0.2, 'weight': 3, 'color' : 'red', 'fillColor': 'red'}


def isoplot(center, locations=None, shp=None, outputfile = 'out.html'):
    """ Function creates a plot of the isoline on top of a map
    
    Parameters:
    center - Center for the map to be created (lat, long)
    locations - Geoseries/Geodataframe of isoline/isolines
    shp - Geoseries/Geodataframe of a city shapefile to overlay on top of the isolines
    outputfile - Output location in .html extension
    """
    fm = folium.Map(location = center, zoom_start=8, tiles='CartoDBPositron')
    if not locations is none:
        geojson = locations.__geo_interface__
        folium.GeoJson(geojson, style_function = iso_function).add_to(fm)
    if not shp is None:
        geojson = shp.__geo_interface__
        folium.GeoJson(geojson, style_function = iso_function_shp).add_to(fm)
    fm.save(outputfile)
    print('map saved to %s' %outputfile)