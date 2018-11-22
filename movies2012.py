from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2012.db'

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
    db.cursor().execute('insert into movies2012  values ("1", "The Avengers", "$1,518,812,988")')
    db.cursor().execute('insert into movies2012  values ("2", "Skyfall", "$1,108,561,013")')
    db.cursor().execute('insert into movies2012  values ("3", "The Dark Knight Rises", "$1,084,939,099")')
    db.cursor().execute('insert into movies2012  values ("4", "The Hobbit: An Unexpected Journey", "$1,021,103,568")')
    db.cursor().execute('insert into movies2012  values ("5", "Ice Age: Continental Drift", "$877,244,782")')
    db.cursor().execute('insert into movies2012  values ("6", "The Twilight Saga: Breaking Down - Part 2", "$829,746,820")')
    db.cursor().execute('insert into movies2012  values ("7", "The Amazing Spider-Man", "$757,930,663")')
    db.cursor().execute('insert into movies2012  values ("8", "Madagascar 3: Europes Most Wanted", "$746,921,274")')
    db.cursor().execute('insert into movies2012  values ("9", "The Hunger Games", "$694,394,724")')
    db.cursor().execute('insert into movies2012  values ("10", "Men in Black 3", "$624,026,776")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2012 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
