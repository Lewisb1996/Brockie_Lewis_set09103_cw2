from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('base.html')

@app.route('/comingsoon/<string:name>')
def comingsoon(name):
    #return name
    return render_template(name+'.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)

