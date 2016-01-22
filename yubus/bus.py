
import sys
import re

if len(sys.argv) < 2:
    bus = 285
else:
    bus = sys.argv[1]
busapi = "http://pda.5284.com.tw/MQS/businfo2.jsp?routeId="+str(bus)

if sys.version_info > (3,):
    import urllib.request
    opener = urllib.request.urlopen
    u = opener(busapi)
    data = u.read().decode('utf-8')
    data = data.split()
else:
    import urllib
    opener = urllib.urlopen
    u = opener(busapi)
    data = u.read()
    data = data.split()





count = 0
first_stop = "none"
for i,each in enumerate(data[130:-10]):
    each = re.sub('<.*>*', '', each)
    each = re.sub('.*>$', '', each)
    each = re.sub('href.*>', '', each)
    each = re.sub('align=cente', '', each)
    each = re.sub('nowrap', '', each)
    each = re.sub('border=0', '', each)
    each = re.sub('style=', '', each)
    each = re.sub('"color.*', '', each)
    each = re.sub('"810.*', '', each)    
    each = re.sub('title=', '', each)            
    if each == 'r' or each == '' or each[0] == '''"''' or each[:3] in ("wid", "val", "cla"):
        pass
    else:
        count += 1

        if count == 2:
            return_bound = each
            pass

        else:
            if each[0] == ">":
                print(each[1:] + '\n')
            else:
                print(each)

            
