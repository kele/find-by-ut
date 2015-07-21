#! /usr/bin/env python2

from runner import Runner
import imp
import os
import re
import sys
import compiler

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
      print "Unexpected error: " + sys.exec_info()[0]
      return False

  def run_bulk(self, test_body, file_regex):
    num_args = self._get_num_args(test_body)
    if num_args < 0:
      raise ValueError

    functions = _GUIDO.search(num_args, file_regex)
    good = [f in functions if self.run(test_body, { "filepath" : f.filepath, "name" : f.name })]
    return good


  @staticmethod
  def _get_num_args(test_body):

    class FunctionVisitor(compiler.visitor.ASTVisitor):
      def __init__(self):
        self.num_args = -1

      def visitCallFunc(self, node):
        if node.node.name == "FUNCTION":
          self.num_args = len(node.args)

    ast = compiler.parse(test_body)
    visitor = CallVisitor()
    compiler.walk(ast, visitor)
    return visitor.num_args

  @staticmethod
  def _fill_test(test, filepath, function_name):
    # TODO: should the import be somehow unimported?
    return """
FUNCTION = imp.load_source("imported_modulename", "{filepath}").{function_name}
""".format(filepath=filepath, function_name=function_name) + test


