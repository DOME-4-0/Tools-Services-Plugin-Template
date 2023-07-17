"""
Wrapper APIs. 
"""
from fastapi import APIRouter, Request
from pydantic import BaseModel
from requests_oauthlib import OAuth2Session
from fastapi.responses import RedirectResponse
import os

HOSTNAME = os.environ.get("EXTERNAL_HOST_NAME")
CLIENT_ID  = os.environ.get("CLIENT_ID")
CLIENT_SECRET  = os.environ.get("CLIENT_SECRET ")
CALLBACK_URL = os.environ.get("CALLBACK_URL ")
SCOPES =["openid"]
AUTH_URL = f"{HOSTNAME}/auth/realms/dome4.0/protocol/openid-connect/auth"
TOKEN_URL = f"{HOSTNAME}/auth/realms/dome4.0/protocol/openid-connect/token"
USER_INFO = f"{HOSTNAME}/auth/realms/dome4.0/protocol/openid-connect/userinfo"

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

@router.get("/login")
async def login():
    oauth_session = OAuth2Session(CLIENT_ID, redirect_uri=CALLBACK_URL, scope=SCOPES)
    authorization_url, _ = oauth_session.authorization_url(AUTH_URL)
    return RedirectResponse(authorization_url)

@router.get("/callback")
async def callback(request: Request):
    scope_request = request.query_params.get("scope")
    oauth_session = OAuth2Session(
        CLIENT_ID, redirect_uri=CALLBACK_URL, scope=scope_request
    )
    try:
        oauth_session.fetch_token(
            TOKEN_URL,
            client_secret=CLIENT_SECRET,
            authorization_response=request.url._url,
            scope=scope_request,
            verify=False,
        )
    except Exception:
        return request.query_params.get("error_description")
    user = oauth_session.get(USER_INFO)

    return user.content

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
