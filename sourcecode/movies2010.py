from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2010.db'

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
    db.cursor().execute('insert into movies2010  values ("1", "Toy Story 3", "$1,066,969,703")')
    db.cursor().execute('insert into movies2010  values ("2", "Alice in Wonderland", "$1,025,467,110")')
    db.cursor().execute('insert into movies2010  values ("3", "Harry Potter and The Deathly Hallows - Part 1", "$960,283,305")')
    db.cursor().execute('insert into movies2010  values ("4", "Inception", "$825,532,764")')
    db.cursor().execute('insert into movies2010  values ("5", "Shrek Forever After", "$752,600,867")')
    db.cursor().execute('insert into movies2010  values ("6", "The Twilight Saga: Eclipse", "$698,491,347")')
    db.cursor().execute('insert into movies2010  values ("7", "Iron Man 2", "$623,933,331")')
    db.cursor().execute('insert into movies2010  values ("8", "Tangled", "$591,794,936")')
    db.cursor().execute('insert into movies2010  values ("9", "Despicable Me", "$543,113,985")')
    db.cursor().execute('insert into movies2010  values ("10", "How to Train Your Dragon", "$494,878,759")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2010 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
