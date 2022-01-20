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

# Function that read the response data.
def passwords_crack_count(hashes, hash_checks):
  hashes = (line.split(":") for line in hashes.text.splitlines())
  for h, count in hashes:
    print(h, count)

# Function that check the pwned API.
def check_pwned_api(password):
  # Hash the password.
  sha_one_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
  # Store the first 5 characters and then store the remaining chars.
  first_five_chars, remaining_chars = sha_one_password[:5], sha_one_password[5:]
  response = api_data_request(first_five_chars)
  print(response)
  
  return passwords_crack_count(response, remaining_chars)

check_pwned_api("123")