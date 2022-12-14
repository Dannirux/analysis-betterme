from unittest.mock import sentinel
from flask import Flask, json, jsonify, request
from Predict import predict
import requests
import ast

# dataset link -> https://drive.google.com/file/d/1zI4EGD0XEsiZWrOf7Ymoa2QCYx2Wee6J/view?usp=sharing

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! this is sentimental analysis api</p>"


@app.route('/', methods=['GET', 'POST'])
def returnHappinessIndex():
    if request.method == 'POST':
        print('args: ', request.args)
        sentList = ast.literal_eval(request.args.get('sentList'))
        print('sentList', sentList)
        res = predict(sentList)
        result = {

            "total_score": res[0],
            "positive_score": res[1],
            "negative_score": res[2],
            "sentence_list": sentList,
        }
        return jsonify(result)
    else:
        return "<p>Please use proper API POST request call for happiness index</p>"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5500)
