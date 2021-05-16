from flask import Flask
from scrape import scrape_brands
from scrape import dump_json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def av_brands():
    return "Hello"

@app.route("/abc", methods=['POST'])
def av_parse():
    scrape_brands()
    dump_json()
    return "Done"