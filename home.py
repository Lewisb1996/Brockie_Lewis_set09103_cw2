from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def root():
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


@app.route('/comingsoon/<string:name>')
def comingsoon(name):
    #return name
    return render_template(name+'.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

