from typing import Optional
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/freeusers_view")
def read_item(access_token: str):

    headers = {"Authorization": "Bearer " + access_token}
    result = requests.get(
        "https://api.airtable.com/v0/app61I7CwlK0gHEIX/jobs?maxRecords=50&sort%5B0%5D%5Bfield%5D=creation_date&sort%5B0%5D%5Bdirection%5D=desc&view=Free%20users%20view&fields=Name,company,location,remote_string,days_ago_text",
        headers=headers,
    )
    return result.json()
    ## please add bearer token to the request
