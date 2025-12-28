# main.py
"""
The main file
"""

import hackatime

# Constants
Version = "V1.0.0"

print("Virtual Tree by D4LM")
print("Version:",Version)
print("Would you like to create a virtual tree for all your time or just for today?")
print("[1] All your time")
print("[2] Today's time")
if input("> ").lower() == "1":
    print("Since you started using HackaTime, you spent", hackatime.get_time_all())
elif input("> ").lower() == "2":
    print("Today you spent", hackatime.get_time_today())