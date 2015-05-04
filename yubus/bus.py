import urllib
import sys
import re

if len(sys.argv) < 2:
    bus = 285
else:
    bus = sys.argv[1]
busapi = "http://pda.5284.com.tw/MQS/businfo2.jsp?routeId="+str(bus)

u = urllib.urlopen(busapi)

data = u.read()

data = data.split()



for i,each in enumerate(data[:-10]):
    each = re.sub(r'<.*>*', '', each)
    each = re.sub(r'.*>$', '', each)
    each = re.sub(r'href.*>', '', each)
    each = re.sub(r'align.*', '', each)
    each = re.sub(r'nowrap>', '', each)
    each = re.sub(r'border=0', '', each)
    each = re.sub(r'style=', '', each)
    each = re.sub(r'"color.*', '', each)
    each = re.sub(r'"810.*', '', each)    
    each = re.sub(r'title=', '', each)            
    print(each)

            
