"""
Wrapper APIs. 
"""
from fastapi import APIRouter
from pydantic import BaseModel
import requests
import os
import base64

CLIENT_ID  = os.environ.get("CLIENT_ID")
CLIENT_SECRET  = os.environ.get("CLIENT_SECRET")
TOKEN_URL = "https://dome.the-marketplace.eu//auth/realms/dome4.0/protocol/openid-connect/token"


class CatalogData(BaseModel):
    """
    Pydantic data model for DOME 4.0 catalog datasets.
    """
    dataset: str
    issueDate: str
    license: str
    title: str
    url: str
    dataCreator: str
    dataPublisher: str
    keyword: str


router = APIRouter()


@router.get("/")
async def home():
    """
    API for testing.
    Return a simple "Hello World" message.

    Returns:
        A dictionary with a message key and "Hello World" value.
    """
    return {"msg": "Hello World"}

async def get_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode()).decode()}"
    }
    data = {'grant_type': 'client_credentials' }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return {"error": f"Request failed with status code {response.status_code}"}


@router.post("/fetch-application-output-url")
async def fetch_output_url(dome_catalog_data: CatalogData):
    """
    Receive a POST request from DOME 4.0.
    Return an output url.

    Returns:
        A dictionary with a url key and value.
    """
    # Use dome_catalog_data.url to fetch data from DOME to your application. Use get_token() to fetch the token!
    # Process it and send back an output url (redicert url if you're returning a webpage,
    # download url if you're returning a file).
    
    output_url = "return_url"

    # Return either redirect url or download url, depending on your application.
    return {"url": output_url}
