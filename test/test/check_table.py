import sqlite3



def check():
    dbname = 'TEST.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    # terminalで実行したSQL文と同じようにexecute()に書く
    cur.execute('SELECT * FROM mondais')


    data1 = cur.fetchall()
    # 中身を全て取得するfetchall()を使って、printする。
    print(data1)


    cur.close()
    conn.close()
    return data1