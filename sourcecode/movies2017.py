from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2017.db'

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
    db.cursor().execute('insert into movies2017  values ("1", "Star Wars: The Last Jedi", "$1,332,539,889")')
    db.cursor().execute('insert into movies2017  values ("2", "Beauty and The Beast", "$1,263,521,126")')
    db.cursor().execute('insert into movies2017  values ("3", "The Fate of the Furious", "$1,236,005,118")')
    db.cursor().execute('insert into movies2017  values ("4", "Despicable Me 3", "$1,034,799,409")')
    db.cursor().execute('insert into movies2017  values ("5", "Jumanji: Welcome to The Jungle", "$962,077,546")')
    db.cursor().execute('insert into movies2017  values ("6", "Spider-Man: Homecoming", "$880,166,924")')
    db.cursor().execute('insert into movies2017  values ("7", "Wolf Warrior 2", "$874,325,959")')
    db.cursor().execute('insert into movies2017  values ("8", "Guardians of The Galaxy Vol. 2", "$863,756,051")')
    db.cursor().execute('insert into movies2017  values ("9", "Thor: Ragnarok", "$853,977,126")')
    db.cursor().execute('insert into movies2017  values ("10", "Wonder Woman", "$821,847,012")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2017 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
