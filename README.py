# poll
from flask import Flask
from fask import render_template
app=Flask(__name__)
@app.route('/')
@app.route('/<name>')
def index(name):
  return "hello {}".format(name)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
#def add(num1,num2):
 # return '{} + {} = {}'.format(num1, num2, num1+num2)
def add(num1,num2):
  return render_template("add.html")
app.run(debug=True)
