import requests
import json
from ics import Calendar, Event

import sys

from pprint import pprint

with open('config.json', 'r') as f:
	cfg = json.load(f)
	url = cfg['url']
	outFile = cfg['outFile']

try:
	req = requests.get(url,verify=False)
	#print(req.text)


	data = json.loads(req.text)

	#fh = open("tmp.txt", "w")
	#fh.write(data.text)
	#json.dump(data, fh)



	#fh = open("tmp.txt", "r")
	#data = json.load(fh)
	#pprint(data)

	cal = Calendar()

	for event in data:
	    #pprint(event)
	    ev = Event()
	    ev.name = event['description']
	    ev.begin = event['start']
	    ev.end = event['end']
	    ev.location = event['room']

	    des = event['instructor'] + ' ' + event['title']
	    ev.description = des

	    cal.events.add(ev)


	#pprint(cal)
	#pprint(cal.events)
	with open(outFile, 'w') as f:
	    f.writelines(cal)
except:
	print("Unexpected error")
	raise

sys.exit(0)


