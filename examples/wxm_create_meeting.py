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
access_token = '____REPLACE_WITH_ACCESS_TOKEN______'

# Create an instance of the WebexSimpleApi with your access token
api = WebexSimpleApi(tokens=access_token)

# Create variables for start and end times and meeting title
start_time = datetime.now(timezone.utc).replace(microsecond=0) + timedelta(minutes=5)
end_time = start_time + timedelta(minutes=30)
meeting_title = "Lab Test Meeting"

# Create Meeting using the create meeting API
meeting_response = api.meetings.create(title=meeting_title, start=start_time, end=end_time)
log.info(meeting_response.model_dump_json(indent=4))
log.info(f'Meeting id: {meeting_response.id}')
log.info(f'Meeting Number: {meeting_response.meeting_number}')
log.info(f'Meeting Link: {meeting_response.web_link}')

# Generate the join links for the meeting
join_response = api.meetings.join(meeting_id=meeting_response.id, join_directly=False)
log.info(join_response)
