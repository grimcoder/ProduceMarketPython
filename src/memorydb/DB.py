import json

class DB(object):

    rowFile = open('./../data/prices.json')
    prices = json.load(rowFile)
    rowFile = open('./../data/sales.json')
    sales = json.load(rowFile)
    rowFile = open('./../data/priceChanges.json')
    priceChanges = json.load(rowFile)

    @staticmethod
    def findNextID(arr):
        iDs = map(lambda i: i['Id'], arr)
        maxId = max(iDs)
        return maxId + 1

    @staticmethod
    def saveobjecttofile(data, filename):
        f = open(filename, 'w')
        string = json.dumps(data)
        f.write(string)
        return

    @staticmethod
    def getprices(id):
        if (id):
            return filter(
            lambda i:
            int(i['Id']) == int(id), DB.prices)
        return DB.prices

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

        data = filter(lambda i: i['Id'] == int(id), DB.prices)[0]
        DB.prices = filter(lambda i: i['Id'] != int(id), DB.prices)
        DB.saveobjecttofile(DB.prices,'./../data/prices.json')
        data['Action'] = "Delete"
        DB.priceChanges.append(data)
        DB.saveobjecttofile(DB.priceChanges,'./../data/priceChanges.json')

    @staticmethod
    def getsales(id):
      if (id):
          return filter(
              lambda i:
              str(i['Id']) == id, DB.sales)
      return DB.sales

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
          return filter(
              lambda i:
              str(i['Id']) == id, DB.priceChanges)
      return DB.priceChanges
