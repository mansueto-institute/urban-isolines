# Urban Isochrones
## Research Question
Creating a generalizeable standardized definition of city delinations using urban isochrones. 
- Studied US Metros using CBSA Metro definitions to help understand our isochrones
- Hope to create a global metric using Population Raster data

## Usage
Used many data sources to support our work, that you will need if using different parts of the project. 
- [HERE REST API](https://developer.here.com/documentation/routing/topics/introduction.html) to create isochrones. You will need to create a Here API code and key available on the HERE website.
- The following Python Libraries will be needed: [Shapely](https://pypi.org/project/Shapely/), [GeoPandas](http://geopandas.org/install.html), [Folium](https://pypi.org/project/folium/), [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)
- [US TigerLine Shapefiles](https://www2.census.gov/geo/tiger/TIGER2018/) at County, Tract and Block Group level
    - To compare isolines to city shapefiles you will need the [cbsa city definitions](https://www2.census.gov/geo/tiger/TIGER2018/CBSA/)
    

- [Google API](https://developers.google.com/maps/documentation/geocoding/start) to geocode cities to coordinate centroids
- [World Pop Population Raster Data](https://www.worldpop.org/project/categories?id=3) to get global population data
- [Census 

## Demonstration

Each function is demonstrated and used in a notebook page linked [here](https://github.com/mansueto-institute/urban-isolines/blob/master/City%20Dileniations.ipynb). 

## Usage

- get_isodata returns isoline information from HERE API
- 


