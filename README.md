# Urban Isochrones
## Research Question
Creating a generalizeable standardized definition of city delinations using urban isochrones. 
- Studied US Metros using CBSA Metro definitions to help understand our isochrones
- Hope to create a global metric using Population Raster data

## Usage
Used many data sources to support our work, that you will need if using different parts of the project. 
- [HERE REST API](https://developer.here.com/documentation/routing/topics/introduction.html) to create isochrones. You will need to create a Here API code and key available on the HERE website.
- The following Python Libraries will be needed: [Shapely](https://pypi.org/project/Shapely/), [GeoPandas](http://geopandas.org/install.html), [Folium](https://pypi.org/project/folium/), [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html), [Numpy](https://www.scipy.org/install.html), [MatPotLib](https://matplotlib.org) 
- [US TigerLine Shapefiles](https://www2.census.gov/geo/tiger/TIGER2018/) at County and Block Group level
    - To compare isolines to city shapefiles you will need the [cbsa city definitions](https://www2.census.gov/geo/tiger/TIGER2018/CBSA/)
    - To generate population data using the isolines you will need [County](https://www2.census.gov/geo/tiger/TIGER2018/COUNTY/) and [Block Group](https://www2.census.gov/geo/tiger/TIGER2018/BG/) shapefiles. (There are many blockgroup folders, downloads ones for the states that you need. 
    - [Urban Areas](https://www2.census.gov/geo/tiger/TIGER2018/UAC/) will allow us to match our isolines to cbsa defined urban areas
- For population data you will need to install the [Census](https://pypi.org/project/census/) python library and get a Census API Key. Instructions for getting a key are on the Census link. 
- [Google API](https://developers.google.com/maps/documentation/geocoding/start) to get centroid coordinates from city names. You will need an API Key available at the location. 
- [World Pop Population Raster Data](https://www.worldpop.org/project/categories?id=3) to get global population raster data


## Demonstration

Each function is demonstrated and used in a notebook page linked [here](https://github.com/mansueto-institute/urban-isolines/blob/master/City%20Dileniations.ipynb). 

## Usage

- get_isodata returns isoline information from HERE API
- 


