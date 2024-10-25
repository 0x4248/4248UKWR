import requests
import json
import datetime
import os

r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m,precipitation&forecast_days=1')
data = r.json()


def create_file():
	os.mkdir('data')
	contents  = {
		"data": {
			"times": data['hourly']['time'],
			"temperature": data['hourly']['temperature_2m'],
			"precipitation": data['hourly']['precipitation']
		}
	}

	with open('data/2024-OCT-NOV-CB-temp-precip.json', 'w') as f:
		json.dump(contents, f)
	
	exit(0)


try:
	f = open('data/2024-OCT-NOV-CB-temp-precip.json', 'r')
	contents = json.load(f)
	f.close()
except Exception as e:
	create_file()

for i in range(len(data['hourly']['time'])):
	contents['data']['times'].append(data['hourly']['time'][i])
	contents['data']['temperature'].append(data['hourly']['temperature_2m'][i])
	contents['data']['precipitation'].append(data['hourly']['precipitation'][i])

f = open('data/2024-OCT-NOV-CB-temp-precip.json', 'w')
json.dump(contents, f)
f.close()
