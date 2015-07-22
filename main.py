import json

from flask import Flask, Markup, render_template, request, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

from constants import RUNNER_ENDPOINT
from google.appengine.api import taskqueue
from scanner.scanner import scan_config
from runner.python_runner import PythonRunner
import dispatcher

pr = PythonRunner()
disp = dispatcher.Dispatcher()


@app.route(RUNNER_ENDPOINT, methods=['POST'])
def work():
  regex = request.form.get("regex")
  test = request.form.get("test")

  results = [{'name' : r.name, 'path' : r.filepath } for r in pr.run_bulk(test, regex)]
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


def dispatch(code, regex):
  disp.dispatch(code, regex)
  res = disp.get_results()
  return str(res)

@app.route('/backend', methods=['POST'])
def backend():
  code = request.form['code']
  return render_template('action.html', code=code, result=Markup(dispatch(code, "/codebase")))
