from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/highestgrossing.db'

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
    db.cursor().execute('insert into highestgrossing values ("1", "Avatar", "2009", "$2,787,965,087")')
    db.cursor().execute('insert into highestgrossing values ("2", "Titanic", "1997", "$2,187,463,944")')
    db.cursor().execute('insert into highestgrossing values ("3", "Star Wars: The Force Awakens", "2015", "$2,068,223,624")')
    db.cursor().execute('insert into highestgrossing values ("4", "Avengers: Infinity War", "2018", "$2,046,687,478")')
    db.cursor().execute('insert into highestgrossing values ("5", "Jurassic World", "2015", "$1,671,713,208")')
    db.cursor().execute('insert into highestgrossing values ("6", "The Avengers", "2012", "$1,518,812,988")')
    db.cursor().execute('insert into highestgrossing values ("7", "Furious 7", "2015", "$1,516,045,911")')
    db.cursor().execute('insert into highestgrossing values ("8", "Avengers: Age of Ultron", "2015", "$1,405,403,694")')
    db.cursor().execute('insert into highestgrossing values ("9", "Black Panther", "2018", "$1,346,913,161")')
    db.cursor().execute('insert into highestgrossing values ("10", "Harry Potter and The Deathly Hallows - Part 2", "2011", "$1,341,511,219")')
    db.cursor().execute('insert into highestgrossing values ("11", "Star Wars: The Last Jesi", "2017", "$1,332,539,889")')
    db.cursor().execute('insert into highestgrossing values ("12", "Jurassic World: Fallen Kingdom", "2018", "$1,304,937,955")')
    db.cursor().execute('insert into highestgrossing values ("13", "Frozen", "2013", "$1,290,000,000")')
    db.cursor().execute('insert into highestgrossing values ("14", "Beauty and The Beast", "2017", "$1,263,521,126")')
    db.cursor().execute('insert into highestgrossing values ("15", "Incredibles 2", "2018", "$1,239,568,617")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM highestgrossing ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
