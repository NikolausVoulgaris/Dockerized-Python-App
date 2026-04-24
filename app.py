from flask import Flask
from os import walk
from data.xml2json import xml2json


app = Flask(__name__)

per_page = 50


@app.route("/")
def home():
    return {"message": "Docker CI/CD App running"}


@app.route("/health")
def health():
    filenames = next(walk('data/'), (None, None, []))[2]
    return {"datafiles": filenames,
            "status": "ok"}


@app.route("/data")
def data():
    return xml2json(1, 10)


@app.route("/data/<page>")
def data_paginate(page):
    first = ((int(page) - 1) * per_page) + 1
    return xml2json(first, per_page)


@app.route("/data/v<list_v>")
@app.route("/data/v<list_v>/<page>")
def data_edition(list_v, page=None):
    if not page:
        return xml2json(1, 10, src=list_v)
    first = ((int(page) - 1) * per_page) + 1
    return xml2json(first, per_page, src=list_v)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
