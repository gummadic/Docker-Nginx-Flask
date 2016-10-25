#!/usr/bin/python3
from flask import Flask, request, json, Response
from MongoDao import MongoDao
from bson import json_util
import os

app = Flask(__name__)
logger = app.logger
dao = MongoDao("mongodb://test:test@ds063856.mlab.com:63856/auth");

@app.route("/token")
def getToken():
    logger.debug("Get Token");
    key = request.args.get('key');
    secret = request.args.get('secret');
    result = dao.authenticateClient(key, secret);
    if result:
        return Response(json_util.dumps({"token":result}), status=201);
    else:
        return Response(status=401);

@app.route("/health")
def health():
    logger.debug("Get Health");
    return json.jsonify(healthy='true');

if __name__ == "__main__":
    app.run()
