from flask import Flask, request, jsonify

app = Flask(__name__)

healthy_ingredients = ["bread", "olive oil", "lettuce", "tomato", "cheese"]

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    ingredients = data.get("ingredients", [])
    analysis = []

    for item in ingredients:
        status = "Healthy" if item in healthy_ingredients else "Unhealthy"
        analysis.append({"ingredient": item, "status": status})

    return jsonify(analysis)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)