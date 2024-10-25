import requests
import json
import datetime

# https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m,precipitation&forecast_days=1

r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m,precipitation&forecast_days=1')
data = r.json()

# {"latitude":51.5,"longitude":-0.120000124,"generationtime_ms":0.032067298889160156,"utc_offset_seconds":0,"timezone":"GMT","timezone_abbreviation":"GMT","elevation":23.0,"hourly_units":{"time":"iso8601","temperature_2m":"°C","precipitation":"mm"},"hourly":{"time":["2024-10-25T00:00","2024-10-25T01:00","2024-10-25T02:00","2024-10-25T03:00","2024-10-25T04:00","2024-10-25T05:00","2024-10-25T06:00","2024-10-25T07:00","2024-10-25T08:00","2024-10-25T09:00","2024-10-25T10:00","2024-10-25T11:00","2024-10-25T12:00","2024-10-25T13:00","2024-10-25T14:00","2024-10-25T15:00","2024-10-25T16:00","2024-10-25T17:00","2024-10-25T18:00","2024-10-25T19:00","2024-10-25T20:00","2024-10-25T21:00","2024-10-25T22:00","2024-10-25T23:00"],"temperature_2m":[12.2,12.1,12.0,12.2,12.0,11.9,12.5,12.9,13.6,14.3,15.3,16.4,16.8,16.4,16.5,16.3,15.3,14.9,14.6,14.1,13.5,13.1,12.5,12.2],"precipitation":[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]}}

# place into file as:
"""
{
	"data": {
		"times": [
		"2024-10-25T00:00",...]

		"temperature": [29...]
		"precipitation": [0.00...]
	}
}
"""

def create_file():
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
