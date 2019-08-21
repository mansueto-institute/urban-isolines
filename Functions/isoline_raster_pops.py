from rasterstats import zonal_stats
import get_isodata
import geoseries_area

def isoline_raster_pops(center, city_shp):
    """
    Matches isolines with population raster data. Runs for 10 minute intervals for upto 1.5 hours
    Parameters:
    center = City coordinates in format lat, long
    city_shp = Raster data file 
    """
    count = 0
    times = []
    marginal_pops = []
    cumu_pops = []
    marginal_areas = []
    cumulative_areas = []
    for time in range(600, 7800, 600):
        isoline = get_isodata(center, range_iso = time, traffic = 'enabled', departure = '2019-02-13T18:00:00')
        if count == 0:
            isoline_gdf = gpd.GeoDataFrame(geometry = isoline)
            isoline.crs = {'init':'epsg:4326'}
        else:
            isoline_gdf = gpd.GeoDataFrame(geometry = isoline.difference(prev_isoline))
            isoline_gdf.crs = {'init':'epsg:4326'}
        iso_stats = zonal_stats(isoline_gdf, city_shp, stats= ['count', 'sum'])
        iso_pop = iso_stats[0]['sum']
        marginal_pops.append(int(iso_pop))
        area = geoseries_area(isoline)
        marginal_areas.append(area)
        if count == 0:
            prev_isoline = gpd.GeoDataFrame(geometry = isoline)
            prev_isoline.crs = {'init' : 'epsg:4326'}
        else :
            prev_isoline = gpd.GeoDataFrame(geometry = prev_isoline.union(isoline))
            prev_isoline.crs = {'init' : 'epsg:4326'}
        times.append(time/60)
        count += 1
    optima = []
    cumu_pop = 0
    cumu_area = 0
    for index, num in enumerate(marginal_pops):
        try:
            if num > marginal_pops[index+1] and num > marginal_pops[index-1]:
                optima.append(1)
            else:
                optima.append(0)
        except IndexError:
            optima.append(0)
        cumu_pop += num
        cumu_pops.append(cumu_pop)
        cumu_area += marginal_areas[index]
        cumulative_areas.append(cumu_area)
    return_dict = {'Times' : times, 
                   'Marginal_Areas' : marginal_areas, 
                   'Cumulative_Areas' :cumulative_areas,
                   'Marginal_Population' : marginal_pops,
                   'Cumulative_Population' : cumu_pops,
                   'Maxima' : optima}
    return_frame = pd.DataFrame(data = return_dict)
    return return_frame
    

