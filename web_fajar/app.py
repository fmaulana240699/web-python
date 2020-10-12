from flask import Flask, session, redirect, url_for
from flask import request
from flask import render_template
from markupsafe import escape
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'jaringan'
#app.config['MYSQL_DB'] = 'chat_flask'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/home', methods= ['POST', 'GET'])
def home():
	if 'username' in session:
		username = session['username']
		greeting = f"Halo {username}"
		return render_template("home.html", greeting=greeting)
	return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		session['username'] = request.form['username']
		return redirect(url_for("home"))
	return render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == "POST":
		session['username'] = request.form['username']
		return redirect(url_for("home"))
	return render_template("register.html")


@app.route('/logout', methods=['POST', 'GET'])
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()