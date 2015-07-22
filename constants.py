import os

RUNNER_ENDPOINT = '/runner'
RESULT_KEYNAME = 'RESULT'
HOST = 'localhost:8080' if os.environ.get('INSTANCE_ID') == '0' else 'hackaton-1009.appspot.com'
