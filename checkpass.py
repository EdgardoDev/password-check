import requests

# Build the URL to be used on the request.
url = "https://api.pwnedpasswords.com/range/" + "AA95E"
res = requests.get(url)

print(res)