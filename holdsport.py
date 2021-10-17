import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_url = "https://api.holdsport.dk/v1/teams"

response = requests.get(api_url, auth = (os.environ.get("HS_USER"), os.environ.get("HS_PWD")))
user = os.environ.get("HS_USER")
pwd = os.environ.get("HS_PWD")

#response = requests.get(api_url, auth = (user, pwd))
response_json  = response.json()
#print(json.dumps(response_json, indent=4))

print(response_json[1]["id"])


