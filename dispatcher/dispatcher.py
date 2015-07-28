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
import urllib
import json

from google.appengine.api import taskqueue, urlfetch
from google.appengine.ext import ndb

from guido import DefaultGuido
from constants import RUNNER_ENDPOINT
from constants import RESULT_KEYNAME
from constants import HOST

class Dispatcher(object):

  def __init__(self):
    self._rpc_pool = []

  def dispatch(self, test, path):
    regexes = self._make_regexes(path)
    payloads = [{'test': test, 'regex':reg} for reg in regexes]

    rpc_pool = []
    for payload in payloads:
      encoded_payload = urllib.urlencode(payload)
      rpc = urlfetch.create_rpc()
      urlfetch.make_fetch_call(rpc,
                               'http://{host}{runner}'.format(host=HOST, runner=RUNNER_ENDPOINT),
                               payload=encoded_payload,
                               method=urlfetch.POST)
      self._rpc_pool.append(rpc)

  def _make_regexes(self, path):
    regexes = []
    for root, dirs, files in os.walk(path):
      for directory in dirs:
        path_to_dir = os.path.join(root, directory)
        regex = r'{path}/[^/]*.py'.format(path=path_to_dir)
        regexes.append(regex)
    return regexes

  def get_results(self):
    matched_functions = []
    for rpc in self._rpc_pool:
      result = rpc.get_result()
      if result.status_code == 200:
        json_res = json.loads(result.content)
        matched_functions.extend(json_res)
    self._rpc_pool = []
    return matched_functions
