

from census import Census
import get_isodata
import geoseries_area

bg_name = 'BG/tl_2018_{}_bg/tl_2018_{}_bg.shp'
pop_code = 'B01003_001E'
c = Census(config.census_api_key)


def isoline_pops(center, city_shape):
    """
    Paraneters:
    center - coordinates of the center of isolines
    city_shape - city shapefile
    Function returns a data frame consisting of the marginal population and areas of each
    isoline increasing in 10 minutes. The function is given co-ordinates of the center of cities
    and runs until it reaches 98% percentage of the city. 
    """
    used_shape = city_shape.copy()
    big_isoline = get_isodata(center, range_iso = 9000)
    used_shape = big_isoline.intersection(used_shape)
    city_area = geoseries_area(city_shape)
    count = 0
    zero_count = 0
    overlap = 10000
    time = 600
    times, marginal_pops, containments, cumu_pops, cumu_area, IOU_list, areas, geometries = [], [], [], [], [], [], []. []
    cumu_area = overlap/city_area 
    merged = gpd.GeoDataFrame()
    states = []
    state_data = []
    states_read = dict()
    st_county_read = dict()
    while (sum(cumu_areas) < 0.98 and count<24 and zero_count < 3): 
        isoline = get_isodata(center, range_iso = time, traffic = 'enabled', departure = '2019-02-13T16:00:00')
        intersection = geoseries_area(isoline.intersection(city_shape))
        containment = (intersection/city_area) * intersection/(geoseries_area(isoline))
        containments.append(containment)
        union = geoseries_area(isoline.union(city_shape))
        IOU_list.append(intersection/union)
        if count == 0:
            isoline_gdf = gpd.GeoDataFrame(geometry = isoline)
            isoline_gdf.crs = {'init':'epsg:4326'}
        else:
            isoline_gdf = gpd.GeoDataFrame(geometry = isoline.difference(prev_isoline))
            isoline_gdf.crs = {'init':'epsg:4326'}
        states = gpd.sjoin(US_counties, isoline_gdf, op="intersects").STATEFP.unique()
        for state in states:
            if state in states_read.keys():
                pass
            else:
                bg_new = gpd.read_file(bg_name.format(state,state))
                bg_new.crs = ({'init':'epsg:4326'})
                states_read[state] = bg_new
                merged = pd.concat([merged, bg_new])
        marginal_pops.append(0)
        current_iso = gpd.sjoin(merged, isoline_gdf, op='intersects')
        for index, row in current_iso.iterrows():
            state_county = row['STATEFP'] + row['COUNTYFP']
            if not (state_county) in st_county_read.keys():
                st_county_read[state_county] = dict()
                county_bg_data = c.acs5.state_county_blockgroup(pop_code, row['STATEFP'], row['COUNTYFP'], Census.ALL)
                for d in county_bg_data:
                    st_county_read[state_county][state_county + d['tract'] + d['block group']] = d[pop_code]
            marginal_pops[count] += st_county_read[state_county][row['GEOID']]
            isoline = isoline.union(row['geometry'])
        overlap = geoseries_area(isoline.intersection(used_shape))
        geometries.append(isoline[0])
        times.append(time/60)
        areas.append(geoseries_area(isoline))
        cumu_area = overlap/city_area
        if cumu_area == 0:
            zero_count += 1
        cumu_areas.append(cumu_area)
        used_shape = used_shape.difference(isoline)
        if count == 0:
            prev_isoline = gpd.GeoDataFrame(geometry = isoline)
            prev_isoline.crs = {'init' : 'epsg:4326'}
        else :
            prev_isoline = gpd.GeoDataFrame(geometry = prev_isoline.union(isoline))
            prev_isoline.crs = {'init' : 'epsg:4326'}
        time += 600
        count += 1
    optima = []
    largest_IOU = []
    cumu_pop = 0
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
        if max(IOU_list) == IOU_list[index]:
            largest_IOU.append(1)
        else:
            largest_IOU.append(0)
    return_dict = {'Times' : times, 
                   'Cumulative_Areas' : cumu_areas, 
                   'Areas' : areas,
                   'Marginal_Population' : marginal_pops,
                   'Cumulative_Population' : cumu_pops,
                  'Optima' : optima,
                  'IoU' : IOU_list,
                  'IOU_Largest': largest_IOU}
    return_frame = pd.DataFrame(data = return_dict)
    return return_frame
                