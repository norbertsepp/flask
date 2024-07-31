from flask import Flask, request, render_template

app = Flask(__name__)

FRATERNITIES = ["PhiKappaTheta", "DeltaPhi", "AlphaKappaAlpha"]

@app.route("/")
def index():
    return render_template("index.html", fraternities=FRATERNITIES)

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or request.form.get("fraternity") not in FRATERNITIES:
        return render_template("failure.html")
    return render_template("success.html", name=request.form.get("name"))
    