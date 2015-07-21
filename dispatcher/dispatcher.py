import os

from google.appengine.api import taskqueue

from guido import DefaultGuido
from constants import RUNNER_ENDPOINT


class Dispatcher(object):

  def __init__(self):
    self._id = self.__make_unique_id()
    self._q = taskqueue.Queue(self.ident)
    self._rpc_list = []

  def __make_unique_id(self):
    return os.environ.get('INSTANCE_ID', '1')

  def dispatch(self, test, repo, path=''):
    regexes = self._make_regexes(repo, path)

    for payload in payloads:
      new_task = taskqueue.Task(payload=payload, url=RUNNER_ENDPOINT)
      self._rpc_list.append(self._q.add_async(new_task))

  def _make_regexes(self, path):
    regexes = []
    for root, dirs, files in os.walk(path):
      for directory in dirs:
          

  def get_results():
    for rpc in self._rpc_list:
      rpc.wait()
