# poll
from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/<name>')
def index(name):
  return "hello {}".format(name)
app.run()
