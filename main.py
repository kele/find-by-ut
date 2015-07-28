#
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json

from flask import Flask, Markup, render_template, request, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

import constants
from google.appengine.api import taskqueue
from scanner.scanner import scan_config
from runner.python_runner import PythonRunner
import dispatcher

pr = PythonRunner()
disp = dispatcher.Dispatcher()


@app.route(constants.RUNNER_ENDPOINT, methods=['POST'])
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


@app.route('/')
def frontend():
  return render_template('submit.html')


def dispatch(code, regex):
  disp.dispatch(code, regex)
  return disp.get_results()

@app.route('/backend', methods=['POST'])
def backend():
  code = request.form['code']
  code = '\n'.join([c.rstrip() for c in code.split('\n')])
  return render_template('action.html', code=code, result=dispatch(code, "/codebase"))

@app.route('/info')
def info():
  return """
RUNNER_ENDPOINT = {RUNNER_ENDPOINT}<br>
RESULT_KEYNAME = {RESULT_KEYNAME}<br>
SERVER_SOFTWARE = {SERVER_SOFTWARE}<br>
IS_PRODUCTION = {IS_PRODUCTION}<br>
DEFAULT_VERSION_HOSTNAME = {DEFAULT_VERSION_HOSTNAME}<br>
HOST = {HOST}""".format(RUNNER_ENDPOINT=constants.RUNNER_ENDPOINT,
                        RESULT_KEYNAME=constants.RESULT_KEYNAME,
                        SERVER_SOFTWARE=constants.SERVER_SOFTWARE,
                        IS_PRODUCTION=constants.IS_PRODUCTION,
                        HOST=constants.HOST,
                        DEFAULT_VERSION_HOSTNAME=constants.DEFAULT_VERSION_HOSTNAME)
