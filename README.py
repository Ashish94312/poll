# poll
from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/<name>')
def index(name):
  return "hello {}".format(name)

@app.route('/add/<num1>/<num2>')
def add(num1,num2):
  return '{} + {} = {}'.format(num1, num2, num1+num2)
app.run(debug=True)
