
from flask import Flask, jsonify, redirect, request
import copy
app = Flask("__name__")

testy = {
    #SQL Verbinung integrieren
    "1": {
        "Name": "Name 1",
        "Verkäufer": "Otto",
        "Verkäufe im letzten Monat": "Graph 1",
        "text": "Auswertung 1",
    },
    "2": {
        "Name": "Name 1",
        "Verkäufer": "Otto",
        "Verkäufe im letzten Monat": "Graph 1",
        "text": "Auswertung 1",
    },
    "3  ": {
            "Name": "Name 1",
            "Verkäufer": "Otto",
            "Verkäufe im letzten Monat": "Graph 1",
            "text": "Auswertung 1",
    },
}

@app.route("/getdata/<id>", methods=["GET"])
def provideInfo(id):
    test = copy.deepcopy(testy["1"])
    print(id)
    return jsonify(test)


@app.route("/getdata", methods=["POST"])
def test():
    data = request.data.decode("utf-8")
    print(data)
    return jsonify(2), 200




if __name__ == "__main__":
    app.run(port=3187)