#! /usr/bin/env python2

from runner import Runner
import imp
import os
import re
import sys

from guido import Guido

_GUIDO = Guido()

class PythonRunner(Runner):
  @staticmethod
  def get_supported_languages():
    return ["python"]

  def run(self, test, env):
    ready_to_run = self._fill_test(test, env["filepath"], env["name"])
    try:
      exec(ready_to_run)
      return True
    except:
      print "Unexpected error: " sys.exec_info()[0]
      return False

  def run_bulk(self, test_body, num_args, file_regex):
    functions = _GUIDO.search(num_args, file_regex)
    good = [f in functions if self.run(test_body, { "filepath" : f.filepath, "name" : f.name })]
    return good

  @staticmethod
  def _fill_test(test, filepath, function_name):
    # TODO: should the import be somehow unimported?
    return """
FUNCTION = imp.load_source("imported_modulename", "{filepath}").{function_name}
""".format(filepath=filepath, function_name=function_name) + test


