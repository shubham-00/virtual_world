import requests

response = requests.post("url here ...", data={
    'txtUserId': '1',
    'txtPassword': '1',
    '...': '...',   # Data that form collects
})

print("Form submitted")
