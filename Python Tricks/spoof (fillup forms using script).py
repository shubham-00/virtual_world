import requests
import os
from random import randint
import string
import json

form_id = 113
timestamp = 1587137943

url = "http://thechattercourt.com/register/"

for i in range(10):
    form_id += 1
    timestamp += 10235


    name = ''
    text = ["script"] + [chr(randint(65, 90)) for i in range(10)]
    for i in text:
        name += i
    print(name)

    password = ""
    text = ["aA1"] + [chr(randint(0, 127)) for i in range(25)]
    for i in text:
        if i != ' ' or i != '\n' or i != '\t' or i != "\\":
            password += i.strip()
    print(password)    

    requests.post(url, allow_redirects=False, data={
        'user_login-111': name,
        'first_name-111': name,
        'last_name-111': name[::-1],
        'user_email-111': name + "@gmail.com",
        'user_password-111': password,
        'confirm_user_password-111': password,
        'form_id': form_id,
        'timestamp': timestamp,
        '_wpnonce': '9582aa357a',
        '_wp_http_referer': '/register/',
    })



'''


'''