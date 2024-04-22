from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_mysqldb import MySQL
from flask import jsonify
from datetime import timedelta
from config import Config

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
# MySQL configuration
app.config['MYSQL_HOST'] = app.config['MYSQL_HOST']
app.config['MYSQL_USER'] = app.config['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = app.config['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = app.config['MYSQL_DB']

mysql = MySQL(app)


class getUserId(Resource):
    def get(self):
        username = request.args.get('username')

        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT user_id FROM users WHERE username = %s', (username,))
        user = cur.fetchall()
        cur.close()

        return jsonify(user)


class UserVaildate(Resource):
    def post(self):
        data = request.json

        username = data.get('username')
        password = data.get('password')

        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM users WHERE username = %s AND pass = %s', (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            return {'message': 'User authenticated successfully'}, 200
        else:
            return {'error': 'Invalid username or password'}, 401


class GetUserSongs(Resource):
    def get(self):
        userId = request.args.get('userId')

        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM dashboard_view WHERE user_id = %s''', (userId,))
        data = cur.fetchall()
        cur.close()

        return jsonify(data)


class SongProfileView(Resource):
    def get(self):
        songId = request.args.get('songId')

        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM songprofile_view WHERE song_id = %s''', (songId,))
        data = cur.fetchall()
        cur.close()

        formatted_data = []
        for row in data:
            formatted_row = list(row)
            # Convert timedelta to string
            formatted_row[7] = str(formatted_row[7])
            formatted_data.append(formatted_row)

        return jsonify(formatted_data)

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
        songId = request.args.get('songId')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT s.song_title, CONCAT(a.first_name, " ", a.last_name), ab.album_title, g.genre_name, l.label_name 
                    FROM songs s JOIN song_artist sa ON s.song_id = sa.fk_song_id
                    JOIN artists a ON fk_artist_id = a.artist_id
                    JOIN albums ab ON s.fk_album_id = ab.album_id
                    JOIN genres g ON s.fk_genre_id = g.genre_id
                    JOIN label l ON fk_label_id = l.label_id
                    WHERE song_id = %s''', (songId,))
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
                       VALUES (%s, %s, %s, %s, %s, %s)''', (songTitle, genreId, albumId, publisherId, userId, labelId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Song Added successfully'}, 201


class SongMetadata(Resource):
    def get(self):
        songId = request.args.get('songId')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT DATE_FORMAT(release_date, '%%Y-%%m-%%d') as release_date, duration, song_language 
                    FROM song_metadata WHERE fk_song_id = %s''', (songId,))
        data = cur.fetchall()
        cur.close

        formatted_data = []
        for row in data:
            formatted_row = list(row)
            # Convert timedelta to string
            formatted_row[1] = str(formatted_row[1])
            formatted_data.append(formatted_row)

        return jsonify(formatted_data)

    def post(self):

        data = request.json
        releaseDate = data.get('releaseDate')
        duration = data.get('duration')
        songLanguage = data.get('songLanguage')
        songId = data.get('songId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO song_metadata (release_date, duration, song_language, fk_song_id) 
                       VALUES (%s, %s, %s, %s)''', (releaseDate, duration, songLanguage, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Metadata Added successfully'}, 201


class Albums(Resource):
    def get(self):
        userId = request.args.get('userId')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM albums WHERE user_id = %s''', (userId,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)

    def post(self):

        data = request.json
        albumTitle = data.get('albumTitle')
        releaseDate = data.get('releaseDate')
        userId = data.get('userId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO albums (album_title, release_date, user_id) 
                       VALUES (%s, %s, %s)''', (albumTitle, releaseDate, userId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'album Added successfully'}, 201


class Artists(Resource):
    def get(self):
        userId = request.args.get('userId')
        cur = mysql.connection.cursor()
        cur.execute(
            '''SELECT * FROM artists WHERE fk_user_id = %s''', (userId,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)

    def post(self):

        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        userId = data.get('userId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO artists (first_name, last_name, fk_user_id) 
                       VALUES (%s, %s, %s)''', (firstName, lastName, userId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Artist Added successfully'}, 201


class Publisher(Resource):
    def get(self):
        userId = request.args.get('userId')
        cur = mysql.connection.cursor()
        cur.execute(
            '''SELECT * FROM publisher WHERE fk_user_id = %s''', (userId,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)

    def post(self):

        data = request.json
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        userId = data.get('userId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO publisher (first_name, last_name, fk_user_id) 
                       VALUES (%s, %s, %s)''', (firstName, lastName, userId))
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


class Copyright(Resource):
    def get(self):
        songId = request.args.get('songId')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM copyright WHERE fk_song_id = %s''', (songId,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)



class Label(Resource):
    def get(self):
        userId = request.args.get('userId')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM label WHERE fk_user_id = %s''', (userId,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)

    def post(self):
        data = request.json
        labelName = data.get('labelName')
        userId = data.get('userId')

        # Insert data into the database
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO label (label_name, fk_user_id) 
                       VALUES (%s, %s)''', (labelName, userId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Label Added successfully'}, 200


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

        return {'message': 'Registration Added successfully'}, 200


class Payments(Resource):
    def get(self):
        song_id = request.args.get('song_id')
        cur = mysql.connection.cursor()
        cur.execute(
            '''SELECT * FROM payments WHERE song_id = %s''', (song_id,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)

    def post(self):
        data = request.json
        amount = data.get('amount')
        songId = data.get('songId')
        payment_method = data.get('payment_method')
        # payment_date = data.get('payment_date')
        # Insert data into the payment table
        cur = mysql.connection.cursor()
        cur.execute('''CALL InsertPaymentThenRegister(%s,%s,%s)''',
                    (amount, payment_method, songId))
        # mysql.connection.commit()
        cur.close()

        return {'message': 'Payment successfully made'}, 200


class getSongId(Resource):
    def get(self):
        userId = request.args.get('userId')
        songName = request.args.get('songName')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT song_id FROM songs 
                    WHERE fk_user_id = %s AND song_title = %s''', (userId, songName,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)


class getAlbumId(Resource):
    def get(self):
        userId = request.args.get('userId')
        albumName = request.args.get('albumName')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT album_id FROM albums 
                    WHERE user_id = %s AND album_title = %s''', (userId, albumName,))
        data = cur.fetchall()
        cur.close
        return jsonify(data)


class updateSongTitle(Resource):
    def put(self):
        data = request.json
        songId = data.get('songId')
        songTitle = data.get('songTitle')

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE songs SET song_title = %s WHERE song_id = %s''', (songTitle, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Song title updated successfully'}, 200


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


class updateReleaseDate(Resource):
    def put(self):
        data = request.json
        songId = data.get('songId')
        releaseDate = data.get('releaseDate')

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE song_metadata SET release_date = %s WHERE fk_song_id = %s''', (releaseDate, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Release date updated successfully'}, 200


class updateSongLabel(Resource):
    def put(self):
        data = request.json
        songId = data.get('songId')
        labelId = data.get('labelId')

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE songs SET fk_label_id = %s WHERE song_id = %s''', (labelId, songId))
        mysql.connection.commit()
        cur.close()

        return {'message': 'Song label updated successfully'}, 200


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


api.add_resource(updateSongTitle, "/updatetitle")
api.add_resource(updateSongGenre, "/updategenre")
api.add_resource(updateReleaseDate, "/updatereleasedate")
api.add_resource(updateSongLabel, "/updatelabel")
api.add_resource(deleteSong, "/deletesong")
api.add_resource(getAlbumId, "/getalbumid")
api.add_resource(getSongId, "/getsongid")
api.add_resource(Users, "/users")
api.add_resource(Songs, "/songs")
api.add_resource(Albums, "/album")
api.add_resource(Artists, "/artist")
api.add_resource(Publisher, "/publisher")
api.add_resource(Genre, "/genre")
api.add_resource(SongArtist, "/songartist")
api.add_resource(Copyright, "/copyright")
api.add_resource(Label, "/label")
api.add_resource(Registrations, "/registrations")
api.add_resource(Payments, "/payments")
api.add_resource(SongMetadata, "/songmetadata")
api.add_resource(UserVaildate, "/uservaildate")
api.add_resource(GetUserSongs, "/getusersongs")
api.add_resource(getUserId, "/getuserid")
api.add_resource(SongProfileView, "/songprofileview")


if __name__ == '__main__':
    app.run(debug=True)
