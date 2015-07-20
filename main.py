from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

from guido.datastore_guido import DatastoreGuido

dg = DatastoreGuido()

@app.route('/')
def hello():
    dg.add_function("lol", [], [], "file.py", 5)
    dg.add_function("lol2", ['x'], [], "file.py", 10)
    res = dg.search(1)
    return "Results:<br>" + '<br>'.join([f.name for f in res]) + "<br>Results:<br>" + '<br>'.join([f.name for f in dg.search(0)])

