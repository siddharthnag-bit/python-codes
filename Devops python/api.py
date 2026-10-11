from fastapi import FastAPI
from system_util import get_system_info

app = FastAPI(title="devops utilities API")


@app.get("/hello")
def hello():
    return {"hello guyx this is siddharth nag"}

@app.get("/cpu")
def cpu():
    return get_system_info()
