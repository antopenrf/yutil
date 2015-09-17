#!/usr/bin/python
import urllib
import sys


if len(sys.argv) in [2,3,4]:
    a_url = urllib.URLopener()

    if len(sys.argv) == 2:
        filename = './temp.' + sys.argv[1][-3:]
    elif len(sys.argv) == 3:
        filename = './' + sys.argv[2]
    else:
        filename = sys.argv[3] + sys.argv[2]
        
    a_url.retrieve(sys.argv[1], filename)
else:
    print("\nUsage: python getit.py url_in_quotes file_name_in_quotes path_in_quotes")
    print("Note: if no filename is given.  Default filename is temp.")
    print("Note: if no path is given.  Defaul path is ./ .\n")
          


