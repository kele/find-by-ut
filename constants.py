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
import os

from google.appengine.api.app_identity.app_identity import get_default_version_hostname

RUNNER_ENDPOINT = '/runner'
RESULT_KEYNAME = 'RESULT'
SERVER_SOFTWARE = os.environ.get('SERVER_SOFTWARE')
IS_PRODUCTION = SERVER_SOFTWARE.startswith('Google')
DEFAULT_VERSION_HOSTNAME = get_default_version_hostname()
HOST = 'hackaton-1009.appspot.com' if IS_PRODUCTION else 'localhost:8080'
