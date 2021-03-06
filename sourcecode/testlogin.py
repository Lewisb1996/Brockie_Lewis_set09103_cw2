from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/.movies2000.db'

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

def init_db_values():
    with app.app_context():
         db = get_db()
         with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().execute('insert into users values ("iLewis", "hello", "lewis@lewis")')
    db.commit()

@app.route("/")
def root():
   db = get_db()
   db.cursor().execute('insert into users values ("test", "test2", "test@test")')
   db.commit()

   page = []
   page.append('<html><ul>')
   sql = "SELECT rowid, * FROM users ORDER by username"
   for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
   page.append('</ul></html>')
   return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
