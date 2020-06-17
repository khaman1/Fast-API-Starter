from shared import *

@app.get("/")
def read_root():
    return {"Hello": "World"}