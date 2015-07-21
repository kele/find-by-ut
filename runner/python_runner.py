#! /usr/bin/env python2

from runner import Runner
import imp

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
      raise


  @staticmethod
  def _fill_test(test, filepath, function_name):
    return """
FUNCTION = imp.load_source("imported_modulename", "{filepath}").{function_name}
""".format(filepath=filepath, function_name=function_name) + test


