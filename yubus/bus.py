import urllib
import sys

if len(sys.argv) < 2:
    bus = 285
else:
    bus = sys.argv[1]
busapi = "http://pda.5284.com.tw/MQS/businfo2.jsp?routeId="+str(bus)

u = urllib.urlopen(busapi)

data = u.read()

data = data.split()



for i,each in enumerate(data):
    print(each)

            
