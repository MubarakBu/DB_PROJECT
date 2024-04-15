import requests

BASE_URL = "http://127.0.0.1:5000/"
userId = 1
songName = "song2"

# Make a GET request to retrieve the user's songs
response = requests.get(BASE_URL + "getsongid", params={"userId": userId, "songName": songName})

print(type(response.json()[0][0]))
print(response.json()[0][0])
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the songs data from the response
    songs = response.json()
    print("User Songs:", songs)
else:
    print("Failed to retrieve user songs. Status code:", response.status_code)