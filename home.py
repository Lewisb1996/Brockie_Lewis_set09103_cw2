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

@app.route('/comingsoon/<string:name>')
def comingsoon(name):
    #return name
    return render_template(name+'.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

