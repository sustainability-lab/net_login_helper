import requests
from getpass import getpass

# URL to open
login_url = 'https://internet.iitgn.ac.in'
check_url = 'https://www.google.com'

# Create a session object to maintain state
session = requests.Session()

# Get login page to fetch any necessary cookies or tokens
response = session.get(login_url)

# Print response content for debugging if needed
print("Received login page")

# Prepare login data
username = input("Enter Username: ")
password = getpass(prompt='Enter your password: ')
login_data = {
    'LoginUserPassword_auth_username': username,
    'LoginUserPassword_auth_password': password
}

# Send login request
response = session.post(login_url, data=login_data)

# Check if login was successful
if response.ok:
    print("Login script executed")

    # Check if internet is working
    response = session.get(check_url)
    
    if response.ok and "Google" in response.text:
        print("Login Successful")
    else:
        print("Internet check failed")
else:
    print("Login failed")
