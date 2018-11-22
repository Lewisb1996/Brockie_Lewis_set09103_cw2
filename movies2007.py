from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2007.db'

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
    db.cursor().execute('insert into movies2007  values ("1", "Pirates of the Caribbean: At Worlds End", "$963,420,425")')
    db.cursor().execute('insert into movies2007  values ("2", "Harry Potter and The Order of the Pheonix", "$939,885,929")')
    db.cursor().execute('insert into movies2007  values ("3", "Spider-Man 3", "$890,871,626")')
    db.cursor().execute('insert into movies2007  values ("4", "Shrek The Third", "$798,958,162")')
    db.cursor().execute('insert into movies2007  values ("5", "Transformers", "$709,709,780")')
    db.cursor().execute('insert into movies2007  values ("6", "Ratatouille", "$620,702,951")')
    db.cursor().execute('insert into movies2007  values ("7", "I Am Legend", "$585,349,010")')
    db.cursor().execute('insert into movies2007  values ("8", "The Simpsons Movie", "$527,071,022")')
    db.cursor().execute('insert into movies2007  values ("9", "National Treasure: Book of Secrets", "$457,364,600")')
    db.cursor().execute('insert into movies2007  values ("10", "300", "$456,068,181")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2007 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
