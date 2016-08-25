# NOAA_Webscraper

##### NOAA_Webscraper[lat,long] 

Downloads the hourly forecast for the indicated location beginning at the next midnight, and continuing for 24 hours.  It will save a comma separated .txt file to the current working directory.  The filename will be in the format YYMMDD_HHMMSS_NOAA_Forecast.  The default location is Central Park in New York City.  To change the location enter new latitude and longitude coordinates in the function call at the end of the python script.  Usually 2 integers after the decimal is sufficiently accurate.

#### Parameters:
**lat: [float, -180.0 to 180.0]** Latitude of the location of the forecast. North is positive, South is negative.  
**long: [float, -180.0 to 180.0]** Longitude of the location of the forecast. West is negative, East is positive.

#### Output:
**YYMMDD_HHMMSS_NOAA_Forecast.txt** file containing the downloaded forecast.  This file is in the proper format to be loaded into a pandas.DataFrame.