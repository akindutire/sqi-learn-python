# Installation of mysql connector
# pip install mysql-connector-python

import mysql.connector as sql

db = sql.connect(
    host="localhost",
    user="root",
    password="mac_root",
    database="sqi_l1"
)

print("Database connected successfully")

cursor = db.cursor() # Create a cursor object to interact with the database

# cursor.execute("show databases")
# databases = cursor.fetchall()

tables = cursor.execute("show tables")
print("tables:", cursor.fetchall())

#Queries
#drop database sqi_l1
#create database sqi_l1

