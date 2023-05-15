from flask import Flask
from  main import web_test

app =Flask(__name__)

@app.route("/")
def testing():
	return "<p>Hello, World</p>"

@app.route("/admin")
def admin():
	test = web_test()
	return f'{test}'

@app.route("/homepage")
def homepage():
	return "<button>Hello, World</button>"

@app.route("/DashBoard")
def dashboard():
	return "<p>Hello, World</p>"

@app.route("/Research")
def research():
	return "<p>Hello, World</p>"

@app.route("/profolio")
def profolio():
	return "<p>Hello, World</p>"

@app.route("/Education")
def education():
	return "<p>Hello, World</p>"


@app.route("/Support")
def support():
	return "<p>Hello, World</p>"
