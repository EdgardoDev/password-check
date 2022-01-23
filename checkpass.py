import requests
import hashlib
import sys

# Function that request data and give a response.


def api_data_request(character_query):
    # Build the URL to be used on the request.
    url = "https://api.pwnedpasswords.com/range/" + character_query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, please check the API and try again!")
    return res

# Function that read the response data.


def passwords_crack_count(hashes, hash_checks):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        # Check how many times the password has been hacked.
        if h == hash_checks:
            return count
    return 0

# Function that check the pwned API.


def check_pwned_api(password):
    # Hash the password.
    sha_one_password = hashlib.sha1(
        password.encode("utf-8")).hexdigest().upper()
    # Store the first 5 characters and then store the remaining chars.
    first_five_chars, remaining_chars = sha_one_password[:5], sha_one_password[5:]
    response = api_data_request(first_five_chars)
    return passwords_crack_count(response, remaining_chars)

# This function will receive the arguments given by the user.


def main(args):
    for password in args:
        count = check_pwned_api(password)
        if count:
            print("-------------------------------------------------------------------------------------------------------------")
            print(
                f"The password [ {password} ] was found on internet [ {count} ] times ⚠️  please change your password immediately! 🚨")
            print("-------------------------------------------------------------------------------------------------------------")
        else:
            print(
                "------------------------------------------------------------------------------------")
            print(
                f"The password [ {password} ] was not found on internet! ✅ you can use it safely! 👍")
            print(
                "------------------------------------------------------------------------------------")
    return " Done! 🔐"


# Only run this file if it's the main file been run from the command line.
if __name__ == "__main__":
    # Lastly we call the main function that accepst any number of arguments.
    # Exit the process in case was not exited successfully.
    sys.exit(main(sys.argv[1:]))
