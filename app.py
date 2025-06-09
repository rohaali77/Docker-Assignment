from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/recipe")
def get_recipe():
    recipe = {
        "name": "Grilled Cheese Sandwich",
        "ingredients": ["bread", "cheese", "butter"]
    }
    return jsonify(recipe)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)