import sqlite3

db = sqlite3.connect("blog.db")

db.execute("DROP TABLE IF EXISTS users")
db.execute("CREATE TABLE users (username TEXT, password TEXT)")

db.execute("INSERT INTO users (username, password) VALUES ('Jim', 'jimpassword'), ('Kate', 'katepassword')")
db.commit()
db.close()
