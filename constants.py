import os

from google.appengine.api.app_identity.app_identity import get_default_version_hostname

RUNNER_ENDPOINT = '/runner'
RESULT_KEYNAME = 'RESULT'
SERVER_SOFTWARE = os.environ.get('SERVER_SOFTWARE')
IS_PRODUCTION = SERVER_SOFTWARE.startswith('Google')
DEFAULT_VERSION_HOSTNAME = get_default_version_hostname()
HOST = get_default_version_hostname() if IS_PRODUCTION else 'localhost:8080'
