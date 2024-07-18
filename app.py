# Import the libraries we need.
# Flask is the framework we're using to create an API
from flask import Flask, abort
# JSON is a nifty library which allows us to load JSON files into Python dict and vice versa.
# Hint, have a look at the docs for 'json'. We can't send Python dicts back to the server...
# https://docs.python.org/3/library/json.html
from json import load

# Makes sure that our Flask server refers to our file ("app.py")
app = Flask(__name__)

# Load the pokemon.json data into a dict
pf = open("pokemon.json")
pokemon_data = load(pf)

# Load the pokemon_types.json data into a dict
ptf = open("pokemon_types.json")
pokemon_types = load(ptf)


@app.route("/", methods=["GET"])
def pokemon():
    """Add some routing. This is the first thing you'll see!"""
    return "I wanna be the very best, that no one ever was...!"


@app.route("/pokemon", methods=["GET"])
def get_all_pokemon():
    # TODO: return a JSON object of all pokemon.
    return pokemon_data


@app.route("/pokemon/<int:id>", methods=["GET"])
def get_pokemon(id: int):
    return [data for data in pokemon_data if data["id"] == id]


@app.route("/pokemon/<int:id>/types", methods=["GET"])
def get_pokemon_type(id: int):
    return [type["type"] for type in pokemon_types if type["pokemon_id"] == id]


@app.route("/type/<type>", methods=["GET"])
def get_all_pokemon_of_type(type: str):
    if type:
        return [data for data in pokemon_data if type in get_pokemon_type(
            data["pokemon_id"])]
    abort(404)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
