from flask import Flask, render_template
import reader
import statistics as stats
import sys


app = Flask(__name__)


@app.route('/')
def show_bitcoin():
	avg = stats.get_statistics()
	price = reader.get_bitcoin()
	return render_template('index.html', price=price, avg=avg, plot="./static/bitcoin-stats.jpg")


def run_webserver():
	app.run(host="0.0.0.0", port=int("5000"), debug=True)


if __name__ == '__main__':
	run_webserver()