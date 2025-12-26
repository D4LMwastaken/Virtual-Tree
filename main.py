# main.py
"""
The main file
"""
import os

import requests
from dotenv import load_dotenv
import datetime

load_dotenv()

# Datetime
today = datetime.date.today()
midnight = datetime.time(0,0,0,0)
endOfDay = datetime.time(23,59,59,59)

slack_id = os.getenv("SLACK_ID")
print(slack_id)
startofday = datetime.datetime.combine(today,midnight)
endofday = datetime.datetime.combine(today,endOfDay)


api_url = f"https://hackatime.hackclub.com/api/v1/users/{slack_id}/stats?start_date=${startofday}&end_date=${endofday}"
api_url_all = f"https://hackatime.hackclub.com/api/v1/users/{slack_id}/stats?"

'''
Appears that I use sometime like this: (thanks https://github.com/joysudo/catatime/blob/master/backend/index.js for helping me...)
https://hackatime.hackclub.com/api/v1/users/${slack_id}/stats?start_date=${startofday}&end_date=${endofday}
'''
response = requests.get(api_url)
response_all = requests.get(api_url_all)
print(response.json())
print(response_all.json())