#! python3

# quickWeather.py - prints the weather for a given location from the command line

import json
import requests
import sys
import pprint


debug = None

if len(sys.argv) > 1:
    debug = sys.argv[1]



url = 'http://192.168.1.201/api/NNKCJxSsNFd1WMPpA5BsoKHG0kRXu7ImwuwX711z/sensors/19'

response = requests.get(url)
response.raise_for_status()



# Get the data into a json Variable

tempData = json.loads(response.text)


w = tempData['state']

lasttrigger = (w.get('lastupdated', 'Sensor Fault'))

temp = (w.get('temperature', 'Sensor Does not report Temperature')) / 100

if str(debug) == 'DEBUG':
    pprint.pprint(tempData)

print('Temp ' + str(temp) + ' Celcius')









