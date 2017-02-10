import json
import requests
import time
import pprint
import pymongo

for I in range(12):


    offurl = 'http://192.168.1.201/api/NNKCJxSsNFd1WMPpA5BsoKHG0kRXu7ImwuwX711z/lights/' + str(I) + '/state'
    headers = {'content-type': 'application/json'}

    _ = requests.get(offurl)
    _.raise_for_status()
    print(_)

    lightData = json.loads(_.text)
    pprint.pprint(lightData)



    payload = {"bri": 300, "on": True, "ct": 154, "alert": "lselect", "colormode" : "xy", "xy" : [ 0.6752, 0.3004]}

    _ = requests.put(offurl, data=json.dumps(payload), headers=headers)




