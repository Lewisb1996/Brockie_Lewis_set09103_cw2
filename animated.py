from flask import Flask , g
import sqlite3

from flask import Flask
app = Flask ( __name__ )
db_location = 'var/test1.db'

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
        with app.open_resource ('schema1.sql', mode ='r') as f :
            db.cursor().executescript(f.read())
        db.commit()

@app.route("/")
def root():
    db = get_db()
    db.cursor().execute('insert into animated values ("1", "Frozen", "2013", "$1,290,000,0000")')
    db.cursor().execute('insert into animated values ("2", "Incredibles 2", "2018", "$1,239,568,617")')
    db.cursor().execute('insert into animated values ("3", "Minions", "2015", "$1,159,398,397")')
    db.cursor().execute('insert into animated values ("4", "Toy Story 3", "2010", "$1,066,969,703")')   
    db.cursor().execute('insert into animated values ("5", "Despicable Me 3", "2017", "$1,034,799,409")')
    db.cursor().execute('insert into animated values ("6", "Finding Dory", "2016", "$1,028,570,889")')
    db.cursor().execute('insert into animated values ("7", "Zootopia", "2016", "$1,023,784,195")')
    db.cursor().execute('insert into animated values ("8", "Despicable Me 2", "2013", "$970,761,885")')
    db.cursor().execute('insert into animated values ("9", "The Lion King", "1994", "$968,483,777")')
    db.cursor().execute('insert into animated values ("10", "Finding Nemo", "2003", "$940,335,536")')
    db.cursor().execute('insert into animated values ("11", "Shrek 2", "2004", "$919,838,758")')
    db.cursor().execute('insert into animated values ("12", "Ice Age: Dawn of the Dinosaurs", "2009", "$886,686,817")')
    db.cursor().execute('insert into animated values ("13", "Ice Age: Continental Drift", "2012", "$877,244,782")')
    db.cursor().execute('insert into animated values ("14", "The Secret Life of Pets", "2016", "$875,457,937")')
    db.cursor().execute('insert into animated values ("15", "Inside Out", "2015", "$857,611,174")')
    db.commit()

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM animated ORDER by rank"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
    
    page.append('</ul></html>')
    return ''.join(page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
