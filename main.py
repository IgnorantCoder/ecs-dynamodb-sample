from flask import Flask, jsonify, make_response, request
import boto3
from boto3.dynamodb.conditions import Key


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    response_body = {
        'msg': 'Hello world.'
    }
    return make_response(jsonify(response_body))


@app.route('/songs', methods=['POST'])
def songs():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    query = {
        'KeyConditionExpression': Key('Artist').eq(request.json['artist']),
        'ProjectionExpression': ','.join([
            'SongTitle'
        ])
    }

    response_body = [e['SongTitle'] for e in table.query(**query)['Items']]
    return make_response(jsonify(response_body))


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
