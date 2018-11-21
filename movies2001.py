from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/movies2001.db'

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
    db.cursor().execute('insert into movies2001  values ("1", "Mission: Impossible 2", "$546,388,105")')
    db.cursor().execute('insert into movies2001  values ("2", "Gladiator", "$457,640,427")')
    db.cursor().execute('insert into movies2001  values ("3", "Cast Away", "$429,632,142")')
    db.cursor().execute('insert into movies2001  values ("4", "What Women Want", "$374,111,707")')
    db.cursor().execute('insert into movies2001  values ("5", "Dinosaur", "$349,822,765")')
    db.cursor().execute('insert into movies2001  values ("6", "How The Grinch Stole Christmas", "$345,141,403")')
    db.cursor().execute('insert into movies2001  values ("7", "Meet The Parents", "$330,444,045")')
    db.cursor().execute('insert into movies2001  values ("8", "The Perfect Storm", "$328,718,434")')
    db.cursor().execute('insert into movies2001  values ("9", "X-Men", "$296,339,527")')
    db.cursor().execute('insert into movies2001  values ("10", "What Lies Beneath", "$291,420,351")')
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
