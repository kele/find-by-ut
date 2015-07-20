from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'
