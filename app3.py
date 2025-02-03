#pip install flask

# import flask as fl
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


businesses = [

    {
        "id": 1,
        "name": "Sam's",
        "town": "London",
        "rating": 4,
        "review": []


    },

    {
        "id": 2,
        "name": "Pizza Hub",
        "town": "Camden",
        "rating": 3,
        "review": []


    },

    {
        "id": 3,
        "name": "Dominos",
        "town": "London",
        "rating": 4,
        "review": []
    },

]



@app.route('/', methods = ['Get'])
def home():
    return jsonify({"message":"Welcome to Flask API"})


@app.route('/business', methods=['GET'])
def get_business():
    return make_response(jsonify({"businesses":businesses}))

@app.route('/business', methods={'POST'})
def add_business():

    data = request.form
    id = businesses[-1]["id"] + 1
    new_business = {
        "name": data.get("name"),
        "town": data.get("town"),
        "rating": data.get("rating", 0),
        "review": []

    }

    businesses.append(new_business)
    return make_response(jsonify(new_business), 200)

@app.route('/business/<int:id>', methods=['PUT'])
def update_business(id):
    data = request.form
    for business in businesses:
        if business["id"] == id:
            business["name"] = data.get("name")
            business["town"] = data.get("town")
            business["rating"] = data.get("rating")
            break
    return make_response(jsonify(business), 200)

if __name__== '__main__':
    app.run(debug=True)