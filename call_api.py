#!/usr/bin/env python3
import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
defaultConfig = config['DEFAULT']
api_key = str(defaultConfig['api_key'])
#url = "https://api.playbattlegrounds.com/shards/pc-na/matches/276f5bcb-a831-4e8c-a610-d2073692069e"
#url = "https://api.playbattlegrounds.com/shards/pc-na/players?filter[playerNames]=Dennis_Quaid_419"
url = "https://api.playbattlegrounds.com/shards/pc-na/matches/0ff52157-03ff-4e03-9bb9-2bed0f8176bc"

header = {
        "Authorization": api_key,
        "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
json_response = json.loads(r.text)
participants = []
for i in json_response['included']:
    if i['type'] == "participant":
        if i['attributes']['stats']['name'] == "Dennis_Quaid_419":
            participants.append(i)
for i in json_response['included']:
    if i['type'] == 'roster':
        print (json.dumps(i['attributes']))
print (json.dumps(participants, indent=4))
