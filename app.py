from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

import os
from database import create_table, save_results

from mapreduce_engine import mapreduce_log_analysis

load_dotenv()
create_table()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if (
            username == os.getenv("ADMIN_USERNAME")
            and password == os.getenv("ADMIN_PASSWORD")
        ):
            session["logged_in"] = True
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if not session.get("logged_in"):
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":

        file = request.files["logfile"]

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        results = mapreduce_log_analysis(filepath)

        save_results(results)

        return render_template(
            "results.html",
            results=results
        )

    return render_template("upload.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)