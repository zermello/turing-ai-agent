import datetime as dt
from zoneinfo import ZoneInfo
import logging

def get_time(location):
    try:
     today = dt.datetime.now(ZoneInfo(location))
     return today
    except Exception as err:
       logging.error(f"Error: {err}")
       return f"Invalid timezone/location. Please provide a valid timezone."

    