from flask import Flask, redirect,url_for,render_template


app = Flask(__name__)

@app.route("/")
def home():
    return "This is home page, <h1> Hello </h1>"

@app.route("/<name>")
def user(name):
    return f"<h1> Hello {name}</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/admin2")
def admin2():
    return redirect(url_for("user", name ="Jawad"))


if __name__ =="__main__":
    app.run()
