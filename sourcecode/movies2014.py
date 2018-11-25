from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2014.db'

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
    db.cursor().execute('insert into movies2014  values ("1", "Transformers: Age of Extinction", "$1,104,054,072")')
    db.cursor().execute('insert into movies2014  values ("2", "The Hobbit: The Battle of The Five Armies", "$956,019,788")')
    db.cursor().execute('insert into movies2014  values ("3", "Guardians of The Galaxy", "$773,328,629")')
    db.cursor().execute('insert into movies2014  values ("4", "Maleficent", "$758,539,785")')
    db.cursor().execute('insert into movies2014  values ("5", "The Hunger Games: Mockingjay - Part 1", "$755,356,711")')
    db.cursor().execute('insert into movies2014  values ("6", "X-Men: Days of Future Past", "$747,862,775")')
    db.cursor().execute('insert into movies2014  values ("7", "Captain America: The Winter Soldier", "$714,264,267")')
    db.cursor().execute('insert into movies2014  values ("8", "Dawn of The Planet of The Apes", "$710,644,566")')
    db.cursor().execute('insert into movies2014  values ("9", "The Amazing Spider-Man 2", "$708,982,323")')
    db.cursor().execute('insert into movies2014  values ("10", "Instellar", "$677,463,813")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2014 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
