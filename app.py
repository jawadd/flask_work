from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True  # Make the session permanent
        user = request.form["username"]
        session["user"] = user
        flash("You were successfully logged in!")  # Flash message on successful login
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>Welcome, {user}!</h1><a href='/logout'>Logout</a>"
    else:
        flash("You need to log in first!")  # Flash message if not logged in
        return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    session.pop("user", None)
    flash("You were successfully logged out!")  # Flash message on logout
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
