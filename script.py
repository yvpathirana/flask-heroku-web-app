from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")
@app.route('/about')
def page():
	return render_template("page.html")
@app.route('/nav')
def nav():
	return render_template("navigation.html")

if __name__=="__main__":
	app.run(debug=True)