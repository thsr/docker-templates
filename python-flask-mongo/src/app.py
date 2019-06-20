from flask import Flask, Response, jsonify
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/", username="user", password="pass")
db = client["mydb"]

@app.route('/testinsert/<foo>')
def testinsert(foo):
    try:
        data = { "foo": foo }
        x = db.mycollection.insert_one(data)
        return Response(json_util.dumps(x.inserted_id), mimetype="application/json")
    except Exception as e:
        return jsonify(str(e)), 500

@app.route('/testfind')
def testfind():
    try:
        res = db.mycollection.find()
        return Response(json_util.dumps([x for x in res]), mimetype="application/json")
    except Exception as e:
        return jsonify(str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)