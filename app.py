from flask import Flask
import requests


app = Flask(__name__)


@app.route("/", methods=["GET"])
def chuck_norris_api_details():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>All details from Chuck Norris API: </strong><br>{}".format(response)


@app.route("/categories")
def chuck_norris_api_categories():

    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()

    return "<strong>Categories for Chuck Norris API:</strong><br>{}".format(response)


if __name__ == "__main__":
    app.debug = True
    app.run()
