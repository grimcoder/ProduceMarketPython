from flask.ext.api import FlaskAPI
from flask import  request
from flask.ext.cors import CORS

app = FlaskAPI(__name__)
CORS(app)
from memorydb.DB import *

@app.route("/api/prices")
def prices():
    id = request.args.get('id')
    return getprices(id)

@app.route("/api/sales")
def sales():
    id = request.args.get('id')
    return getsales(id)


@app.route("/api/reports/prices")
def priceChanges():
    id = request.args.get('id')
    return getPriceChanges(id)

if __name__ == '__main__':
    app.run(debug=True, port=3001, threaded=True)