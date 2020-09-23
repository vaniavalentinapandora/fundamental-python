import requests

print('Hello World!')

try:
    r = requests.get ('https://goog le.com')
    print(r.status_code)
    if r.status_code == 500:
        print(r.text)
except Exception as e:
    print('Ada error', e)