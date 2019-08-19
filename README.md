# Urban Isochrones
## Research Question
Creating a generalizeable standardized definition of city delinations using urban isochrones. 
- Studied US Metros using CBSA Metro definitions to help understand our isochrones
- Hope to create a global metric using Population Raster data

## Data
Used many data sources to support our work: 
- [US TigerLine Shapefiles](https://www2.census.gov/geo/tiger/TIGER2018/) at County, Tract and Block Group level
- [HERE REST API](https://developer.here.com/documentation/routing/topics/introduction.html) to create isochrones
- [Google API](https://developers.google.com/maps/documentation/geocoding/start) to geocode cities to coordinate centroids
- [World Pop Population Raster Data](https://www.worldpop.org/project/categories?id=3) to get global population data

## Demonstration

Each function is demonstrated and used in a notebook page linked [here](https://github.com/mansueto-institute/urban-isolines/blob/master/City%20Dileniations.ipynb). 

## Usage

- get_isodata returns isoline information from HERE API
- 


