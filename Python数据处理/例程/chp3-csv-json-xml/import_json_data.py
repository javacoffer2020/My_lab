import json

json_data = open('../../data/chp3/data-text.json').read()

data = json.loads(json_data)

i=1
for item in data:
     print("Id No.: {:d}".format(i))
     for key in item:
          print("    {:s} : {:s}".format(key,str(item[key])))
     print(" ")
     i += 1