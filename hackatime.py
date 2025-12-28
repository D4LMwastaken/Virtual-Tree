# hackatime.py
"""
Makes all the api calls here, maybe I should call it api.py?
"""

import os
import requests
from dotenv import load_dotenv
import datetime


def get_slack_id():
    """
    Returns your Slack ID from the .env file
    """
    load_dotenv()
    return os.getenv("SLACK_ID")

def get_today():
    """
    Returns today's date, I think I might need this if someone decides to run my code for more than 24 hours
    """
    return datetime.date.today()

def get_start_of_day():
    """
    Returns the start of the day
    """
    return datetime.datetime.combine(get_today(), datetime.time(0,0,0,0))

def get_end_of_day():
    """
    Returns the end of the day
    """
    return datetime.datetime.combine(get_today(), datetime.time(23,59,59,59))

def get_time_today():
    """
    Returns the amount of time you spend working on HackClub today
    """
    api_url = f"https://hackatime.hackclub.com/api/v1/users/{get_slack_id()}/stats?start_date={get_start_of_day()}&end_date={get_end_of_day()}"
    response = requests.get(api_url).json()
    return response["data"]["human_readable_total"]

def get_time_all():
    """
    Returns all the time you spent working on HackClub
    """
    api_url_all = f"https://hackatime.hackclub.com/api/v1/users/{get_slack_id()}/stats?"
    response = requests.get(api_url_all).json()
    return response["data"]["human_readable_total"]