import json

def getprices(id):
    rowFile = open('./../data/prices.json')
    prices = json.load(rowFile)
    if (id):
        return filter(
        lambda i:
        int(i['Id']) == int(id), prices)

    return prices