import requests

with requests.head("https://c3.ttcache.com/thumbnail/CBxxZnJgSGp/288x162/2.jpg") as response:
    print(response.status_code)
    if response.status_code == 200:
        print(response.headers)