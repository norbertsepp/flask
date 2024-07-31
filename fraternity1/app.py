from flask import Flask, request, render_template, redirect

app = Flask(__name__)

FRATERNITIES = ["PhiKappaTheta", "DeltaPhi", "AlphaKappaAlpha"]

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html", fraternities=FRATERNITIES)

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or request.form.get("fraternity") not in FRATERNITIES:
        return render_template("failure.html")
    REGISTRANTS[request.form["name"]] = request.form["fraternity"]  
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)
    