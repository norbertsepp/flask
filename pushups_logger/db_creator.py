# METHOD 1: SQLite - db U1
import sqlite3

try:
    conn = sqlite3.connect("db.sqlite")
    print("Database connected successfully")
except ConnectionError: 
    print("SQLite table connection error!")

SQL_STM = """
CREATE TABLE IF NOT EXISTS USER
         (ID INTEGER PRIMARY KEY     NOT NULL,
         EMAIL      CHAR(100)    UNIQUE NOT NULL,
         PASSWORD   CHAR(200)     NOT NULL,
         NAME       CHAR(100)
         );
"""
conn.execute(SQL_STM)
print("Table USER created")

conn.close()

# METHOD 2: SQLAlchemy
# run from the virtual environment's project folder: python db_creator.py

# from . import db, create_app
# db.create_all(app=create_app())
