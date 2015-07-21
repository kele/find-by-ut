from flask import Flask, Markup, render_template, request, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

from google.appengine.api import taskqueue

from guido.datastore_guido import DatastoreGuido
from scanner.scanner import scan_config
import dispatcher
from constants import RUNNER_ENDPOINT

import utils

dg = DatastoreGuido()

def get_results(*args, **kwargs):
  return [f.name + "(" + ', '.join(f.args) + ")" for f in dg.search(*args, **kwargs)]

@app.route('/dispatch')
def push():
    disp = dispatcher.Dispatcher()
    disp.dispatch('test!!', '/codebase/small_python_project')
    res = disp.get_results()
    return str(res)

@app.route(RUNNER_ENDPOINT, methods=['POST'])
def work():
    response = dispatcher.Result(matched_functions=['yoyoyo'],
                                 parent=utils.get_result_key_from_id(request.form['id']))
    response.put()
    return 'ok'

@app.route('/scan')
def ingest():
  from scanner.scanner import main as main_scanner
  main_scanner()
  return "Done!"

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
