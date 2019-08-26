# Urban Isochrones
## Research Question
Creating a generalizeable standardized definition of city delinations using urban isochrones. 
- Studied US Metros using CBSA Metro definitions to help understand our isochrones
- Hope to create a global metric using Population Raster data

## Data Sources and Python Libraries
Used many data sources to support our work that you will need for parts of the project. 
- [HERE REST API](https://developer.here.com/documentation/routing/topics/introduction.html) to create isochrones. You will need to create a Here API code and key available on the HERE website.
- The following Python Libraries will be needed: [Shapely](https://pypi.org/project/Shapely/), [GeoPandas](http://geopandas.org/install.html), [Folium](https://pypi.org/project/folium/), [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html), [Numpy](https://www.scipy.org/install.html), [MatPotLib](https://matplotlib.org) 
- [US TigerLine Shapefiles](https://www2.census.gov/geo/tiger/TIGER2018/) at County and Block Group level
    - To compare isolines to city shapefiles you will need the [cbsa city definitions](https://www2.census.gov/geo/tiger/TIGER2018/CBSA/)
    - To generate population data using the isolines you will need [County](https://www2.census.gov/geo/tiger/TIGER2018/COUNTY/) and [Block Group](https://www2.census.gov/geo/tiger/TIGER2018/BG/) shapefiles. (There are many blockgroup folders, downloads ones for the states that you need. 
    - [Urban Areas](https://www2.census.gov/geo/tiger/TIGER2018/UAC/) will allow us to match our isolines to cbsa defined urban areas
- For population data you will need to install the [Census](https://pypi.org/project/census/) python library and get a Census API Key. Instructions for getting a key are on the Census link. 
- [Google API](https://developers.google.com/maps/documentation/geocoding/start) to get centroid coordinates from city names. You will need an API Key available at the link. 
- [World Pop Population Raster Data](https://www.worldpop.org/project/categories?id=3) to get global population raster data


## Demonstration

Each function is demonstrated and used in a notebook page linked [here](https://github.com/mansueto-institute/urban-isolines/blob/master/City%20Dileniations.ipynb). The demonstration is used to study the top 30 cities in the US by size, and then later uses Raster Data to study the top 5 cities in Spain. Some of the useful functions are updated and uploaded in the functions folder such that they can be used in a more general way. 

## Function List

Can be found in the functions folder. 

#### Querying Functions
- `get-isodata` : Wrapper function for Here API. Requires location coordinates, and has other optional parameters. (Store api key and code as here_api_key and here_api_code in a file called config.py)
- `get-google-coords`: Wrapper function for Google Geocoder API. (Store Google API key in config.py file as google_api_key

#### Mapping Functions
- `isoplot`: Plots a geoseries and/or a city shapefile onto a folium map with the coordinates given to the function. 
- `geoseries_area`: Calculates the area of a polygon in square kilometers. 

#### Data Processing Functions
- `isoline_contains`: Returns a csv containing data about the fitness of isolines from the coordinates given matching city boundaries of a shapefile given. 
- `isoline_pops`: Returns a csv containing data about the population statistics of isolines centering at the coordinates given as well as area data about the isoline as related to a city shapefile provided. 
- `isoline_raster_pops`: Returns a csv containing data about the population statistics of isolines using population raster data

## Future 

[Presentation](https://docs.google.com/presentation/d/1B1CAW1vU8_PIuuITTDEFKXsauqRcdeniZEfLgxdBOow/edit#slide=id.g5f77c7d6fb_0_405) on learnings and future work

## Authors/Contact

- Kahaan Shah - Twitter: @kahaantrueblue - kahaan at uchicago dot edu
- Nicholas Marchio

## [License](https://github.com/mansueto-institute/urban-isolines/blob/master/LICENSE)


