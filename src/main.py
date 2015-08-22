from flask.ext.api import FlaskAPI
from flask import request
from flask.ext.cors import CORS
import sys

if ('m' in sys.argv):
    useMongo = True

app = FlaskAPI(__name__)
CORS(app)
from memorydb.DB import *

@app.route("/api/prices", methods=['GET'])
def prices():
    id = request.args.get('id')
    return MemoryDB.getprices(id)

@app.route("/api/prices", methods=['POST'])
def upsertprices():
    data = request.data
    MemoryDB.upsertprices(data)
    return ''


@app.route("/api/sales", methods=['POST'])
def upsertsales():
    data = request.data
    MemoryDB.upsertsales(data)
    return ''

@app.route("/api/prices", methods=['DELETE'])
def pricesdelete():
    id = request.args.get('id')
    MemoryDB.deleteprices(id)
    return ''

@app.route("/api/sales")
def sales():
    id = request.args.get('id')
    return MemoryDB.getsales(id)

@app.route("/api/sales", methods=['DELETE'])
def salesdelete():
    id = request.args.get('id')
    MemoryDB.deletesales(id)
    return ''

@app.route("/api/reports/prices")
def pricechanges():
    id = request.args.get('id')
    return MemoryDB.getPriceChanges(id)

if __name__ == '__main__':
    app.run(debug=True, port=3001, threaded=True)