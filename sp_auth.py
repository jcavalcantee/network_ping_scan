from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext
from dotenv import load_dotenv
import os

load_dotenv()

site_url = os.getenv("SHAREPOINT_SITE_URL")
username = os.getenv("SHAREPOINT_USERNAME")
password = os.getenv("SHAREPOINT_PASSWORD")

# Authentication
def get_sharepoint_context():
    ctx_auth = AuthenticationContext(site_url)
    if ctx_auth.acquire_token_for_user(username, password):
        return ClientContext(site_url, ctx_auth)
    else:
        raise Exception("Authentication failed!")

