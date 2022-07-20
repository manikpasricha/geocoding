# A grid of lat/long based on a city's center

### The code geocoding_city takes the city center lat/long as an input and returns a pandas data frame that breaks a city into a number of grids. Each row of the data frame corresponds to lat and long of each block in the grid. 

The function used in this code can be used by pairing with Google Maps Nearby Search API () to find businesses across the city. 
Currently  Google Maps Nearby Search API only returns 60 results per query. The lat/;png data frame genenated through my function can be input to loop through 
and get a much wider search. 

__Function details__
* Name: my_grid

__Input parameters -__ 
* lat: latitude of city center 
* lon: longtitude of city center 
* step_dis: Distance jumped in 1 iteration i.e size of the block
* step_size: # steps i.e. number of blocks




__Sources & shoutouts:__
* Google Maps Nearby Search: https://developers.google.com/maps/documentation/places/web-service/search-find-place
* Image created using https://mobisoftinfotech.com/tools/plot-multiple-points-on-map/
* Stackoverflow https://stackoverflow.com/questions/7222382/get-lat-long-given-current-point-distance-and-bearing#:~:text=asin%20%3D%20arc%20sin()%20d,radians%2C%20clockwise%20from%20north)%3B


