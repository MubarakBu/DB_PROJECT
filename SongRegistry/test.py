import requests

BASE = "http://127.0.0.1:5000/"

# Data to be passed in the request body
data = {
    "sognId": 1,
    "songwriterId": 1
}

# Sending a POST request with data in JSON format
response = requests.post(BASE + "songsongwriter", json=data)

# Print the response content for debugging
print("Response Content:", response.content)

# Print the response JSON if possible
try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Error decoding JSON:", e)