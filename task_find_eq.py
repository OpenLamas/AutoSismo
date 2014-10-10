import urllib2
import urllib
from datetime import date, timedelta

# Params
# starttime=2014-10-08 00:00:00
# minmagnitude=4
# format=csv
# endtime=2014-10-08 23:59:59
# orderby=time
# request = "http://comcat.cr.usgs.gov/fdsnws/event/1/query?starttime=2014-10-08%2000:00:00&minmagnitude=4&format=csv&endtime=2014-10-08%2023:59:59&orderby=time"

def get_earthquakes(day):
    
    minmagnitude = '3'
    # Defining url
    url = 'http://comcat.cr.usgs.gov/fdsnws/event/1/query?'
    
    # Formatting args
    data = {
          'format' : 'csv',
          'starttime' : day.strftime("%Y-%m-%d 00:00:00"),
          'minmagnitude' : minmagnitude,
          'endtime' : day.strftime("%Y-%m-%d 23:59:59"),
          'orderby' : 'time' 
    }
    params = urllib.urlencode(data)
    full_url = url + params
    res = urllib2.urlopen(full_url)
    write_results_to_file(day.strftime("%Y-%m-%d"), res)

def write_results_to_file(day, results):
    # Write to file
    filename = "earthquakes/earthquakes_%s" % day
    filee = open(filename, "w")
    filee.write(results.read())
    filee.close()

def get_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday

day = get_yesterday()
get_earthquakes(day)