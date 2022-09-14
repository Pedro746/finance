import mysql.connector as connector

# host="localhost",
# user="root",
# password="Antonov-an-225",
# database="db_finance",

db = connector.connect(
    host = "localhost",
    user = "root",
    password = "Antonov-an-225",
    database="db_finance"
)

cursor = db.cursor()