from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2018.db'

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
    db.cursor().execute('insert into movies2018  values ("1", "Avengers: Infinity War", "$2,046,900,111")')
    db.cursor().execute('insert into movies2018  values ("2", "Black Panther", "$1,346,913,161")')
    db.cursor().execute('insert into movies2018  values ("3", "Jurassic World: Fallen Kingdom", "$1,304,937,955")')
    db.cursor().execute('insert into movies2018  values ("4", "Incredibles 2", "$1,240,258,133")')
    db.cursor().execute('insert into movies2018  values ("5", "Mission: Impossible - Fallout", "$791,017,452")')
    db.cursor().execute('insert into movies2018  values ("6", "Venom", "$780,176,808")')
    db.cursor().execute('insert into movies2018  values ("7", "Deadpool 2", "$734,245,921")')
    db.cursor().execute('insert into movies2018  values ("8", "Ant-Man and The Wasp", "$622,604,622")')
    db.cursor().execute('insert into movies2018  values ("9", "Ready Player One", "$582,218,455")')
    db.cursor().execute('insert into movies2018  values ("10", "Operation Red Sea", "$579,220,560")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2018 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
