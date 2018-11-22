from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2006.db'

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
    db.cursor().execute('insert into movies2006  values ("1", "Pirates of the Caribbean: Dead Mans Chest", "$1,096,179,725")')
    db.cursor().execute('insert into movies2006  values ("2", "The Da Vinci Code", "$758,239,851")')
    db.cursor().execute('insert into movies2006  values ("3", "Ice Age: The Meltdown", "$660,940,780")')
    db.cursor().execute('insert into movies2006  values ("4", "Casino Royale", "$599,045,960")')
    db.cursor().execute('insert into movies2006  values ("5", "Night at The Museum", "$574,480,841")')
    db.cursor().execute('insert into movies2006  values ("6", "Cars", "$462,216,280")')
    db.cursor().execute('insert into movies2006  values ("7", "X-Men: The Last Stand", "$459,359,555")')
    db.cursor().execute('insert into movies2006  values ("8", "Mission: Impossible III", "$397,850,012")')
    db.cursor().execute('insert into movies2006  values ("9", "Superman Returns", "$391,081,192")')
    db.cursor().execute('insert into movies2006  values ("10", "Happy Feet", "$384,335,608")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2006 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
