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

collection = db.lights

pprint.pprint(collection)