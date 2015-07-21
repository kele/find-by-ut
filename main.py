from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True
from google.appengine.api.taskqueue import Queue, Task
from google.appengine.api import taskqueue

from guido.datastore_guido import DatastoreGuido
from scanner.scanner import scan_config

dg = DatastoreGuido()

def get_results(*args, **kwargs):
  return [f.name + "(" + ', '.join(f.args) + ")" for f in dg.search(*args, **kwargs)]

@app.route('/push')
def push():
    q = Queue()
    task = Task(url='/work')
    rpc = q.add_async(task)
    return str(rpc.get_result())
    # taskqueue.add(url='/work')
    # return 'meow'

@app.route('/work', methods=['POST'])
def work():
    return 'helloworld'

@app.route('/ingest')
def ingest():
  from scanner.scanner import main as main_scanner
  main_scanner()
  return "Done!"

@app.route('/')
def hello():
    dg.add_lazy("lol", [], [], "file.py", 5)
    dg.add_lazy("lol1", ['x'], [], "file.py", 10)
    dg.add_lazy("lol2", ['y'], [], "/this/funny/dir/file.py", 10)
    dg.add_lazy("lol3", ['z'], [], "/this/funny/dir/file.py", 10)
    dg.add_lazy("lol4", ['q'], [], "/this/notfunny/dir/file.py", 10)
    dg.flush()


    res1 = '<br>'.join(get_results(num_args=0))
    res2 = '<br>'.join(get_results(num_args=1, file_regex=".*this.*"))
    res3 = '<br>'.join(get_results(num_args=1, file_regex=".*notfunny.*"))
    res = '<hr>'.join([res1, res2, res3])
    return res

@app.route('/runner')
def run():
  from runner.python_runner import PythonRunner
  r = PythonRunner()

  test = """
assert(FUNCTION('xyz') == 'zyx')
"""
  good = r.run_bulk(test, "codebase/.*")

  return '<br>'.join([g.name for g in good])
