import copy
from bson import ObjectId


class DB(object):
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client.ProduceMarket
    prices = db['prices']
    sales = db['sales']
    pricechanges = db['pricechanges']

    @staticmethod
    def addIdVirtualField(data):
        data['Id'] = str(data['_id'])
        data['_id'] = data['Id']
        return data

    @staticmethod
    def addIdtoList(arr):
        return map(lambda i: DB.addIdVirtualField(i), arr)

    @staticmethod
    def getprices(id):
        if (id):
            return DB.addIdtoList(DB.prices.find({u'_id': ObjectId(id)}))
        return DB.addIdtoList(list(DB.prices.find()))

    @staticmethod
    def upsertprices(data):
        oldPrice = 'n/a'
        if (data.get('Id') == None):
            Action = 'New'
        else:
            Action = 'Edit'
            oldPrice = DB.prices.find_one({'_id': ObjectId(data['Id'])})['Price']
            DB.prices.delete_one({'_id': ObjectId(data['Id'])})
        data['_id'] = ObjectId(data['Id'])
        DB.prices.insert_one(data)
        data['Action'] = Action
        data['priceWas'] = oldPrice
        data['_id'] = None
        DB.pricechanges.insert_one(data)

    @staticmethod
    def deleteprices(id):
        data = DB.prices.find_one({'_id' : ObjectId(id)})
        DB.prices.delete_one({'_id' : ObjectId(id)})
        data['Action'] = "Delete"
        DB.pricechanges.insert_one(data)

    @staticmethod
    def getsales(id):
        if (id):
            return DB.addIdtoList(DB.sales.find({u'_id': ObjectId(id)}))
        return DB.addIdtoList(list(DB.sales.find()))

    @staticmethod
    def upsertsales(data):
        if (data.get('Id') != None):
            DB.sales.delete_one({'_id': ObjectId(data['Id'])})
        data['_id'] = ObjectId(data['Id'])
        DB.sales.insert_one(data)

    @staticmethod
    def deletesales(id):
        DB.sales.delete_one({'_id' : ObjectId(id)})

    @staticmethod
    def getPriceChanges(id):
        if (id):
            return DB.addIdtoList(DB.pricechanges.find({u'_id': ObjectId(id)}))
        return DB.addIdtoList(list(DB.pricechanges.find()))
