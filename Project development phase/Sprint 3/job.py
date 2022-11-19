import requests
import json
import pandas as pd
from json2html import *
url = "https://linkedin-jobs-search.p.rapidapi.com/"

payload = {
	"search_terms": "python programmer",
	"location": "india",
	"page": "1"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "b045b9af95msha8d7c3160785729p1674cdjsnbdf4adbf9868",
	"X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

infoFromJson = json.loads(response.text)
print(json2html.convert(json = infoFromJson))
#data = json.loads(elevations)
df = pd.json_normalize(infoFromJson)
print(df)
