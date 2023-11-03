# app.py code
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template("/index.html")


@app.route('/main')
def main():
	return render_template("/main.html")


@app.route('/jupyter_tutorial')
def jupyter_tutorial():
	return render_template("/jupyter_tutorial.html")


if __name__ == '__main__':
	app.run(debug=True)