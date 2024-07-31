from flask import Flask, request, render_template, redirect, session
from flask_session import Session

import sqlite3

# Configure app
app = Flask(__name__)

# Connect to db
conn = sqlite3.connect("store.db", check_same_thread=False)
cursor = conn.cursor()

# Session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    books = cursor.execute("SELECT * FROM books;").fetchall()
    print(session)  # how does a session look like?
    return render_template("books.html", books=books)

@app.route("/cart", methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []

    # POST
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")
    
    # GET
    cart_list = session["cart"]

    if len(cart_list) > 0:
        qm = '?' + ',?' * (len(cart_list) - 1)
    books_c = cursor.execute(f"SELECT * FROM books WHERE id IN ({qm});", cart_list)
    books = books_c.fetchall()
    return render_template("cart.html", books=books)
    
    