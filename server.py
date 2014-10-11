from bottle import route, run, template, static_file
from earthquake import Earthquake
from datetime import date, timedelta, datetime
from subprocess import call
import locale

locale.setlocale(locale.LC_ALL, '')


@route('/')
@route('/<day>')
def ea(day=None):
    earthquakes = []
    file_day = None

    # Returns yesterday if day is defined
    if day is None:
        day = date.today() - timedelta(days=1)
    else:
        day = datetime.strptime(day, "%Y-%m-%d")

    for _ in range(2):
        try:
            with open("earthquakes/earthquakes_%s" % day.strftime("%Y-%m-%d")) as f:
                content = f.readlines()
        except IOError:
            # File not existing, retrying after download it
            Earthquake.get_daily_earthquakes(day.strftime("%Y-%m-%d"))
            pass

    for line in content[1:]:
        earthquakes.append(Earthquake(line.split(',')))

    return template('index', earthquakes=earthquakes, day=day.strftime("%A %d %B %Y").capitalize())

@route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='static')

run(host='0.0.0.0', port=8080)