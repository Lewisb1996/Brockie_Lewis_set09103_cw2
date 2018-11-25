from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2009.db'

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
    db.cursor().execute('insert into movies2009  values ("1", "Avatar", "$2,749,064,328")')
    db.cursor().execute('insert into movies2009  values ("2", "Harry Potter and The Half-Blood Prince", "$934,416,487")')
    db.cursor().execute('insert into movies2009  values ("3", "Ice Age: Dawn of the Dinosaurs", "$886,686,817")')
    db.cursor().execute('insert into movies2009  values ("4", "Transformers: Revenge of the Fallen", "$836,303,693")')
    db.cursor().execute('insert into movies2009  values ("5", "2012", "$769,679,473")')
    db.cursor().execute('insert into movies2009  values ("6", "Up", "$735,099,082")')
    db.cursor().execute('insert into movies2009  values ("7", "The Twilight Saga: New Moon", "$709,711,008")')
    db.cursor().execute('insert into movies2009  values ("8", "Sherlock Holmes", "$524,028,679")')
    db.cursor().execute('insert into movies2009  values ("9", "Angels & Demons", "$485,930,816")')
    db.cursor().execute('insert into movies2009  values ("10", "The Hangover", "$467,483,912")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2009 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
