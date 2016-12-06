from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def testindex():
	return "This is the index!!1"

@app.errorhandler(404)
def page_not_found(e):
	return render_template('errors/404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('errors/404.html'), 500

if __name__ == '__main__':
	app.run(debug=True)