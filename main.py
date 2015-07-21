from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

from guido.datastore_guido import DatastoreGuido

dg = DatastoreGuido()


def get_results(*args, **kwargs):
  return [f.name + "(" + ', '.join(f.args) + ")" for f in dg.search(*args, **kwargs)]

@app.route('/')
def hello():
    dg.add_lazy("lol", [], [], "file.py", 5)
    dg.add_lazy("lol1", ['x'], [], "file.py", 10)
    dg.add_lazy("lol2", ['y'], [], "/this/funny/dir/file.py", 10)
    dg.add_lazy("lol3", ['z'], [], "/this/funny/dir/file.py", 10)
    dg.add_lazy("lol4", ['q'], [], "/this/notfunny/dir/file.py", 10)
    dg.flush()


    res1 = '<br>'.join(get_results(num_args=0))
    res2 = '<br>'.join(get_results(num_args=1, directory_regex=".*this.*"))
    res3 = '<br>'.join(get_results(num_args=1, directory_regex=".*notfunny.*"))
    res = '<hr>'.join([res1, res2, res3])
    return res
