# Download the helper library from https://www.twilio.com/docs/python/install
from dotenv import load_dotenv
import os
from twilio.rest import Client
load_dotenv()
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

messages = client.messages.list(limit=20)

for record in messages:
    print(record.body)
