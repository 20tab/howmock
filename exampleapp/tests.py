from datetime import date
from unittest.mock import patch

from django.test import TestCase

from exampleapp.functions import call_external_api, myfunc_using_date


def mocked_today():
    return date(year=2020, month=1, day=1)


class TestImmutableObject(TestCase):
    @patch("exampleapp.functions.get_today", mocked_today)
    def test_myfunc_using_date(self):
        self.assertEqual(myfunc_using_date().strftime("%Y-%m-%d"), "2020-01-01")


class MockResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return {
            "week_number": 18,
            "utc_offset": "+02:00",
            "utc_datetime": "2020-04-30T10:48:54.398875+00:00",
            "unixtime": 1588243734,
            "timezone": "Europe/Rome",
            "raw_offset": 3600,
            "dst_until": "2020-10-25T01:00:00+00:00",
            "dst_offset": 3600,
            "dst_from": "2020-03-29T01:00:00+00:00",
            "dst": True,
            "day_of_year": 121,
            "day_of_week": 4,
            "datetime": "2020-04-30T12:48:54.398875+02:00",
            "client_ip": "91.252.18.0",
            "abbreviation": "CEST",
        }


class TestExternalAPI(TestCase):
    @patch("requests.get", return_value=MockResponse())
    def test_call_external_api(self, mocked):
        self.assertEqual(call_external_api(), "2020-04-30T12:48:54.398875+02:00")
