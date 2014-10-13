# python -c 'from earthquake import Earthquake; Earthquake.get_daily_earthquakes()'

import urllib2
import urllib
from datetime import date, timedelta, datetime
import os

class Earthquake:

    def __init__(self, table):
        date_time = table[0].split("T")

        self.date = date_time[0]
        self.time = date_time[1].translate(None, 'Z').partition('.')[0]
        self.latitude = table[1]
        self.longitude = table[2]
        self.depth = table[3]
        self.mag = table[4]
        self.place = table[13].translate(None, '"')

    @classmethod
    def get_daily_earthquakes(self, day=None, minmagnitude=3):
        
        if not os.path.exists('earthquakes'):
            os.mkdir('earthquakes')
        # Creating date object from day
        if day is None:
            # logger.info('None day is definied, picking current day...')
            day = date.today() - timedelta(days=1)
        else:
            day = datetime.strptime(day, "%Y-%m-%d").date()
        
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
        
        # Sending request
        res = urllib2.urlopen(full_url)

        # Saving results
        filename = "earthquakes/earthquakes_%s" % day.strftime("%Y-%m-%d")
        filee = open(filename, "w")
        filee.write(res.read())
        filee.close()