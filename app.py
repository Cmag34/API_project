import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
data = response_API.text


parse_json = json.loads(data)


active_case = parse_json['Andhra Pradesh']['districtData']['East Godavari']['active']
# active_case2 = parse_json['Andaman and Nicobar Islands']['districtData']['Jaluan']['active']

print(parse_json)
print("\n\n\n\n\n")
print("Active cases in South Andaman:", active_case)