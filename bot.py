import requests
import json
from ics import Calendar, Event
import arrow

import sys

from pprint import pprint

with open('config.json', 'r') as f:
	cfg = json.load(f)
	url = cfg['url']
	outFile = cfg['outFile']
	outFile2 = cfg['outFile2']

try:
	req = requests.get(url,verify=False)
	#print(req.text)


	data = json.loads(req.text)

	#fh = open("tmp.txt", "w")
	#fh.write(req.text)
	#fh.write(data.text)
	#json.dump(data, fh)



	#fh = open("tmp.txt", "r")
	#data = json.load(fh)
	#pprint(data)

	cal = Calendar()
	js = []

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

	    #js.append({'start': event['start'].for_json(),'end': event['end'].for_json(),'title': event['description']})
	    js.append({'start': ev.begin.for_json(),'end': ev.end.for_json(),'title': event['title'] + ' - '  + event['room'] })

	#pprint(cal)
	#pprint(cal.events)
	with open(outFile, 'w') as f:
	    f.writelines(cal)

	with open(outFile2, 'w') as f:
	    f.writelines(json.dumps(js))

except:
	print("Unexpected error")
	raise

sys.exit(0)


