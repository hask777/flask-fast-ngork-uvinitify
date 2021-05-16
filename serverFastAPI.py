import os
import datetime
from fastapi import FastAPI
from logger import trigger_log_save
from scrape import scrape_brands
from scrape import dump_json

app = FastAPI()

@app.get("/")
def home_view():
    return {"Home": "page"}

@app.post("/abc")
def get_brands():
    trigger_log_save()
    scrape_brands()
    dump_json()
    return {"data": scrape_brands()}