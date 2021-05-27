import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config['DEBUG'] = True

data = [{
    "name": "Vikas P",
    "gender": "Male",
    "age": 25
}]


@app.route('/', methods=['GET'])
def home():
    return "<h1>This is my first API</h1><p>Just a try!</p>"


@app.route('/new-page', methods=['GET'])
def new_page():
    return jsonify(data)


@app.route('/add-details', methods= ['POST'])
def add_details():
    request_data = request.get_json()
    for i in data:
        if i['name'] == request_data['name']:
            return jsonify({"message": f"data with name {request_data['name']} already present"})
        else:
            data.append(request_data)
            return jsonify(request_data)


app.run()

