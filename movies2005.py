from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2005.db'

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
    db.cursor().execute('insert into movies2005  values ("1", "Harry Potter and The Goblet of Fire", "$896,911,078")')
    db.cursor().execute('insert into movies2005  values ("2", "Star Wars: Episode III -  Revenge of The Sith", "$848,754,768")')
    db.cursor().execute('insert into movies2005  values ("3", "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "$745,013,115")')
    db.cursor().execute('insert into movies2005  values ("4", "War of The Worlds", "$591,745,540")')
    db.cursor().execute('insert into movies2005  values ("5", "King Kong", "$550,517,357")')
    db.cursor().execute('insert into movies2005  values ("6", "Madagascar", "$532,680,671")')
    db.cursor().execute('insert into movies2005  values ("7", "Mr. & Mrs. Smith", "$478,207,520")')
    db.cursor().execute('insert into movies2005  values ("8", "Charlie and The chocolate Factory", "$474,968,763")')
    db.cursor().execute('insert into movies2005  values ("9", "Batman Begins", "$374,218,673")')
    db.cursor().execute('insert into movies2005  values ("10", "Hitch", "$368,100,420")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM movies2005 ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
