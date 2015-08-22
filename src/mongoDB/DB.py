__author__ = 'taraskovtun'

import pymongo

import json

class MemoryDB(object):

    # rowFile = open('./../data/prices.json')
    # prices = json.load(rowFile)
    # rowFile = open('./../data/sales.json')
    # sales = json.load(rowFile)
    # rowFile = open('./../data/priceChanges.json')
    # priceChanges = json.load(rowFile)

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
            int(i['Id']) == int(id), MemoryDB.prices)
        return MemoryDB.prices

    @staticmethod
    def upsertprices(data):
        oldPrice = 'n/a'
        if (data.get('Id') == None):
            Action = 'New'
            data['Id'] = MemoryDB.findNextID(MemoryDB.prices)
        else:
            Action = 'Edit'
            oldPrice = filter(lambda i: i['Id'] == int(data['Id']), MemoryDB.prices)[0]['Price']
            MemoryDB.prices = filter(lambda i: i['Id'] != int(data['Id']), MemoryDB.prices)

        MemoryDB.prices.append(data)
        data['Action'] = Action
        data['priceWas'] = oldPrice
        MemoryDB.priceChanges.append(data)
        MemoryDB.saveobjecttofile(MemoryDB.prices,'./../data/prices.json')
        MemoryDB.saveobjecttofile(MemoryDB.priceChanges,'./../data/priceChanges.json')


    @staticmethod
    def deleteprices(id):

        data = filter(lambda i: i['Id'] == int(id), MemoryDB.prices)[0]
        MemoryDB.prices = filter(lambda i: i['Id'] != int(id), MemoryDB.prices)
        MemoryDB.saveobjecttofile(MemoryDB.prices,'./../data/prices.json')
        data['Action'] = "Delete"
        MemoryDB.priceChanges.append(data)
        MemoryDB.saveobjecttofile(MemoryDB.priceChanges,'./../data/priceChanges.json')

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
        MemoryDB.saveobjecttofile(MemoryDB.sales,'./../data/sales.json')

    @staticmethod
    def deletesales(id):
        MemoryDB.sales = filter(lambda i: i['Id'] != int(id), MemoryDB.sales)
        MemoryDB.saveobjecttofile(MemoryDB.sales,'./../data/sales.json')

    @staticmethod
    def getPriceChanges(id):
      if (id):
          return filter(
              lambda i:
              str(i['Id']) == id, MemoryDB.priceChanges)
      return MemoryDB.priceChanges
