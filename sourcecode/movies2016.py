from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2016.db'

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
    db.cursor().execute('insert into movies2016  values ("1", "Captain America: Civil War", "$1,153,304,495")')
    db.cursor().execute('insert into movies2016  values ("2", "Rogue One: A Star Wars Story", "$1,056,057,273")')
    db.cursor().execute('insert into movies2016  values ("3", "Finding Dory", "$1,028,570,889")')
    db.cursor().execute('insert into movies2016  values ("4", "Zootopia", "$1,023,784,195")')
    db.cursor().execute('insert into movies2016  values ("5", "The Jungle Book", "$966,550,600")')
    db.cursor().execute('insert into movies2016  values ("6", "The Secret Life of Pets", "$875,457,937")')
    db.cursor().execute('insert into movies2016  values ("7", "Batman v Superman: Dawn of Justice", "$873,634,919")')
    db.cursor().execute('insert into movies2016  values ("8", "Fantastic Beasts and Where to Find Them", "$814,037,575")')
    db.cursor().execute('insert into movies2016  values ("9", "Deadpool", "$783,112,979")')
    db.cursor().execute('insert into movies2016  values ("10", "Suicide Squad", "$746,846,894")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2016 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
