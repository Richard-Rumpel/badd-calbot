import requests
import json
from ics import Calendar, Event
import arrow

import sys

from pprint import pprint

dump = False
#dump = True

debug = False
#debug = True

with open('config.json', 'r') as f:
        cfg = json.load(f)
        url = cfg['url']

        outFileJSON = cfg['outFileJson']
        
        outFileBase = cfg['outFileBase']
        outFileAll = cfg['outFileAll']

        outFileMobAnw = cfg['outFileAnw']
        outFileMobKom = cfg['outFileKom']
        outFileVsit = cfg['outFileVsit']
        outFileEvsa = cfg['outFileEvsa']

try:

        if (debug):
            print("load cal from file ...")
            fh = open("tmp.txt", "r")
            data = json.load(fh)
            #pprint(data)

        else:
            print("download cal ...")
            req = requests.get(url,verify=False)
            #print(req.text)


            data = json.loads(req.text)
            
            if(dump):
                fh = open("tmp.txt", "w")
                fh.write(req.text)
                #fh.write(data.text)
                #json.dump(data, fh)




        calAll = Calendar()
        calBase = Calendar()
        calKom = Calendar()
        calAnw = Calendar()

        calEvs = Calendar()
        calVsi = Calendar()
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

            calAll.events.add(ev)


            if ("3IT-PMA" in ev.description):
                color = "#cf2c08"
                calAnw.events.add(ev)
            elif("3IT-MK" in ev.description):
                color = "#08b4cf"
                calKom.events.add(ev)



            elif("EVSA" in ev.description):
                color = "#08b4cf"
                calEvs.events.add(ev)

            elif("VSIT" in ev.description):
                color = "#08b4cf"
                calVsi.events.add(ev)



            elif("MTIT" in ev.description):
                color = "#cf2c08"
                calEvs.events.add(ev)
            elif("F.Prog." in ev.description):
                color = "#08b4cf"
                calVsi.events.add(ev)

            elif("IT Sicherheit" in ev.description):
                color = "#08b4cf"
                calEvs.events.add(ev)
            elif("VSIT" in ev.description):
                color = "#08b4cf"
                calVsi.events.add(ev)



            else:
                color = "#90cf08" 
                calBase.events.add(ev)

            #js.append({'start': event['start'].for_json(),'end': event['end'].for_json(),'title': event['description']})
            js.append({'start': ev.begin.for_json(),'end': ev.end.for_json(),'title': ("{0} - {1} ({2})".format(event['title'],event['room'],event['instructor'])),'backgroundColor': color })

        #pprint(cal)
        #pprint(cal.events)
        
        with open(outFileBase, 'w') as f:
            f.writelines(calBase)

        with open(outFileMobKom, 'w') as f:
            f.writelines(calKom)

        with open(outFileMobAnw, 'w') as f:
            f.writelines(calAnw)
        
        with open(outFileEvsa, 'w') as f:
            f.writelines(calEvs)

        with open(outFileVsit, 'w') as f:
            f.writelines(calVsi)

        with open(outFileAll, 'w') as f:
            f.writelines(calAll)
        
        with open(outFileJSON, 'w') as f:
            f.writelines(json.dumps(js))

except:
        print("Unexpected error")
        raise

sys.exit(0)


