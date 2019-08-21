from shapely.geometry import Polygon
import requests
import geopandas as gpd
from geopandas import GeoSeries
import config
import pandas as pd 


name = "hereapi"
ID = config.here_api_key
CODE = config.here_api_code

head = 'https://isoline.route.cit.api.here.com/routing/7.2/calculateisoline.json?'
URL_Base = '{}app_id={}&app_code={}&mode=fastest;{};traffic:{}&start=geo!{},{}&range={}&rangetype={}'
URL_Base_dep = '{}app_id={}&app_code={}&mode=fastest;{};traffic:{}&departure={}&start=geo!{},{}&range={}&rangetype={}'

def get_isodata(location, type_iso = 'time', range_iso = 3600, travel_mode = 'car', traffic='disabled', departure=None): #receives a single location
    """ Function uses Here API to generate isolines depending on input parameters
    
    Parameters:
    location - Tuple of coordinates (lat, long)
    type_iso - Type of isoline, distance or time based, defaults to time
    range_iso - Range of the isoline depending on type_iso (in seconds), defaults to 1 hour
    travel_mode - Type of transit, can be truck, car or pedestrian
    traffic - toggles enabled or disabled
    departure - Departure time in format YYYY-MM-DDTHH:MM:SS (can include timezone)
    """
    
    if departure == None:
        url = URL_Base.format(head, ID, CODE, travel_mode, traffic, location[0], location[1], range_iso, type_iso) 
    else: 
        url = URL_Base_dep.format(head, ID, CODE, travel_mode, traffic, departure, location[0], location[1], range_iso, type_iso)
    try: 
        js = requests.get(url).json()['response']
        iso = js['isoline']
        coords = Polygon([(float(x.split(',')[1]), float(x.split(',')[0])) for x in iso[0]['component'][0]['shape']])
        geojs = gpd.GeoSeries([coords])
        geojs.crs = {'init' : 'epsg:4326'}
        return geojs
    except KeyError:
        js = requests.get(url).json()
        print(js)
        raise ValueError("HereAPI doesn't have data requested")
    except IndexError:
        print(js)
        raise ValueError("HereAPI doesn't have quality data")