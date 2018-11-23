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


@app.route('/comingsoon/<string:name>')
def comingsoon(name):
    #return name
    return render_template(name+'.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

