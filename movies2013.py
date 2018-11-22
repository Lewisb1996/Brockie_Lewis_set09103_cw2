from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2013.db'

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
    db.cursor().execute('insert into movies2013  values ("1", "Frozen", "$1,276,480,335")')
    db.cursor().execute('insert into movies2013  values ("2", "Iron Man 3", "$1,214,811,252")')
    db.cursor().execute('insert into movies2013  values ("3", "Despicable Me 2", "$970,761,885")')
    db.cursor().execute('insert into movies2013  values ("4", "The Hobbit: The Disolation of Smaug", "$958,366,855")')
    db.cursor().execute('insert into movies2013  values ("5", "The Hunger Games: Catching Fire", "$865,011,746")')
    db.cursor().execute('insert into movies2013  values ("6", "Fast & Furious 6", "$788,679,850")')
    db.cursor().execute('insert into movies2013  values ("7", "Monsters University", "$744,229,437")')
    db.cursor().execute('insert into movies2013  values ("8", "Gravity", "$723,192,705")')
    db.cursor().execute('insert into movies2013  values ("9", "Man of Steel", "$668,045,518")')
    db.cursor().execute('insert into movies2013  values ("10", "Thor: The Dark World", "$644,571,402")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2013 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
