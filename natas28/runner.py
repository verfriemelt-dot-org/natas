# -*- coding: UTF-8-*-

import requests
import datetime
import sys
import re
import datetime
import aes
from string import * 

key  = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'
user = 'natas28'
url  = 'http://natas28.natas.labs.overthewire.org'


#cookies are encode like this:
# 123-<username> as hex 

slices = 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKriAqPE2%2B%2BuYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D'.split('%2F')

print slices[1].decode('base64') # cipher?

# decodetext =  base64.b64decode(enc_cipher)
aes = AES.new(key, AES.MODE_CBC, iv)
cipher = aes.decrypt(decodetext)
pad_text = encoder.decode(cipher)
print pad_text

# print 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKg9sQ0V8wVl%2FPPsvF1L%2Fzemi4rXbbzHxmhT3Vnjq2qkEJJuT5N6gkJR5mVucRLNRo%3D'.decode('base64')
# print 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPICkEwAa1566xpyjPIA0fNq25tSHWhU1IzKYEbRozqho3X9UET9Bj0m9rt%2Fc0tByJk%3D'.decode('base64')


# print 'c%2BJ2TdR0Qp8dcjPKriAqPE2%2B%2BuYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq'.decode('base64')

r = requests.Session();
r.auth = (user,key)


# response = r.get(url)
# flag = r.get(url + '/search.php?query=' + ('\x00'*100).encode('base64'))
# flag = r.get(url + '?password=asd&username=natas28' )
# print (flag.headers)
# print (flag.text)

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
