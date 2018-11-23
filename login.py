from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3

app = Flask ( __name__ )
db_location = 'var/.users.db'

def get_db():
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

@app.route("/", methods = ['GET', 'POST'])
def root():
    error = None
    if request.method == 'POST':
            if request.form['username'] == 'lewis' and request.form['password'] == 'lewis':
                    return redirect(url_for('root'))
            else:
                    error = 'The Username and Password you entered is Invalid'
    return render_template("login.html", error=error)

@app.route("/register", methods = ['GET', 'POST'])
def register():
        db = get_db()
        error = "initial"
        errorname = None
        errorpassword = None
        erroremail = None
        date = ''
        if request.method == 'POST':
                if request.form['username'] == "":
                        errorname = 'Please enter a Username'
                else:
                      for row in db.cursor().execute("SELECT username FROM users WHERE username-'"+request.form['username']+"'"):
                              if str(row) == "(u'"+request.form['username']+"',)":
                                      errorname = "The Username entered is already used"
                      if errorname != None:
                                      errorname = "The Username entered is already used"
                      else:
                              if request.form['password'] == "":
                                      errorpassword = 'Please enter a Password'
                              else:
                                      if request.form['email'] == "":
                                              erroremail = 'Please enter your Email'
                                      else:
                                            db.cursor().execute('INSERT INTO users VALUES("'+request.form['username']+'", "'+request.form['password']+'", "'+request.form['email']+'")')
                                            db.commit()
        return render_template("register.html", error=error, errorname=errorname, errorpassword = errorpassword, erroremail=erroremail)

if __name__ == "__main__":
    app.run(host="0.0.0.0", febug=True) 
