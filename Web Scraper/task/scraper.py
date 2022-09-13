import requests

print("Input the URL:")
url = input()
# http://api.quotable.io/quotes/-4WQ_JwFWI
response = requests.get(url)
print()
try:
    if response.status_code == 200:
        j = response.json()
        print(j['content'])
    else:
        print("Invalid quote resource!")
except KeyError:
    print("Invalid quote resource!")