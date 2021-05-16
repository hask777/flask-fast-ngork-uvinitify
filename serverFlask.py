from flask import Flask
from scrape import scrape_brands

app = Flask(__name__)

@app.route("/", methods=['GET'])
def av_brands():
    scrape_brands()
    return "Done"

@app.route("/abc", methods=['GET'])
def abc_view():
    return "Hello world ABC"