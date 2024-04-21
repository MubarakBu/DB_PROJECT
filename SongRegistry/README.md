

# Flask-RESTful MySQL Backend

This project uses Flask-RESTful and MySQL to create a backend with endpoints for interacting with a MySQL database. The following API endpoints are implemented to perform CRUD (Create, Read, Update, Delete) operations on user songs, user information, and song details.

## Configuration

Before running the backend, ensure you have the following MySQL configuration parameters set in your Flask application:

```python
app.config.from_object(Config)
# MySQL configuration
app.config['MYSQL_HOST'] = app.config['MYSQL_HOST']
app.config['MYSQL_USER'] = app.config['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = app.config['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = app.config['MYSQL_DB']
```

These configurations connect your Flask application to the MySQL database.

## API Endpoints

The backend defines four RESTful API endpoints, each represented by a class. These endpoints support GET, POST, PUT, and DELETE methods to interact with the MySQL database.

### 1. Get User Songs (GET)

This endpoint retrieves a list of songs associated with a specific user. It requires a `username` as a query parameter and returns song information in JSON format.

```python
from flask_restful import Resource, request
from flask import jsonify
from flask_mysqldb import MySQL

class GetUserSongs(Resource):
    def get(self):
        username = request.args.get('username')
        
        cur = mysql.connection.cursor()
        cur.execute('''
            SELECT s.song_id, s.song_title, CONCAT(a.first_name, " ", a.last_name),
                   ab.album_title, g.genre_name 
            FROM songs s
            JOIN users u ON s.fk_user_id = u.user_id
            JOIN song_artist sa ON s.song_id = sa.fk_song_id
            JOIN artists a ON sa.fk_artist_id = a.artist_id
            JOIN albums ab ON s.fk_album_id = ab.album_id
            JOIN genres g ON s.fk_genre_id = g.genre_id
            WHERE u.username = %s
        ''', (username,))
        data = cur.fetchall()
        cur.close()

        return jsonify(data)
```

### 2. Insert New User (POST)

This endpoint creates a new user by inserting user data into the `users` table. It requires user information in the JSON body and returns a success message if the insertion is successful.

```python
class Users(Resource):
    def post(self):
        data = request.json
        user_name = data.get('user_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_email = data.get('user_email')
        password = data.get('password')

        cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO users (username, f_name, l_name, email, pass) 
            VALUES (%s, %s, %s, %s, %s)
        ''', (user_name, first_name, last_name, user_email, password))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Account created successfully'}, 201
```

### 3. Update Song Genre (PUT)

This endpoint updates the genre of a specific song in the `songs` table. It requires a `songId` and `genreId` in the JSON request body, returning a success message upon successful completion.

```python
class updateSongGenre(Resource):
    def put(self):
        data = request.json
        songId = data.get('songId')
        genreId = data.get('genreId')

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE songs SET fk_genre_id = %s WHERE song_id = %s''', (genreId, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Song genre updated successfully'}, 200
```

### 4. Delete Song (DELETE)

This endpoint deletes a song and its associated song-artist relationships. It requires a `songId` query parameter to identify the song to delete. If the deletion is successful, it commits the transaction and returns a success message.

```python
class deleteSong(Resource):
    def delete(self):
        songId = request.args.get('songId')

        cur = mysql.connection.cursor()
        cur.execute(
            '''DELETE FROM song_artist WHERE fk_song_id = %s''', (songId,))
        cur.execute('''DELETE FROM songs WHERE song_id = %s''', (songId,))
        mysql.connection.commit()
        cur.close()

        return {'message': f'Song with ID {songId} deleted successfully'}, 200
```

# Flask Frontend

Here's the documentation that demonstrates how the frontend interacts with the Flask-RESTful backend using HTTP requests. 


# Flask-RESTful Frontend Interaction

This example demonstrates how the frontend uses HTTP requests to interact with the backend API endpoints implemented with Flask-RESTful. The backend uses MySQL to perform CRUD (Create, Read, Update, Delete) operations on data such as user songs, user information, and song details.

### API Base URL
The base URL for the Flask-RESTful backend is: `http://127.0.0.1:5000/`

### Example: Retrieve User Songs (GET)
The frontend retrieves the songs associated with a specific user by sending a GET request to the `getusersongs` endpoint, passing the `username` as a query parameter.

```python
import requests

BASE = "http://127.0.0.1:5000/"

username = "exampleUser"
getusersongs = requests.get(BASE + "getusersongs", params={"username": username})

# Convert the response to JSON
songs = getusersongs.json()

print(songs)
```