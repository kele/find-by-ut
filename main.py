import json

from flask import Flask, Markup, render_template, request, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

from constants import RUNNER_ENDPOINT
from google.appengine.api import taskqueue
from scanner.scanner import scan_config
import dispatcher

@app.route('/dispatch')
def push():
    disp = dispatcher.Dispatcher()
    disp.dispatch('test!!', '/codebase/small_python_project')
    res = disp.get_results()
    return str(res)

@app.route(RUNNER_ENDPOINT, methods=['POST'])
def work():
    # Do some work here and find a list of function ids that work.
    results = ['123', '456', '789']
    return json.dumps(results)

@app.route('/scan')
def ingest():
  from scanner.scanner import main as main_scanner
  count = main_scanner()
  return "Done! Number of scanned entries: " + str(count)

def run(code):
  from runner.python_runner import PythonRunner
  r = PythonRunner()
  good = r.run_bulk(code, ".*")
  return '<br>'.join([g.name + " @ " + g.filepath for g in good])

@app.route('/')
def frontend():
  return render_template('submit.html')

@app.route('/backend', methods=['POST'])
def backend():
  code = request.form['code']
  return render_template('action.html', code=code, result=Markup(run(code)))
