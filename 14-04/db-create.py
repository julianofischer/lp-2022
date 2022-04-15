import sqlite3
con = sqlite3.connect('exemplo.db')
cur = con.cursor()

#cur.execute('CREATE TABLE cliente (nome text, idade integer)')
#cur.execute("INSERT INTO cliente VALUES ('juliano', 33)")
#con.commit()

def insert(cliente):
    s = f"INSERT INTO cliente VALUES ('{cliente[0]}', {cliente[1]})"
    print('minhastr: ' + s)
    cur.execute(s)
    con.commit()

#insert({'nome': 'Guilherme', 'idade': 23})
#insert(('Jaina', 19))

def select_all():
    rows = cur.execute('SELECT * FROM cliente')
    return rows

for o in select_all():
    print(o)