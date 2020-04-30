from datetime import date

import requests


def get_today():
    return date.today()


def myfunc_using_date():
    print("do something")
    day = get_today()
    print("do something else")
    return day


def call_external_api():
    response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Rome")
    data = response.json()
    currenttime = data.get("datetime")
    return currenttime
