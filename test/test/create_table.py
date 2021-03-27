import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute(
    'CREATE TABLE mondais(mondai STRING,type Integer,answer Integer,sentaku1 String,sentaku2 String,sentaku3 String,sentaku4 String)'
    )

conn.commit()
conn.close()