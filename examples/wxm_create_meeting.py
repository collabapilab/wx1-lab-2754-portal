"""
Sample python script demonstrating scheduling a meeting using the wxc_sdk 
"""
import logging
from datetime import datetime, timedelta, timezone
from pprint import pformat
from wxc_sdk import WebexSimpleApi

# Set up logging with a default level of INFO
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')
# The logging levels for individual components can be adjusted
logging.getLogger('wxc_sdk.rest').setLevel(logging.DEBUG)
# Create a logging instance
log = logging.getLogger(__name__)

# Replace with your access token
access_token = '___PASTE_YOUR_PERSONAL_ACCESS_TOKEN_HERE___'

# Create an instance of the WebexSimpleApi with your access token
api = WebexSimpleApi(tokens=access_token)

# Create variables for start and end times and meeting title

# Create Meeting using the create meeting API

# Generate the join links for the meeting
