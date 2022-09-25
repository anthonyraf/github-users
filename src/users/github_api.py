import requests
import json

response = requests.get('http://country.io/names.json')
COUNTRIES_JSON = {code : country for code, country in sorted(response.json().items(), key=lambda item: item[1])}
COUNTRIES = list(COUNTRIES_JSON.values())


class Users:
    GH_TOKEN = "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"
    def __init__(self, country_target):
        self.country_name = country_target
    
    def get_users(self):
        url = f"https://api.github.com/search/users?q=location:{self.country_target}"
        response = requests.get(url, params={"Authorization": f"Bearer {self.GH_TOKEN}"})
        return  json.dumps(response.json(), indent=4)
    

# anthony = Users("Madagascar")
# print(anthony.get_users())