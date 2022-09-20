import json
from flask import Flask, request, jsonify, Response
from actions.mongo import getDatabase, migrateFromCsv
from bson.json_util import dumps
from bson.json_util import loads

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/migrate", methods=["POST"])
def migrate():
    migrateFromCsv()
    return 'migrated'


@app.route("/mostRated", methods=["GET"])
def mostRated():
    query = request.args.to_dict()
    db = getDatabase()
    filter_query = {'prime_genre' : query['genere']} if 'genere' in query else {}
    print(filter_query)
    result = db.appleStore.find(filter_query)
    if 'sort_by' in query:
        result = result.sort(query['sort_by'], -1)
    if 'limit' in query:
        result = result.limit(int(query['limit']))
    json_data = dumps(list(result))
    return json_data
