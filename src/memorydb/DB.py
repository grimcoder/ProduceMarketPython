import json

class MemoryDB(object):

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
    def getprices(id):
        if (id):
            return filter(
            lambda i:
            int(i['Id']) == int(id), MemoryDB.prices)
        return MemoryDB.prices

    @staticmethod
    def upsertprices(data):
        if (data.get('Id') == None):
            data['Id'] = MemoryDB.findNextID(MemoryDB.prices)
        else:
            MemoryDB.deleteprices(data['Id'])
        MemoryDB.prices.append(data)

    @staticmethod
    def deleteprices(id):
        MemoryDB.prices = filter(lambda i: i['Id'] != int(id), MemoryDB.prices)

    @staticmethod
    def getsales(id):
      if (id):
          return filter(
              lambda i:
              str(i['Id']) == id, MemoryDB.sales)
      return MemoryDB.sales

    @staticmethod
    def upsertsales(data):
        if (data.get('Id') == None):
            data['Id'] = MemoryDB.findNextID(MemoryDB.sales)
        else:
            MemoryDB.deletesales(data['Id'])
        MemoryDB.sales.append(data)

    @staticmethod
    def deletesales(id):
        MemoryDB.sales = filter(lambda i: i['Id'] != int(id), MemoryDB.sales)

    @staticmethod
    def getPriceChanges(id):
      if (id):
          return filter(
              lambda i:
              str(i['Id']) == id, MemoryDB.priceChanges)
      return MemoryDB.priceChanges
