from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2004.db'

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
    db.cursor().execute('insert into movies2004  values ("1", "Shrek 2", "$919,838,758")')
    db.cursor().execute('insert into movies2004  values ("2", "Harry Potter and The Prisoner of Azkaban", "$796,668,549")')
    db.cursor().execute('insert into movies2004  values ("3", "Spider-Man 2", "$783,766,341")')
    db.cursor().execute('insert into movies2004  values ("4", "The Incredibles", "$633,019,734")')
    db.cursor().execute('insert into movies2004  values ("5", "The Passion of The Christ", "$611,899,420")')
    db.cursor().execute('insert into movies2004  values ("6", "The Day After Tomorrow", "$544,272,402")')
    db.cursor().execute('insert into movies2004  values ("7", "Meet The Fockers", "$516,642,939")')
    db.cursor().execute('insert into movies2004  values ("8", "Troy", "$497,409,852")')
    db.cursor().execute('insert into movies2004  values ("9", "Shark Tale", "$367,275,019")')
    db.cursor().execute('insert into movies2004  values ("10", "Oceans Twelve", "$362,744,280")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2004 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
