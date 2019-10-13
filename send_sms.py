# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests
import json
import config
import datetime

def get_message(user):
  message = ""
  url ='https://github-contributions-api.now.sh/v1/' + user
  response = requests.get(url)
  year_range = 0
  # for i in response.json()['years']:
  #   year_range += 1
  # print(year_range)
  # print(response.url)
  contributions = response.json()['contributions']
  date_today = str(datetime.date.today())
  today_flag = False
  streak = 0
  # break if no streak or streak is broken
  for c,i in enumerate(contributions):
    if today_flag: # checks from yesterday and back
      if contributions[c]['count'] != 0:
        streak += 1
      else:
        #return streak
        message += " You're current streak is " + str(streak) + " commits."
        break
    if  date_today == contributions[c]['date']: # look for today's date
      today_flag = True
      if contributions[c]['count'] != 0: # start streak count
        streak += 1
        message = "You commited github today!"
      else: # remind user to commit and check for streak
        message = "You didn't commit to github today!"
        break
  return message
print(get_message("clincl"))
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
