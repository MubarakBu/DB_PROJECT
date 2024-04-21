import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import func, desc, or_
from datetime import timedelta
app = Flask(__name__)
app.secret_key = 'r123q123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://mfb56:InfSci2710_4612667@164.90.137.194/mfb56'

db = SQLAlchemy(app)


class Genres(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_name = db.Column(db.String(255), nullable=False)


class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    fk_user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)


# class Song_Artist(db.Model):
#     fk_artist_id = db.Column(db.Integer, db.ForeignKey(
#         'artist.artist_id'), nullable=False)
#     song_id_fk = db.Column(db.Integer, db.ForeignKey(
#         'songs.song_id'), nullable=False)


class Publisher(db.Model):
    publisher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    fk_user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)


class Users(db.Model):
    song_writer_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)


class Payments(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String(20))
    song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.song_id'), nullable=False)


# class Registrations(db.Model):
#     register_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     song_id_fk = db.Column(db.Integer, db.ForeignKey(
#         'songs.song_id'), nullable=False)
#     registration_date = db.Column(db.Date, nullable=False)


class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_title = db.Column(db.String(255))
    fk_album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'))
    fk_artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.artist_id'), nullable=False)
    fk_genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    publisher_id_fk = db.Column(
        db.Integer, db.ForeignKey('publisher.publisher_id'))
    song_writer_id_fk = db.Column(db.Integer, db.ForeignKey(
        'song_writers.song_writer_id'), nullable=False)


class CopyrightInfo(db.Model):
    copyright_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    copyright_holder = db.Column(db.Text, nullable=False)
    fk_song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.song_id'), nullable=False)


class Label(db.Model):
    label_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label_name = db.Column(db.String(20), nullable=False)
    fk_user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)


class SongMetadata(db.Model):
    metadata_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    release_date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    language = db.Column(db.String(20), nullable=False)
    fk_song_id = db.Column(db.Integer, db.ForeignKey(
        'songs.song_id'), nullable=False)

################################## HOME/LOGIN ####################################


@app.route('/')
def login_form():
    return render_template('login.html')

############################################# REGISTER ###########################################


@app.route('/register')
def register_form():
    return render_template('register.html')


@app.route('/adduser', methods=['POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        # Data to be passed in the request body
        data = {
            "user_name": username,
            "first_name": firstname,
            "last_name": lastname,
            "user_email": email,
            "password": password
        }

        # Send a POST request to the database API with the form data
        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "users", json=data)

        # Print the response content for debugging
        print("Response Content:", response.status_code)
        if response.status_code == 500:
            flash(
                'Username is already in use. Please choose a different username.', 'error')
            return render_template('register.html')
        else:
            # Redirect to a success page or any other page
            return redirect(url_for('success'))

    return render_template('register.html')


@app.route('/success')
def success():
    return 'Registration successful! <a href="/login">Go to login page</a>'


##################################### LOGIN ###############################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract username and password from the form
        username = request.form['username']
        password = request.form['password']
        session['username'] = username

        data = {
            "username": username,
            "password": password
        }

        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "uservaildate", json=data)

        print("Response JSON:", response.json())

        # Check the response status and handle accordingly
        if response.status_code == 200:
            return redirect(url_for('loginsuccess'))
        else:
            # Handle failed login attempt
            flash('Wrong Username or Password.', 'error')
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


@app.route('/loginsuccess')
def loginsuccess():
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()
    # Redirect the user to the login page or any other appropriate page
    return redirect(url_for('login'))


##################################### ADD SONG ############################################

@app.route('/addsong', methods=['GET', 'POST'])
def addsong():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    gui = "http://127.0.0.1:5000/getuserid"
    guires = requests.get(gui, params={"username": username})
    userId = guires.json()[0][0]

    BASE_GENRE = "http://127.0.0.1:5000/genre"
    BASE_ALBUM = "http://127.0.0.1:5000/album"
    BASE_PUBLISHER = "http://127.0.0.1:5000/publisher"
    BASE_LABEL = "http://127.0.0.1:5000/label"
    BASE_ARTIST = "http://127.0.0.1:5000/artist"
    response1 = requests.get(BASE_GENRE)
    response2 = requests.get(BASE_ALBUM, params={"userId": userId})
    response3 = requests.get(BASE_PUBLISHER, params={"userId": userId})
    response4 = requests.get(BASE_LABEL, params={"userId": userId})
    response5 = requests.get(BASE_ARTIST, params={"userId": userId})

    genres = response1.json()
    albums = response2.json()
    publishers = response3.json()
    labels = response4.json()
    artists = response5.json()
    return render_template('addsong.html', genres=genres, albums=albums, publishers=publishers,
                           labels=labels, artists=artists)


@app.route('/insertsong', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        username = session.get('username')
        gui = "http://127.0.0.1:5000/getuserid"
        guires = requests.get(gui, params={"username": username})
        userId = guires.json()[0][0]
        # Extract username and password from the form
        song_title = request.form['song_title']
        genre_id = request.form['genre_id']
        album_id = request.form['album_id']
        publisher_id = request.form['publisher_id']
        user_id = userId
        label_id = request.form['label_id']
        artist_id = request.form['artist_id']
        # song metadata
        releaseDate = request.form['relase_date']
        duration = request.form['duration']
        songLanguage = request.form['song_language']

        data = {
            "songTitle": song_title,
            "genreId": genre_id,
            "albumId": album_id,
            "publisherId": publisher_id,
            "userId": user_id,
            "labelId": label_id
        }

        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "songs", json=data)

        # print("Response JSON:", response.json())
        if response.status_code == 500:
            flash('Song title is already taken. Please choose another title.', 'error')
            return redirect(url_for('addsong'))
        else:
            print("Response JSON:", response.json())

        if response.status_code == 201:
            gsi = "http://127.0.0.1:5000/getsongid"
            gsires = requests.get(
                gsi, params={"userId": userId, "songName": song_title})
            songId = gsires.json()[0][0]

            metadata = {
                "releaseDate": releaseDate,
                "duration": duration,
                "songLanguage": songLanguage,
                "songId": songId
            }

            songartist = {
                "sognId": songId,
                "artistId": artist_id
            }

            BASE = "http://127.0.0.1:5000/"
            response2 = requests.post(BASE + "songartist", json=songartist)
            print("Response JSON:", response2.json())

            BASE = "http://127.0.0.1:5000/"
            response3 = requests.post(BASE + "songmetadata", json=metadata)
            print("Response JSON:", response3.json())

        # Check the response status and handle accordingly

        return redirect(url_for('insertsuccess'))

    return render_template('addsong.html')


@app.route('/insertsuccess')
def insertsuccess():
    return redirect(url_for('dashboard'))

####################### Payments ###############################


@app.route('/paynow')
def paynow():
    song_id = request.args.get('songId')
    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "songs", params={"songId": song_id})
    songInfo = response.json()
    return render_template('payment.html', song_id=song_id, songInfo=songInfo)


@app.route('/payment_process', methods=['GET', 'POST'])
def payment_process():
    if request.method == 'POST':
        song_id = request.args.get('songId')
        amount = 150.00
        payment_method = request.form.get('payment_method')
        # payment_date = datetime.datetime.now().strftime('%Y-%m-%d')
        details = {
            "amount": amount,
            "songId": song_id,
            "payment_method": payment_method
        }
        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + 'payments', json=details)
        print(response)
        print(details)
    return redirect(url_for('dashboard'))


#################################### HOME #################################


@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    # Query the database to retrieve the user's information and songs
    # Example: user_info = get_user_info(username)
    #          user_songs = get_user_songs(username)
    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "getusersongs",
                            params={"username": username})

    songs = response.json()

    # Render the dashboard template with the user's information and songs
    return render_template('dashboard.html', username=username, user_songs=songs)


################### ADD ALBUM #############################

@app.route('/album')
def addalbum():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))
    return render_template('newalbum.html')


@app.route('/addalbum', methods=['GET', 'POST'])
def insertalbum():
    if request.method == 'POST':
        username = session.get('username')
        gui = "http://127.0.0.1:5000/getuserid"
        guires = requests.get(gui, params={"username": username})
        userId = guires.json()[0][0]

        # Extract username and password from the form
        albumTitle = request.form['album_title']
        releaseDate = request.form['relase_date']
        user_Id = userId

        data = {
            "albumTitle": albumTitle,
            "releaseDate": releaseDate,
            "userId": user_Id
        }

        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "album", json=data)

        print("Response JSON:", response.json())

        return redirect(url_for('albumadded'))

    return render_template('newalbum.html')


@app.route('/albumadded')
def albumadded():
    return redirect(url_for('dashboard'))


################### ADD ARTIST #############################

@app.route('/artist')
def addartist():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    return render_template('newartist.html')


@app.route('/addartist', methods=['GET', 'POST'])
def insertartist():
    if request.method == 'POST':
        username = session.get('username')
        gui = "http://127.0.0.1:5000/getuserid"
        guires = requests.get(gui, params={"username": username})
        userId = guires.json()[0][0]
        # Extract username and password from the form
        firstName = request.form['frist_name']
        lastName = request.form['last_name']
        userId = userId

        data = {
            "firstName": firstName,
            "lastName": lastName,
            "userId": userId
        }

        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "artist", json=data)

        print("Response JSON:", response.json())

        # Check the response status and handle accordingly

        return redirect(url_for('artistadded'))

    return render_template('newartist.html')


@app.route('/artistadded')
def artistadded():
    return redirect(url_for('dashboard'))


################### ADD PUBLISHER #############################

@app.route('/publisher')
def addpublisher():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    return render_template('newpublisher.html')


@app.route('/addpublisher', methods=['GET', 'POST'])
def insertpublisher():
    if request.method == 'POST':
        username = session.get('username')
        gui = "http://127.0.0.1:5000/getuserid"
        guires = requests.get(gui, params={"username": username})
        userId = guires.json()[0][0]
        # Extract username and password from the form
        firstName = request.form['frist_name']
        lastName = request.form['last_name']
        userId = userId

        data = {
            "firstName": firstName,
            "lastName": lastName,
            "userId": userId
        }

        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "publisher", json=data)

        print("Response JSON:", response.json())

        # Check the response status and handle accordingly

        return redirect(url_for('publisheradded'))

    return render_template('newpublisher.html')


@app.route('/publisheradded')
def publisheradded():
    return redirect(url_for('dashboard'))


################### ADD LABEL #############################

@app.route('/label')
def addlabel():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    return render_template('newlabel.html')


@app.route('/addlabel', methods=['GET', 'POST'])
def insertlabel():
    if request.method == 'POST':
        username = session.get('username')
        gui = "http://127.0.0.1:5000/getuserid"
        guires = requests.get(gui, params={"username": username})
        userId = guires.json()[0][0]
        # Extract username and password from the form
        labelName = request.form['label_name']
        userId = userId

        data = {
            "labelName": labelName,
            "userId": userId
        }

        BASE = "http://127.0.0.1:5000/"
        response = requests.post(BASE + "label", json=data)

        print("Response JSON:", response.json())

        # Check the response status and handle accordingly

        return redirect(url_for('labeladded'))

    return render_template('newlabel.html')


@app.route('/labeladded')
def labeladded():
    return redirect(url_for('dashboard'))


################################## SONG PROFILE #####################################


@app.route('/songprofile')
def songprofile():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    song_id = request.args.get('song_id')
    checkRegisteredSong = Payments.query.filter(
        Payments.song_id == song_id).first()
    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "songs", params={"songId": song_id})
    response2 = requests.get(BASE + "songmetadata", params={"songId": song_id})

    songInfo = response.json()
    metadata = response2.json()
    print(response.json())
    print(response2.json())

    if checkRegisteredSong is not None:
        print(checkRegisteredSong.payment_id)
    else:
        print("checkRegisteredSong is None")

    return render_template('songprofile.html', songInfo=songInfo, metadata=metadata, songId=song_id, checkRegisteredSong=checkRegisteredSong)


############################## UPDATE SONG #####################


@app.route('/editsong')
def editsong():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    username = session.get('username')
    gui = "http://127.0.0.1:5000/getuserid"
    guires = requests.get(gui, params={"username": username})
    userId = guires.json()[0][0]

    song_id = request.args.get('songId')

    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "songs", params={"songId": song_id})
    response2 = requests.get(BASE + "songmetadata", params={"songId": song_id})
    response3 = requests.get(BASE + "genre")
    response4 = requests.get(BASE + "label", params={"userId": userId})

    songInfo = response.json()
    metadata = response2.json()
    genre = response3.json()
    label = response4.json()

    print(label)

    return render_template('editsong.html', songInfo=songInfo, metadata=metadata, genre=genre, label=label, songId=song_id)


@app.route('/edit', methods=['GET', 'POST'])
def updatesong():
    if request.method == 'POST':

        song_id = request.args.get('songId')

        songTitle = request.form['song_title']
        genreId = request.form['genre_id']
        releaseDate = request.form['release_date']
        labelId = request.form['label_id']

        titleUpdate = {
            "songId": song_id,
            "songTitle": songTitle
        }
        generUpdate = {
            "songId": song_id,
            "genreId": genreId
        }
        releaseDateUpdate = {
            "songId": song_id,
            "releaseDate": releaseDate
        }
        labelUpdate = {
            "songId": song_id,
            "labelId": labelId
        }

        BASE = "http://127.0.0.1:5000/"

        response1 = requests.put(BASE + "updatetitle", json=titleUpdate)
        response2 = requests.put(BASE + "updategenre", json=generUpdate)
        response3 = requests.put(
            BASE + "updatereleasedate", json=releaseDateUpdate)
        response4 = requests.put(BASE + "updatelabel", json=labelUpdate)

        print(response1.json())
        print(response2.json())
        print(response3.json())
        print(response4.json())

        return redirect(url_for('songupdated', song_id=song_id))


@app.route('/songupdated')
def songupdated():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    song_id = request.args.get('song_id')
    BASE = "http://127.0.0.1:5000/"
    response = requests.get(BASE + "songs", params={"songId": song_id})
    response2 = requests.get(BASE + "songmetadata", params={"songId": song_id})

    songInfo = response.json()
    metadata = response2.json()
    print(response.json())
    print(response2.json())

    return render_template('songprofile.html', songInfo=songInfo, metadata=metadata, songId=song_id)


################################## DELETE SONG ##########################

@app.route('/deletesong')
def deletesong():
    username = session.get('username')
    if not username:
        # Redirect to login if the user is not logged in
        return redirect(url_for('login'))

    song_id = request.args.get('songId')
    BASE = "http://127.0.0.1:5000/"
    response = requests.delete(BASE + "deletesong", params={"songId": song_id})

    print(response.json())

    return redirect(url_for('deleted'))


@app.route('/deleted')
def deleted():
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True, host='::1')
