from flask import Flask, Markup, render_template, request, url_for

app = Flask(__name__)
app.config['DEBUG'] = True


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
