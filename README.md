AutoSismo
=========

Catching earthquakes for a specific day :
```
python -c 'from earthquake import Earthquake; Earthquake.get_daily_earthquakes('your_day')'
```

Example :
```
python -c 'from earthquake import Earthquake; Earthquake.get_daily_earthquakes('2014-10-08')'
```
By default, if none day is definied, the previous day is picked
