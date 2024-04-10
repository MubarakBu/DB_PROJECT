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


    
class Users(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM users''')
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
        cur.execute('''INSERT INTO users (username, f_name, l_name, email, pass) 
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
        genreId = data.get('genreId')
        albumId = data.get('albumId')
        publisherId = data.get('publisherId')
        userId = data.get('userId')
        labelId = data.get('labelId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO songs (song_title, fk_genre_id, fk_album_id, fk_publisher_id, fk_user_id, fk_label_id) 
                       VALUES (%s, %s, %s, %s, %s)''', (songTitle, genreId, albumId, publisherId, userId, labelId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Song Added successfully'}, 201


class SongMetadata(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM song_metadata''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        releaseDate = data.get('releaseDate')
        duration = data.get('duration')
        songLanguage = data.get('songLanguage')
        songId = data.get('songId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_metadata (release_date, duration, song_language, fk_song_id) 
                       VALUES (%s, %s)''', (releaseDate, duration, songLanguage, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'album Added successfully'}, 201


class Albums(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM albums''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        albumTitle = data.get('albumTitle')
        releaseDate = data.get('releaseDate')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO albums (album_title, release_date) 
                       VALUES (%s, %s)''', (albumTitle, releaseDate))
        mysql.connection.commit()
        cur.close()

        return {'message': 'album Added successfully'}, 201


class Artists(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM artists''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO artists (first_name, last_name) 
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


class AlbumArtists(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT b.album_title, CONCAT(a.first_name, " ", a.last_name) FROM albums b
                    JOIN album_artist aa ON b.album_id = aa.fk_album_id
                    JOIN artists a ON aa.fk_artist_id = a.artist_id''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        albumId = data.get('albumId')
        artistId = data.get('artistId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO album_artist (fk_album_id, fk_artist_id) 
                       VALUES (%s, %s)''', (albumId, artistId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'AlbumArtists Added successfully'}, 201


class Copyright(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM copyright''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        songId = data.get('songId')
        copyrightHolder = data.get('copyrightHolder')
        registrationDate = data.get('registrationDate')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO copyright (fk_song_id, copyright_holder, registration_data) 
                       VALUES (%s, %s, %s)''', (songId, copyrightHolder, registrationDate))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Copyright Added successfully'}, 201


class Label(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM label''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        labelName = data.get('labelName')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO label (label_name) 
                       VALUES (%s)''', (labelName))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Label Added successfully'}, 201


class Registrations(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM registrations''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        songId = data.get('songId')
        registration_date = data.get('registration_date')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO registrations (fk_song_id, registration_date) 
                       VALUES (%s, %s)''', (songId, registration_date))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Registration Added successfully'}, 201


class Payments(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM payments''')
        data = cur.fetchall()
        cur.close
        return jsonify(data)
    
    def post(self):

        data = request.json
        amount = data.get('amount')
        paymentMethod = data.get('paymentMethod')
        paymentDate = data.get('paymentDate')
        songId = data.get('songId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO label (amount, payment_method, payment_date, song_id) 
                       VALUES (%s)''', (amount, paymentMethod, paymentDate, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Label Added successfully'}, 201




api.add_resource(Users, "/users")
api.add_resource(Songs, "/songs")
api.add_resource(Albums, "/album")
api.add_resource(Artists, "/artist")
api.add_resource(Publisher, "/publisher")
api.add_resource(Genre, "/genre")
api.add_resource(SongArtist, "/songartist")
api.add_resource(AlbumArtists, "/albumartists")
api.add_resource(Copyright, "/copyright")
api.add_resource(Label, "/label")
api.add_resource(Registrations, "/registrations")
api.add_resource(Payments, "/payments")
api.add_resource(SongMetadata, "/songmetadata")


if __name__ == '__main__':
    app.run(debug=True)