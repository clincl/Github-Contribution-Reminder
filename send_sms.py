# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests
import json
import config
import datetime

url ='https://github-contributions-api.now.sh/v1/clincl'
#params = {}

response = requests.get(url)
year_range = 0
for i in response.json()['years']:
  year_range += 1
print(year_range)
x=datetime.datetime.now()
print(x)
print(response.url)
con = response.json()['contributions']
for c,i in enumerate(con):
  if c < 4:
    print(con[c]['date'],con[c]['count'])
#print(output)

# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = config.account_sid
# auth_token = config.auth_token
# client = Client(account_sid, auth_token)

# twilio_number = config.twilio_number
# to = config.to
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_ = twilio_number,
#                      to = to
#                  )

# print(message.sid)
