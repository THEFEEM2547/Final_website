from pymongo import MongoClient
from django.conf import settings

# Establish MongoDB connection
client = MongoClient(settings.MONGO_URI)
mongo_db = client[settings.MONGO_DATABASE_NAME]

class CarModel:
    def __init__(self):
        # Access the 'cars' collection in MongoDB
        self.collection = mongo_db['cars']

    def get_all_cars(self):
        # Fetch all car models from the 'cars' collection
        return list(self.collection.find())

    def get_car_by_id(self, car_id):
        # Fetch a specific car by ID
        return self.collection.find_one({'_id': car_id})
