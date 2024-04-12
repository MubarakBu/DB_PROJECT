from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests


app = Flask(__name__)
app.secret_key = 'r123q123'


@app.route('/')
def login_form():
    return render_template('login.html')


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
            flash('Username is already in use. Please choose a different username.', 'error')
            return render_template('register.html')
        else:
            # Redirect to a success page or any other page
            return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/success')
def success():
    return 'Registration successful! <a href="/login">Go to login page</a>'



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
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

@app.route('/loginsuccess')
def loginsuccess():
    return redirect(url_for('dashboard'))





@app.route('/addsong', methods=['GET', 'POST'])
def addsong():
    BASE_GENRE = "http://127.0.0.1:5000/genre"
    BASE_ALBUM = "http://127.0.0.1:5000/album"
    BASE_PUBLISHER = "http://127.0.0.1:5000/publisher"
    BASE_LABEL = "http://127.0.0.1:5000/label"
    response1 = requests.get(BASE_GENRE)
    response2 = requests.get(BASE_ALBUM)
    response3 = requests.get(BASE_PUBLISHER)
    response4 = requests.get(BASE_LABEL)

    genres = response1.json()
    albums = response2.json()
    publishers = response3.json()
    labels = response4.json()

    return render_template('addsong.html', genres=genres, albums=albums, publishers=publishers, labels=labels)




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

        print("Response JSON:", response.json())

        # Check the response status and handle accordingly
        
        return redirect(url_for('insertsuccess'))

    return render_template('addsong.html')

@app.route('/insertsuccess')
def insertsuccess():
    return redirect(url_for('dashboard'))







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
    response = requests.get(BASE + "getusersongs", params={"username": username})

    songs = response.json()

    # Render the dashboard template with the user's information and songs
    return render_template('dashboard.html', username=username, user_songs=songs)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2')