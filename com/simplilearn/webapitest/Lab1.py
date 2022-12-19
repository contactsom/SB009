import unittest
import requests
import json

class myTestCase(unittest.TestCase):
    def test_api_get(self):
        resp=requests.get("https://reqres.in/api/users?page=2")
        assert (resp.status_code==200), "Status Code is not 200 , Rather than :  " +str(resp.status_code)
        for record in resp.json()['data']:
            if record['id']==7:
                assert record['first_name']=="Michael",\
                "First Name not Matched"
                assert record['last_name'] == "Lawson", \
                "Last  Name not Matched"
                assert record['email'] == "michael.lawson@reqres.in", \
                    "Email not Matched"

