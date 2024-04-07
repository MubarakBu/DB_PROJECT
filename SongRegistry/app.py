from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_mysqldb import MySQL
from flask import jsonify
import datetime
from config import Config

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
## MySQL configuration 
app.config['MYSQL_HOST'] = app.config['MYSQL_HOST']
app.config['MYSQL_USER'] = app.config['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = app.config['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = app.config['MYSQL_DB']

mysql = MySQL(app)

account_post_args = reqparse.RequestParser()
account_post_args.add_argument("balance", type=float, help="put balance")
account_post_args.add_argument("account_type", type=str, help="put balance")
account_post_args.add_argument("date_opened", type=datetime, help="put balance")
account_post_args.add_argument("account_status", type=str, help="put status")

    
class SongWriters(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM song_writers''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)

    def post(self):

        data = request.json
        user_name = data.get('user_name')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_email = data.get('user_email')
        password = data.get('password')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_writers (username, f_name, l_name, email, pass) 
                       VALUES (%s, %s, %s, %s, %s)''', (user_name, first_name, last_name, user_email, password))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Account created successfully'}, 201


class Songs(Resource):
    # get song title
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM songs''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):
        
        data = request.json
        songTitle = data.get('songTitle')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO songs (song_title) 
                       VALUES (%s)''', (songTitle))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Song Added successfully'}, 201
    

class Album(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM album''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        albumTitle = data.get('albumTitle')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO album (album_title) 
                       VALUES (%s)''', (albumTitle))
        mysql.connection.commit()
        cur.close()

        return {'message': 'album Added successfully'}, 201


class Artist(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM artist''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO artist (first_name, last_name) 
                       VALUES (%s, %s)''', (firstName, lastName))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Artist Added successfully'}, 201
    

class Publisher(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM publisher''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO publisher (first_name, last_name) 
                       VALUES (%s, %s)''', (firstName, lastName))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Publisher Added successfully'}, 201


class Genre(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM genres''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        genreName = data.get('genreName')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO genres (genre_name) 
                       VALUES (%s)''', (genreName))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Genre Added successfully'}, 201
    

class SongGenre(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT s.song_title, g.genre_name FROM songs s
                        JOIN song_genre sg ON s.song_id = sg.fk_song_id
                        JOIN genres g ON sg.fk_genre_id = g.genre_id''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        sognId = data.get('sognId')
        genreId = data.get('genreId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_genre (fk_song_id, fk_genre_id) 
                       VALUES (%s, %s)''', (sognId, genreId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'SongGenre Added successfully'}, 201
    

class SongAlbum(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT s.song_title, a.album_title FROM songs s
                        JOIN song_album sa ON s.song_id = sa.fk_song_id
                        JOIN album a ON sa.fk_album_id = a.album_id''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        sognId = data.get('sognId')
        albumId = data.get('albumId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_album (fk_song_id, fk_album_id) 
                       VALUES (%s, %s)''', (sognId, albumId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'SongAlbum Added successfully'}, 201


class SongPublisher(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT s.song_title, CONCAT(p.first_name, " ", p.last_name) FROM songs s
                        JOIN song_publisher sp ON s.song_id = sp.fk_song_id
                        JOIN publisher p ON sp.fk_publisher_id = p.publisher_id''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        sognId = data.get('sognId')
        publisherId = data.get('publisherId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_publisher (fk_song_id, fk_publisher_id) 
                       VALUES (%s, %s)''', (sognId, publisherId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'SongPublisher Added successfully'}, 201
    

class SongArtist(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT s.song_title, CONCAT(a.first_name, " ", a.last_name) FROM songs s
                        JOIN song_artist sa ON s.song_id = sa.fk_song_id
                        JOIN artist a ON sa.fk_artist_id = a.artist_id''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        sognId = data.get('sognId')
        artistId = data.get('artistId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_artist (fk_song_id, fk_artist_id) 
                       VALUES (%s, %s)''', (sognId, artistId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'SongArtist Added successfully'}, 201


class SongSongwriter(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT sw.username, s.song_title FROM song_writers sw
                        JOIN songwriters_songs ss ON sw.song_writer_id = ss.fk_songwriter_id
                        JOIN songs s ON ss.fk_song_id = s.song_id''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        songwriterId = data.get('songwriterId')
        sognId = data.get('sognId')
        
        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO songwriters_songs (fk_songwriter_id, fk_song_id) 
                       VALUES (%s, %s)''', (songwriterId, sognId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'SongArtist Added successfully'}, 201




api.add_resource(SongWriters, "/songwriter")
api.add_resource(Songs, "/songs")
api.add_resource(Album, "/album")
api.add_resource(Artist, "/artist")
api.add_resource(Publisher, "/publisher")
api.add_resource(Genre, "/genre")
api.add_resource(SongGenre, "/songgenre")
api.add_resource(SongAlbum, "/songalbum")
api.add_resource(SongPublisher, "/songpublisher")
api.add_resource(SongArtist, "/songartist")
api.add_resource(SongSongwriter, "/songsongwriter")


if __name__ == '__main__':
    app.run(debug=True)