"""Working with API's"""

import requests
import json
import time as t 
from datetime import datetime



count = 0

def welcome(count):
	while count != 3:
		t.sleep(0)
		print("...LOADING SPACE STATS...")
		count += 1
		t.sleep(1)

welcome(count)


parameters = {
    "lat": 40.71,
    "lon": -74
}


response_one = requests.get("http://api.open-notify.org/astros.json")
response_two = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)


def print_response_one(obj):
		#create a formatted string of the python JSON object
		text = json.dumps(obj, sort_keys=True, indent=4)
		print(text)
t.sleep(2)	
print_response_one(response_one.json())
print("----------")



def print_response_two(obj):
		#create a formatted string of the python JSON object
		text = json.dumps(obj, sort_keys=True, indent=4)
		print(text)
t.sleep(2)	
print_response_two(response_two.json())
print("----------")


pass_times = response_two.json()['response']
print_response_two(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)
print("----------")


times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
    print("----------")




"""toggle = "Off"

while toggle == "On":
	def jsonprint(obj):
		#create a formatted string of the python JSON object
		text = json.dumps(obj, sort_keys=True, indent=4)
		print(text)
	t.sleep(2)		
	jsonprint(response_one.json())"""


