from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies200333.db'

def get_db () :
    db = getattr (g, 'db', None)
    if db is None :
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None )
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource ('schema.sql', mode ='r') as f :
            db.cursor().executescript(f.read())
        db.commit()

@app.route("/")
def root():
    db = get_db()
    db.cursor().execute('insert into movies2003  values ("1", "The Lord of the Rings: The Return of the King", "$1,119,929,521")')
    db.cursor().execute('insert into movies2003  values ("2", "Finding Nemo", "$940,335,536")')
    db.cursor().execute('insert into movies2003  values ("3", "The Matrix Reloaded", "$742,128,461")')
    db.cursor().execute('insert into movies2003  values ("4", "Pirates of the Caribbean: The Curse of the Black Pearl", "$654,264,015")')
    db.cursor().execute('insert into movies2003  values ("5", "Bruce Almighty", "$484,592,874")')
    db.cursor().execute('insert into movies2003  values ("6", "The Last Samurai", "$456,758,981")')
    db.cursor().execute('insert into movies2003  values ("7", "Terminator 3: Rise of the Machines", "$433,371,112")')
    db.cursor().execute('insert into movies2003  values ("8", "The Matrix Revolutions", "$427,343,298")')
    db.cursor().execute('insert into movies2003  values ("9", "X2", "$407,711,549")')
    db.cursor().execute('insert into movies2003  values ("10", "Bad Boys II", "$273,339,556")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2003 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
