from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, pwd):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:46678' % (user, pwd))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            return True            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, readData):
        if readData:
            data = self.database.animals.find({}, {"_id": False})
            return data
        
# Create method to implement the U in CRUD
    def update(self, query, record):
        if record is not none:
            update_result = self.database.animals.update_many(query, record)
            result = "Documents updated: " + json.dumps(update_result.modified_count)
            return result
        
        else:
            raise Exception("Record not found.")
            
# Create method to implement D in CRUD
    def delete(self, data):
        if data is not none:
            delete_result = self.database.animals.delete_many(data)
            result = "Documents deleted: ", json.dumps(delete_result.deleted_count)
            return result
        
        else:
            raise Exception("No record provided!")