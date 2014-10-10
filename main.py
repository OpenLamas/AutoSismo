from bottle import route, run, template, static_file
from earthquake import Earthquake

@route('/ea')
def ea():
    earthquakes = []

    with open("earthquakes/earthquakes_2014-10-07") as f:
        content = f.readlines()

    for line in content[1:]:
        earthquakes.append(Earthquake(line.split(',')))

    return template('index', earthquakes=earthquakes)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='0.0.0.0', port=8080)