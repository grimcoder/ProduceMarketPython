import json

def getprices(id):
    rowFile = open('./../data/prices.json')
    prices = json.load(rowFile)
    if (id):
        return filter(
        lambda i:
        int(i['Id']) == int(id), prices)

    return prices

def getsales(id):
  rowFile = open('./../data/sales.json')
  sales = json.load(rowFile)
  if (id):
      return filter(
          lambda i:
          str(i['Id']) == id, sales)

  return sales

def getPriceChanges(id):
  rowFile = open('./../data/priceChanges.json')
  priceChanges = json.load(rowFile)

  if (id):
      return filter(
          lambda i:
          str(i['Id']) == id, priceChanges)

  return priceChanges

