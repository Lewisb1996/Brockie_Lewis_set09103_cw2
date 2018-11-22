from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2008.db'

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
    db.cursor().execute('insert into movies2008  values ("1", "The Dark Knight", "$997,000,000")')
    db.cursor().execute('insert into movies2008  values ("2", "Indiana Jones and the Kingdom of the Crystal Skull", "$786,636,033")')
    db.cursor().execute('insert into movies2008  values ("3", "Kung Fu Panda", "$631,744,560")')
    db.cursor().execute('insert into movies2008  values ("4", "Hancock", "$624,386,746")')
    db.cursor().execute('insert into movies2008  values ("5", "Mamma Mia!", "$609,841,637")')
    db.cursor().execute('insert into movies2008  values ("6", "Madagascar: Escape 2 Africa", "$603,900,354")')
    db.cursor().execute('insert into movies2008  values ("7", "Quantum of Solace", "$586,090,727")')
    db.cursor().execute('insert into movies2008  values ("8", "Iron Man", "$585,174,222")')
    db.cursor().execute('insert into movies2008  values ("9", "WALL-E", "$533,281,433")')
    db.cursor().execute('insert into movies2008  values ("10", "The Chronicles of Narnia: Prince Caspian", "$419,665,568")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2008 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
