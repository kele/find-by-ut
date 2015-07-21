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
    return os.environ.get('INSTANCE_ID')

  def dispatch(self, test, repo, path):
    payloads = self._make_payloads(repo, path)

    for payload in payloads:
      new_task = taskqueue.Task(payload=payload, url=RUNNER_ENDPOINT)
      self._rpc_list.append(self._q.add_async(new_task))

  def get_results():
    for rpc in self._rpc_list:
      rpc.wait()
