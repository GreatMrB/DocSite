from pymongo import MongoClient

cluster = MongoClient(
    'mongodb+srv://beka:Almaty2018@cluster0.udkjxo3.mongodb.net/table?retryWrites=true&w=majority')
database = cluster.table
collection = database.tabcollection
collection.insert_one({'_id': 1, 'name': 'beka', 'balance': 202})
