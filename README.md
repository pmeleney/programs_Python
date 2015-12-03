# usefulPythonPrograms

This is a repository of generalized programs I wrote for various tasks in the past and might want to use again.

NOAA_Webscraper[lat,long] is a python program which will download the hourly forecast for the indicated location beginning at the next midnight, and continuing for 24 hours.  It will save a comma separated .txt file to the current working directory.  The filename will be in the format YYMMDD_HHMMSS_NOAA_Forecast.  The default location is Central Park in New York City.  To change the location enter new latitude and longitude coordinates in the function call at the end of the python script.  Usually 2 integers after the decimal is sufficiently accurate.
