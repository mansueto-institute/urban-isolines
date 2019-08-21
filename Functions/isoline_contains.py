import get_isodata
import geoseries_area
import pandas as pd



def isoline_contains(center, city_shape):
    """
    Performs calculations about the fitness of isolines and how well they match up to shapefiles 
    given to the functions. Examples below are shown using different forms of shapefiles, 
    cbsa and urban areas definitions, #Fitness is defined as percentage of area of isoline
    within city boundaries
    Paraneters:
    center - coordinates for center of isoline
    city_shape - city shapefile
    """
    time = 600
    times = []
    fitness = []
    areas_both = []
    areas_only_isoline = []
    isoline_areas = []
    while(time<9000):
        isoline = get_isodata(center, range_iso = time, traffic = 'enabled', departure = '2019-02-12T16:00:00')
        isoline_gdf = gpd.GeoDataFrame(geometry = isoline)
        intersection = gpd.overlay(isoline_gdf, city_shape, how = 'intersection')
        intersection_area = geoseries_area(intersection)
        isoline_area = geoseries_area(isoline)
        areas_only_isoline.append(isoline_area-intersection_area)
        fitness.append(intersection_area/isoline_area)
        isoline_areas.append(isoline_area)
        areas_both.append(intersection_area)
        times.append(time/60)
        time += 600
        print(time)
    largest_IOU = []
    for index, num in enumerate(fitness):
        if max(fitness) == fitness[index]:
            largest_IOU.append(1)
        else:
            largest_IOU.append(0)
    return_dict = {'Times' : times, 
                   'Fitness' : fitness, 
                   'Isoline_Area' : isoline_areas,
                   'Intersection' : areas_both,
                    'Only_Isoline' : areas_only_isoline,
                  'Greatest Fitness': largest_IOU}
    return_frame = pd.DataFrame(data = return_dict)
    return return_frame
    