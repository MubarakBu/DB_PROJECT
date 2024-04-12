import requests

BASE_URL = "http://127.0.0.1:5000/"

# Data to be passed in the request body
data = {
    "username": "user1",
    "password": "123456"
}

# Sending a POST request with data in JSON format to the validation endpoint
response = requests.post(BASE_URL + "uservaildate", json=data)

# Print the response content for debugging
print("Response Content:", response.content)

print(response.json()[0])
# Print the response JSON if possible
try:
    print("Response JSON:", response.json())
except ValueError:
    print("Response is not JSON serializable.")