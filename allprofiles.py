from linkedin import linkedin
from linked.models import linked
from linked.models import search_company
import json
CONSUMER_KEY = '75nanr9qwylt2d'
CONSUMER_SECRET = 'UpORpgoDH1iUl2kL'
USER_TOKEN = '5767f0eb-881b-4d79-ba40-7a191856890c'
USER_SECRET = '2132991c-9e73-4ef1-b83c-9dbb64113b0b'
RETURN_URL = ' http://127.0.0.1:8000/'
auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,USER_TOKEN, USER_SECRET,RETURN_URL,permissions=linkedin.PERMISSIONS.enums
.values())
app = linkedin.LinkedInApplication(auth)
connections = app.get_connections()


# print connections
x = connections('header')
connections = app.get_profile('header')
 connections = app.get_profile('rmRc7zfsQX')
print connections


