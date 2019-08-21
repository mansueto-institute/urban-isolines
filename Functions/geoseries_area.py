
def geoseries_area(geoser):
	"""
	#Returns area of a geoseries in square kilometers
	Parameters: 
	geoser - Geoseries containing polygon(s)
	"""
    area_ser = geoser.to_crs({'proj':'cea'})
    area = area_ser.area
    total_area = 0
    for index, value in area.iteritems():
        total_area += value
    return (total_area / 10**6)
