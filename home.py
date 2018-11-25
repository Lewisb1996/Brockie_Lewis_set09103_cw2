import bcrypt
from functools import wraps
from flask import Flask, render_template, redirect, request, session, g, url_for
import sqlite3

app = Flask(__name__)
db_location = 'var/.users.db'

def get_db():
   db = getattr(g, 'db', None)
   if db is None:
      db = sqlite3.connect(db_location)
      g.db = db
   return db


@app.teardown_appcontext
def close_db_connection(exception):
   db = getattr(g, 'db', None)
   if db is not None:
      db.close()


def init_db():
   with app.app_context():
      db = get_db()
      with app.open_resource('schema.sql', mode='r') as f:
         db.cursor().executescript(f.read())
      db.commit()

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


def requires_login(f):
   @wraps(f)
   def decorated(*args, **kwargs):
      status = session.get('logged_in', False)
      if not status:
         return redirect(url_for('.root'))
      return f(*args, **kwargs)
   return decorated


@app.route('/logout')
def logout():
   session['logged_in'] = False
   session['user'] = None
   return redirect(url_for('.root'))

@app.route('/')
def root():
   status = session.get('logged_in', False)
   if not status:
      
      username = []
      password = []
     
      db = get_db()
      data = db.cursor().execute("SELECT * FROM users")
      data = data.fetchall()
      for value in (data):
         username.append(value[0])
         password.append(value[1])
   
      return render_template('login.html', username = username, password = password)
   
   username = []
   password = []

   db = get_db()
   data = db.cursor().execute("SELECT * FROM users")
   data = data.fetchall()
   for value in (data):
      username.append(value[0])
      password.append(value[1])

   return render_template('login.html', username = username, password = password)


@app.route("/register", methods=['GET', 'POST'])
def register():
   if request.method == 'POST':
      username = request.form['usrname-s']
      password = request.form['pswrd-s']
      email = request.form['email-s']
           
      password = password.encode('utf-8')
      
      spwd = bcrypt.hashpw(password, bcrypt.gensalt())
     
      check = False
       
      db = get_db()
      data = db.cursor().execute("SELECT username FROM users WHERE username = '"+username+"'")
      data = data.fetchall()
      names = {name[0] for name in data}
      
      if(username in names):
         check = True
       
       
      if(username is not None and password is not None and email is not None is False):
         db = get_db()
         db.cursor().execute("INSERT INTO users(username,password,email) VALUES (?,?)", (username, spwd))
         db.commit()
         return redirect(url_for('register.html'))
   return render_template('login.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      
      username = request.form['usrname-l']
      password = request.form['psword-1']
      
      db = get_db()
      data = db.cursor().execute("SELECT username, password FROM users WHERE username = '"+username+"'") 
      data = data.fetchall()
      
      password = password.encode('utf-8')
       
      for value in (data):
         if (username == value[0] and value[1].encode('utf-8') == bcrypt.hashpw(password, value[1].encode('utf-8'))):
            session['logged_in'] = True
            session['user'] = username
            return redirect(url_for('base.html'))
   return render_template('base.html')


@app.route('/Send', methods=['GET', 'POST'])
def send():
   if request.method == 'POST':
      
      username = session['user']
      password = session['user-password']      

      db = get_db()
      db.cursor().execute("INSERT INTO users(username, password)", (username, password))
      db.commit()
            

      return redirect(url_for('.root'))
      
@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/highestgrossing')
def highestgrossing():
   con = sql.connect("var/highestgrossing.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from highestgrossing")
   
   rows = cur.fetchall();
   return render_template("highestgrossing.html",rows = rows)

@app.route('/animated')
def animated():
   con = sql.connect("var/animated.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from animated")

   rows = cur.fetchall();
   return render_template("animated.html",rows = rows)

@app.route('/movies2000')
def movies2000():
   con = sql.connect("var/movies2000.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2000")

   rows = cur.fetchall();
   return render_template("movies2000.html",rows = rows)

@app.route('/movies2001')
def movies2001():
   con = sql.connect("var/movies2001.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2001")

   rows = cur.fetchall();
   return render_template("movies2001.html",rows = rows)

@app.route('/movies2002')
def movies2002():
   con = sql.connect("var/movies2002.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2002")

   rows = cur.fetchall();
   return render_template("movies2002.html",rows = rows)

@app.route('/movies2003')
def movies2003():
   con = sql.connect("var/movies2003.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2003")

   rows = cur.fetchall();
   return render_template("movies2003.html",rows = rows)

@app.route('/movies2004')
def movies2004():
   con = sql.connect("var/movies2004.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2004")

   rows = cur.fetchall();
   return render_template("movies2004.html",rows = rows)

@app.route('/movies2005')
def movies2005():
   con = sql.connect("var/movies2005.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2005")

   rows = cur.fetchall();
   return render_template("movies2005.html",rows = rows)

@app.route('/movies2006')
def movies2006():
   con = sql.connect("var/movies2006.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2006")

   rows = cur.fetchall();
   return render_template("movies2006.html",rows = rows)

@app.route('/movies2007')
def movies2007():
   con = sql.connect("var/movies2007.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2007")

   rows = cur.fetchall();
   return render_template("movies2007.html",rows = rows)

@app.route('/movies2008')
def movies2008():
   con = sql.connect("var/movies2008.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2008")

   rows = cur.fetchall();
   return render_template("movies2008.html",rows = rows)

@app.route('/movies2009')
def movies2009():
   con = sql.connect("var/movies2009.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2009")

   rows = cur.fetchall();
   return render_template("movies2009.html",rows = rows)

@app.route('/movies2010')
def movies2010():
   con = sql.connect("var/movies2010.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2010")

   rows = cur.fetchall();
   return render_template("movies2010.html",rows = rows)

@app.route('/movies2011')
def movies2011():
   con = sql.connect("var/movies2011.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2011")

   rows = cur.fetchall();
   return render_template("movies2011.html",rows = rows)

@app.route('/movies2012')
def movies2012():
   con = sql.connect("var/movies2012.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2012")

   rows = cur.fetchall();
   return render_template("movies2012.html",rows = rows)

@app.route('/movies2013')
def movies2013():
   con = sql.connect("var/movies2013.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2013")

   rows = cur.fetchall();
   return render_template("movies2013.html",rows = rows)

@app.route('/movies2014')
def movies2014():
   con = sql.connect("var/movies2014.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2014")

   rows = cur.fetchall();
   return render_template("movies2014.html",rows = rows)

@app.route('/movies2015')
def movies2015():
   con = sql.connect("var/movies2015.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2015")

   rows = cur.fetchall();
   return render_template("movies2015.html",rows = rows)

@app.route('/movies2016')
def movies2016():
   con = sql.connect("var/movies2016.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2016")

   rows = cur.fetchall();
   return render_template("movies2016.html",rows = rows)

@app.route('/movies2017')
def movies2017():
   con = sql.connect("var/movies2017.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2017")

   rows = cur.fetchall();
   return render_template("movies2017.html",rows = rows)

@app.route('/movies2018')
def movies2018():
   con = sql.connect("var/movies2018.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from movies2018")

   rows = cur.fetchall();
   return render_template("movies2018.html",rows = rows)


@app.route('/<string:name>')
def comingsoon(name):
    #return name
    return render_template(name+'.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

