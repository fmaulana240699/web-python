from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')


@app.route('/home', methods= ['POST', 'GET'])
def home():
	username=request.args.get('username', 'password')

	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		greeting = f"Halo {username}"
		return render_template('home.html', greeting=greeting)
	else:
		return "Please Login First on <a href='http://localhost:5000/login'> here </a>"

@app.route('/login', methods=['POST', 'GET'])
def login():
	return render_template("login.html")

if __name__ == "__main__":
	app.run()