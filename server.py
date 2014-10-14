from bottle import route, run, template, static_file
from earthquake import Earthquake
from datetime import date, timedelta, datetime
from subprocess import call
import locale, os

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
            with open(os.path.join(Earthquake.data_folder, 'earthquakes_%s' % day.strftime("%Y-%m-%d"))) as f:
                earthquake_file_content = f.readlines() or None
            
            # Create objects
            for line in earthquake_file_content[1:]:
                earthquakes.append(Earthquake(line.split(',')))
                
        except IOError:
            # File not existing, trying to download it.
            Earthquake.get_daily_earthquakes(day.strftime("%Y-%m-%d"))

    return template('index', earthquakes=earthquakes, day=day.strftime("%A %d %B %Y").capitalize())

@route('/static/<path:path>')
def server_static(path):
    return static_file(path, root='static')

port = int(os.environ.get("PORT", 8080))
run(host='0.0.0.0', port=port, reloader=True)
