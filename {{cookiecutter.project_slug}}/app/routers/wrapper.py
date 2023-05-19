"""
Wrapper APIs. 
"""
from fastapi import APIRouter
from pydantic import BaseModel

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

@router.post("/fetch-application-output-url")
async def fetch_output_url(dome_catalog_data: CatalogData):
    """
    Receive a POST request from DOME 4.0.
    Return an output url.

    Returns:
        A dictionary with a url key and value.
    """
    # Use dome_catalog_data.url to fetch data from DOME to your application.
    # Process it and send back an output url (redicert url if you're returning a webpage,
    # download url if you're returning a file).

    output_url = "return_url"

    # Return either redirect url or download url, depending on your application.
    return {"url": output_url}
