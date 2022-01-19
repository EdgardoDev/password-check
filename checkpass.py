import requests
import hashlib

# Function that request data and give a response.
def api_data_request(character_query):
  # Build the URL to be used on the request.
  url = "https://api.pwnedpasswords.com/range/" + character_query
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f"Error fetching: {res.status_code}, please check the API and try again!")
  return res

# Function that check the pwned API.
def check_pwned_api(password):
  # Hash the password.
  sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
  return sha1password

check_pwned_api("123")