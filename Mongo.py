import pymongo
import json
import requests
import pprint

from pymongo import MongoClient

try:
    client = MongoClient()
    pprint.pprint('Mongo Connection Ready...')
except pymongo.errors.ConnectionFailure as e:
    pprint.pprint('Connection Failed')



    db = client.smart_home_db

    url = 'http://192.168.1.201/api/NNKCJxSsNFd1WMPpA5BsoKHG0kRXu7ImwuwX711z/lights/' + str(I)

    response = requests.get(url)




    lightData = json.loads(response.text)

    pprint.pprint(lightData)

    lights = db.lights

    post_id = lights.insert_one(lightData)



