"""
Sample OAuth authentication flow using an Integration
"""
import http.server
import json
import logging
import re
import requests
import socketserver
from wxc_sdk import WebexSimpleApi

# Replace with your values from the Integration
client_id = '___PASTE_INTEGRATION_CLIENT_ID___'
client_secret = '___PASTE_INTEGRATION_CLIENT_SECRET___'

# Add the redirect_url and scopes


# Set up logging with a default level of INFO
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
# The logging levels for individual components can be adjusted
# logging.getLogger('wxc_sdk.rest').setLevel(logging.DEBUG)
# Create a logging instance
log = logging.getLogger(__name__)
server_port = 5002
authorization_code = None

def get_access_token(code):
    """
    Retrieves an access token given an authorization code
    """
    log.info(f'Requesting authentication token for authorization code: {code}')
    token = None
    # Gets access token and refresh token
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    payload = f"grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&code={code}" \
              f"&redirect_uri={redirect_url}"
    req = requests.post(url='https://webexapis.com/v1/access_token', data=payload, headers=headers)
    results = json.loads(req.text)
    log.info(json.dumps(results, indent=4))  # Prettier way of printing the response data
    if req.status_code == 200:
        token = results["access_token"]
    return token


class Server(socketserver.TCPServer):

    # Avoid "address already used" error when frequently restarting the script
    allow_reuse_address = True


class RedirectHandler(http.server.BaseHTTPRequestHandler):
    """
    Handle incoming server request to the redirect url
    """

    def do_GET(self):
        """
        Parses an incoming request and sets the authorization code, if found
        """

        global authorization_code

        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write(f"Got the redirect: {self.requestline}".encode("utf-8"))
        authorization_code = re.search('^.*code=([^&$]+)', self.requestline).group(1)


logging.info(f'Starting web server on port {server_port}')
# Start up a simple web server that will terminate when an authorization code received
with Server(("", server_port), RedirectHandler) as httpd:
    while not authorization_code:
        httpd.handle_request()

# Retrieve an access code given the authorization code
access_token = get_access_token(authorization_code)

if access_token:
    api = WebexSimpleApi(tokens=access_token)
    try:
        me = api.people.me()
        log.info(f'Authenticated to Webex as {me.emails[0]}')
    except Exception as e:
        log.info(f'Exception encountered: {e}')
else:
    log.error(f'No access token available')
