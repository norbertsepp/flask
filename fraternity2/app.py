from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

try:
    conn = sqlite3.connect("fraternity.db", check_same_thread=False)
except sqlite3.Error:
    print("Connection failed")
    
cursor = conn.cursor()

FRATERNITIES = ["PhiKappaTheta", "DeltaPhi", "AlphaKappaAlpha"]

@app.route("/")
def index():
    return render_template("index.html", fraternities=FRATERNITIES)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    fraternity = request.form.get("fraternity")
    if not name or fraternity not in FRATERNITIES:
        return render_template("failure.html")
    
    cursor.execute("INSERT INTO registrants (name, fraternity) VALUES(?, ?);", (name, fraternity)) 
    conn.commit()
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = cursor.execute("SELECT * FROM registrants;").fetchall()
    print(registrants)
    return render_template("registrants.html", registrants=registrants)


@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        cursor.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")
    
    