from flask import Flask, render_template

app=Flask(__name__)

@app.route('/nav')
def home():
	return render_template("home.html")
@app.route('/about')
def page():
	return render_template("page.html")
@app.route('/')
def nav():
	return render_template("navigation.html")
@app.route('/page1')
def page1():
	return render_template("page1.html")
@app.route('/photo')
def photo():
	return render_template("photos.html")
@app.route('/phy')
def phy():
	return render_template("phy.html")

if __name__=="__main__":
	app.run(debug=True)