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
            data['Id'] = DB.findNextID(DB.prices)
        else:
            Action = 'Edit'
            oldPrice = filter(lambda i: i['Id'] == int(data['Id']), DB.prices)[0]['Price']
            DB.prices = filter(lambda i: i['Id'] != int(data['Id']), DB.prices)

        DB.prices.append(data)
        data['Action'] = Action
        data['priceWas'] = oldPrice
        DB.priceChanges.append(data)
        DB.saveobjecttofile(DB.prices,'./../data/prices.json')
        DB.saveobjecttofile(DB.priceChanges,'./../data/priceChanges.json')


    @staticmethod
    def deleteprices(id):

        data = copy.deepcopy(filter(lambda i: i['Id'] == int(id), DB.prices)[0])

        DB.prices = filter(lambda i: i['Id'] != int(id), DB.prices)
        DB.saveobjecttofile(DB.prices,'./../data/prices.json')
        data['Action'] = "Delete"
        DB.priceChanges.append(data)
        DB.saveobjecttofile(DB.priceChanges,'./../data/priceChanges.json')

    @staticmethod
    def getsales(id):
        if (id):
            return DB.addIdtoList(DB.sales.find({u'_id': ObjectId(id)}))
        return DB.addIdtoList(list(DB.sales.find()))

    @staticmethod
    def upsertsales(data):
        if (data.get('Id') == None):
            data['Id'] = DB.findNextID(DB.sales)
        else:
            DB.deletesales(data['Id'])
        DB.sales.append(data)
        DB.saveobjecttofile(DB.sales,'./../data/sales.json')

    @staticmethod
    def deletesales(id):
        DB.sales = filter(lambda i: i['Id'] != int(id), DB.sales)
        DB.saveobjecttofile(DB.sales,'./../data/sales.json')

    @staticmethod
    def getPriceChanges(id):
        if (id):
            return DB.addIdtoList(DB.pricechanges.find({u'_id': ObjectId(id)}))
        return DB.addIdtoList(list(DB.pricechanges.find()))
