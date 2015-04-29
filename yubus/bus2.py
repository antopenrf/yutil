import urllib
import sys

u = urllib.urlopen("http://tw-bus.appspot.com/json?bus=285&goback=2")

data = u.read()

data = data.split()

data = data[3:]

for i,each in enumerate(data):
    if each.decode("unicode-escape")=='{':
        for j in range(6):
            print(data[i+j+1].decode("unicode-escape"))
        print('\n')
