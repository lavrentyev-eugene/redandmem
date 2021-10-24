import logging
from fastapi import FastAPI


app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/")
def check_index_page():
    return {"greetings": "Welcome to redandmem"}
