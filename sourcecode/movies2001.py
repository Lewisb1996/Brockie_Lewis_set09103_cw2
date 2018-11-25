from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2001.db'

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
    db.cursor().execute('insert into movies2001  values ("1", "Harry Potter and The Philosophers Stone", "$974,755,371")')
    db.cursor().execute('insert into movies2001  values ("2", "The Lord of the Rings: The Fellowship of the Ring", "$871,530,324")')
    db.cursor().execute('insert into movies2001  values ("3", "Monsters, Inc", "$525,366,597")')
    db.cursor().execute('insert into movies2001  values ("4", "Shrek", "$484,409,218")')
    db.cursor().execute('insert into movies2001  values ("5", "Oceans Eleven", "$450,717,150")')
    db.cursor().execute('insert into movies2001  values ("6", "Pearl Harbor", "$449,220,945")')
    db.cursor().execute('insert into movies2001  values ("7", "The Mummy Returns", "$433,013,274")')
    db.cursor().execute('insert into movies2001  values ("8", "Jurassic Park III", "$368,780,809")')
    db.cursor().execute('insert into movies2001  values ("9", "Planet of the Apes", "$362,211,740")')
    db.cursor().execute('insert into movies2001  values ("10", "Hannibal", "$351,692,268")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2001 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
