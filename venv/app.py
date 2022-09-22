from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///narku"
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT album_name, artist_name, year, genre FROM albums WHERE visible = TRUE")
    albums = result.fetchall()
    return render_template("index.html", count=len(albums), albums=albums) 

@app.route("/new")
def new():
    return render_template("new.html")
	
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/send", methods=["POST"])
def send():
    album_name = request.form["album_name"]
    artist_name = request.form["artist_name"]
    year = request.form["year"]
    genre = request.form["genre"]
    visible="TRUE"
    sql = "INSERT INTO albums (album_name,artist_name,year,genre,visible) VALUES (:album_name,:artist_name,:year,:genre,:visible)"
    db.session.execute(sql, {"album_name":album_name,"artist_name":artist_name,"year":year,"genre":genre,"visible":visible})
    db.session.commit()
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/result")
def result():
    query = request.args["query"]
    sql = "SELECT * FROM albums WHERE album_name iLIKE :query"
    result = db.session.execute(sql, {"query":"'%"+query+"%'"})
    albums = result.fetchall()
    return render_template("result.html", albums=albums)
    

@app.route("/back")
def back():
    return redirect("/")