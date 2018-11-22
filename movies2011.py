from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2011.db'

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
    db.cursor().execute('insert into movies2011  values ("1", "Harry Potter and The Deathly Hallows – Part 2", "$1,341,511,219")')
    db.cursor().execute('insert into movies2011  values ("2", "Transformers: Dark of the Moon", "$1,123,794,079")')
    db.cursor().execute('insert into movies2011  values ("3", "Pirates of the Caribbean: On Stranger Tides", "$1,045,713,802")')
    db.cursor().execute('insert into movies2011  values ("4", "The Twilight Saga: Breaking Dawn – Part 1", "$712,205,856")')
    db.cursor().execute('insert into movies2011  values ("5", "Mission: Impossible – Ghost Protocol", "$694,713,380")')
    db.cursor().execute('insert into movies2011  values ("6", "Kung Fu Panda 2", "$665,692,281")')
    db.cursor().execute('insert into movies2011  values ("7", "Fast Five", "$626,137,675")')
    db.cursor().execute('insert into movies2011  values ("8", "The Hangover Part II", "$586,764,305")')
    db.cursor().execute('insert into movies2011  values ("9", "The Smurfs", "$563,749,323")')
    db.cursor().execute('insert into movies2011  values ("10", "Cars 2", "$562,110,557")')
    db.commit()


    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2011 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
