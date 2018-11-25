from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2015.db'

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
    db.cursor().execute('insert into movies2015  values ("1", "Star Wars: The Force Awakens", "$2,068,223,624")')
    db.cursor().execute('insert into movies2015  values ("2", "Jurassic World", "$1,671,713,208")')
    db.cursor().execute('insert into movies2015  values ("3", "Furious 7", "$1,516,045,911")')
    db.cursor().execute('insert into movies2015  values ("4", "Avengers: Age of Ultron", "$1,405,413,868")')
    db.cursor().execute('insert into movies2015  values ("5", "Minions", "$1,159,398,397")')
    db.cursor().execute('insert into movies2015  values ("6", "Spectre", "$880,674,609")')
    db.cursor().execute('insert into movies2015  values ("7", "Inside Out", "$857,611,174")')
    db.cursor().execute('insert into movies2015  values ("8", "Mission: Impossible - Rogue Nation", "$682,330,139")')
    db.cursor().execute('insert into movies2015  values ("9", "The Hunger Games: Mockingjay - Part 2", "$653,428,261")')
    db.cursor().execute('insert into movies2015  values ("10", "The Martian", "$630,161,890")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2015 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
