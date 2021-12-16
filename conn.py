import mysql.connector as sql

db = sql.connect(
    host="localhost",
    user="root",
    password="",
    database="cinemaku"
)
cursor = db.cursor()

def inupdel(sql): # panggil fungsi ini untuk menggunakan INSERT UPDATE dan DELETE
    cursor.execute(sql)
    db.commit()

def read(sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    return data