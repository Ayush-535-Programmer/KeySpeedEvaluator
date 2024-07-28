import sqlite3
con = sqlite3.connect(database=r"keySpeed.db")

def create_db():
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS clientName(id INTEGER PRIMARY KEY AUTOINCREMENT,Score,Time,Difficulty)")
    con.commit()

def create_db_new():
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS clientBill(id INTEGER PRIMARY KEY AUTOINCREMENT,name,description,date,credit,debit,balance)")
    con.commit()

create_db()
# create_db_new()