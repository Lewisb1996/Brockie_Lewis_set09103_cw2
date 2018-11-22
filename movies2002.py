from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2002.db'

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
    db.cursor().execute('insert into movies2002  values ("1", "The Lord of the Rings: The Two Towers", "$926,047,111")')
    db.cursor().execute('insert into movies2002  values ("2", "Harry Potter and The Chamber of Secrets", "$878,979,634")')
    db.cursor().execute('insert into movies2002  values ("3", "Spider-Man", "$821,708,551")')
    db.cursor().execute('insert into movies2002  values ("4", "Star Wars: Episode II - Attack of the Clones", "$649,398,328")')
    db.cursor().execute('insert into movies2002  values ("5", "Men in Black II", "$441,818,803")')
    db.cursor().execute('insert into movies2002  values ("6", "Die Another Day", "$431,971,116")')
    db.cursor().execute('insert into movies2002  values ("7", "Signs", "$408,247,917")')
    db.cursor().execute('insert into movies2002  values ("8", "Ice Age", "$383,257,136")')
    db.cursor().execute('insert into movies2002  values ("9", "My Big Fat Greek Wedding", "$368,744,044")')
    db.cursor().execute('insert into movies2002  values ("10", "Minority Report", "$358,372,926")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2002 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
