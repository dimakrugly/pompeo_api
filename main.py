from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set={
        "items":[
            {
                "key": "1",
                "image": "https://i.ibb.co/ynd6C6T/plate.png",
                "title": "Decor plate",
                "price": 65
            },
            {
                "key": "2",
                "image": "https://i.ibb.co/myC51zs/vaseBlue.png",
                "title": "Mint Pottery",
                "price": 65
            },
            {
                "key": "3",
                "image": "https://i.ibb.co/m0dWqMQ/ceramics.png",
                "title": "Set of pottery",
                "price": 125
            },
            {
                "key": "4",
                "image": "https://i.ibb.co/TW4Xk12/vase-Orange.png",
                "title": "Orange ceramic",
                "price": 55
            },
            {
                "key": "5",
                "image": "https://i.ibb.co/4JHR17b/vase-Black.png",
                "title": "Dark bowl",
                "price": 115
            },
            {
                "key": "6",
                "image": "https://i.ibb.co/wMZWNPN/vaseLava.png",
                "title": "Square pottery",
                "price": 115
            }
        ]
    }

    json_dump = json.dumps(data_set)

    return json_dump
