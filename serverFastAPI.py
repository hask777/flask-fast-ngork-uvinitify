from fastapi import FastAPI
from scrape import scrape_brands
from scrape import dump_json

app = FastAPI()

@app.get("/")
def home_view():
    return {"Home": "page"}

@app.post("/abc")
def get_brands():
    scrape_brands()
    dump_json()
    return {"data": scrape_brands()}