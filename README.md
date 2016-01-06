# usefulPythonPrograms

This is a repository of generalized programs I wrote for various tasks in the past and might want to use again.


NOAA_Webscraper[lat,long] 

Downloads the hourly forecast for the indicated location beginning at the next midnight, and continuing for 24 hours.  It will save a comma separated .txt file to the current working directory.  The filename will be in the format YYMMDD_HHMMSS_NOAA_Forecast.  The default location is Central Park in New York City.  To change the location enter new latitude and longitude coordinates in the function call at the end of the python script.  Usually 2 integers after the decimal is sufficiently accurate.


zScore_numSamples[numSamples, OneSided = True, zTable_min = 1, zTable_max = 6.001, zStep = 0.001]

Provides a test for whether outliers are caused by stochastic error or some other influence.  The function takes the number of samples in a dataset and returns the number of standard deviations beyond which one would expect to see a single data point 50% of the time.  If there exist many outliers beyond this number of standard deviations away, then the outliers are probably caused by some influence other than stochastic error.

The actual rate of occurrence is limited by the zStep, this is accounted for in the results by printing the actual number of samples at which one can expect to see one occurrence.  This value is rounded to the nearest whole number. Since it is constant in zStep is not constant in numSamples, the calculation becomes much less accurate as Z increases.  I chose 8.0 as the default zTable_max because erf(9.0/np.sqrt(2)) is beyond the precision of the default float variable.