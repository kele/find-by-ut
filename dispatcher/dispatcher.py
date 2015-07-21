import os

from google.appengine.api import taskqueue
from google.appengine.ext import ndb

from guido import DefaultGuido
from constants import RUNNER_ENDPOINT
from constants import RESULT_KEYNAME
from result import Result
import utils

class Dispatcher(object):

  def __init__(self):
    self._id = self.__make_unique_id()
    self._rpc_list = []

  def __make_unique_id(self):
    return os.environ.get('INSTANCE_ID', '1')

  def dispatch(self, test, path):
    regexes = self._make_regexes(path)
    payloads = [{'id': self._id, 'test': test, 'regex':reg} for reg in regexes]

    for payload in payloads:
      new_task = taskqueue.Task(params=payload, url=RUNNER_ENDPOINT)
      self._rpc_list.append(new_task.add_async())

  def _make_regexes(self, path):
    regexes = []
    for root, dirs, files in os.walk(path):
      for directory in dirs:
        path_to_dir = os.path.join(root, directory)
        regex = r'{path}/[^/]*.py'.format(path=path_to_dir)
        regexes.append(regex)
    return regexes

  def get_results(self):
    for rpc in self._rpc_list:
      rpc.wait()

    key = utils.get_result_key_from_id(self._id)
    res_query = Result.query(ancestor=key)

    matched_functions = []
    for result in res_query:
      for func in result.matched_functions:
        matched_functions.append(func)
    return matched_functions
