from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoHelper():

    def __init__(self):
        self.user = 'jdayalan1'
        self.password = 'BWDahvk1p7Ll2CdI'
        self.host = 'mine-bdag3.eu1aic0.mongodb.net'
        self.open()
        
    def open(self):
        print("Connecting to DB...")
        url= f'mongodb+srv://{self.user}:{self.password}@{self.host}/?retryWrites=true&w=majority'
        self.client = MongoClient(url, server_api=ServerApi('1'))
        self.db = self.client['MINE-BDAG3']
        print("Connection succesful")

    def close(self):
        print("Closing Connection...")
        self.client.close()

    def get_heatmap_data(self):
        print("Getting HeatMap Data...")
        result = self.db.heatmap.find()
        return list(result)
    
    def get_vessels(self):
        print("Getting routes Data...")
        result = self.db.routes.distinct('VesselName')
        return list(result)
    
    def get_vessel_data(self,name):
        print("Getting routes Data...")
        result = self.db.routes.find({'VesselName':name})
        return list(result)