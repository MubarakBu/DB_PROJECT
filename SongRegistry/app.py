from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify


app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

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