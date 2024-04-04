from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify


app = Flask(__name__)

app.config['MYSQL_HOST'] = '164.90.137.194'
app.config['MYSQL_USER'] = 'mfb56'
app.config['MYSQL_PASSWORD'] = 'InfSci2710_4612667'
app.config['MYSQL_DB'] = 'mfb56'

mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM accounts''')
    data = cur.fetchall()
    cur.close
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)