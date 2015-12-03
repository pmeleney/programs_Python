#Dependencies
import numpy as np
import pandas as pd

import datetime
from bs4 import BeautifulSoup as BSoup
from urllib2 import urlopen
from time import sleep

def wait(seconds):
    #prints one dot a second for seconds.
    
    if type(seconds) != int or seconds < 1 or seconds > 100:
        print 'Please enter a value: 0 < value < 101.'
        return
    
    counter = 0
    while counter < seconds:
        print '.', 
        sleep(1)
        counter += 1
    print ''
    return

def datetimeFormatter(now):
    #Adds leading zeros to a string from a datetime.datetime.now object.
    
    list_of_datetime = [now.year, now.month, now.day, now.hour, now.minute, now.second]
    
    datetime_string = ''
    
    for item in list_of_datetime:
        if item == 0:
            datetime_string = datetime_string + '0' + str(item)
        elif int(np.log10(item)) == 0:
            datetime_string = datetime_string + '0' + str(item)
        else:
            datetime_string = datetime_string + str(item)
    
    #truncate year, add underscore
    datetime_string = datetime_string[2:]
    datetime_string = datetime_string[:6] + '_' + datetime_string[6:]
    
    return datetime_string

def NOAA_Forecast_Scraper(forecastLocation):
    #This function returns a pandas dataframe containing the NOAA weather forecast for the next 24 hours at the 
    #indicated location. 
    
    #forecastLocation should be a list [Latitude_of_forecast_point, Longitude_of_forecast_point] of float type vars.
    #latitude and longitude should be in decimal format.
    #Northern lats and Eastern longs have positive values, Southern lats and Wastern longs have negative values. 
    
    #NOAA makes forecasts for 2.5km square boxes, so precision beyond 0.01 degrees is unnecessary except 
    #at Earth's rotational poles, which is beyond the scope of this project.
    
    Hour = datetime.datetime.today().hour
    AheadHour = 24 - Hour # This needs to be changed if forecast location is not in US Eastern Time Zone, offset by 
                          # hour difference between US Eastern time and forecast location (e.g. for Pacific time zone,
                          # add 3 to the AheadHour to compensate for time difference)
    
    IndexText = [u'Temperature (\xb0F)',u'Dewpoint (\xb0F)',u'Wind Chill (\xb0F)',u'Surface Wind (mph)',u'Wind Dir',
                u'Gust',u'Sky Cover (%)',u'Precipitation Potential (%)',u'Relative Humidity (%)',u'Rain',u'Thunder',
                u'Snow',u'Freezing Rain',u'Sleet']
    
    url = 'http://forecast.weather.gov/MapClick.php?&AheadHour=' + str(AheadHour) + \
    '&FcstType=digital&textField1=' + str(forecastLocation[0]) + '&textField2=' + \
    str(forecastLocation[1])
    
    #This slows down how often the function pings the NOAA server, wait function is to keep the user occupied.
    print 'downloading NOAA forecast', 
    wait(3)
    
    html = urlopen(url).read() #This pings the NOAA server, use sparingly
    soup = BSoup(html)
    
    print 'download complete.'
        
    All_Text = [] #A list where each item is a string with the value of something in a table on the html page.
    for ele in soup.find_all('td'):
        All_Text.append(ele.get_text())
        
    list_Of_Features = []
    for feature in IndexText:
        featureIndex = All_Text.index(feature)
        list_Of_Features.append(All_Text[featureIndex:featureIndex+25])
    
    #Record time of forecast
    now = datetime.datetime.now()
    datetime_string = datetimeFormatter(now)
    filename = datetime_string + '_NOAA_Forecast'
    timestamp = 'Time of Forecast: ' + datetime_string
    
    #Format output into pd.DateFrame
    Output = pd.DataFrame(list_Of_Features)
    Output.columns = [timestamp] + range(1,25)
    Output.index = Output.iloc[:,0]
    Output = Output.drop(timestamp,axis = 1)
    
    #Values as read from NOAA website are not ascii-compatible.  This encodes the index in utf-8.
    csv_compatible_index = []
    for item in Output.index:
        csv_compatible_index.append(item.encode('utf-8'))
    Output.index = csv_compatible_index
    
    #Prints a csv every time the function is executed.  Datetime information is within the filename.
    Output.to_csv(filename)    

    return Output

NOAA_Forecast_Scraper([40.78, -73.97])

