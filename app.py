from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import sqlite3
import os


def open_db():
    if 'db' not in g:
        g.db = sqlite3.connect("blog.db")
        
    return g.db

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()


def users():
    if request.method == "POST":
        db = open_db()
        username = request.form["username"]
        password = request.form["password"]
        db.execute("INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')")
        db.commit()

    db = open_db()
    results = db.execute("SELECT * FROM users").fetchall()
    for r in results:
        print(r)

    return render_template("users.html", data = results)


app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())

app.add_url_rule("/users", "users", users, methods=["GET", "POST"])

app.run()
