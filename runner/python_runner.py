#! /usr/bin/env python2
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

from runner import Runner
import imp
import os
import re
import sys
import compiler

from guido.datastore_guido import DatastoreGuido as Guido

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
    except AssertionError:
      return False
    except:
      return False

  def run_bulk(self, test_body, file_regex):
    num_args = self._get_num_args(test_body)
    if num_args < 0:
      raise ValueError

    functions = _GUIDO.search(num_args, file_regex)
    good = [f for f in functions if self.run(test_body, { "filepath" : f.filepath, "name" : f.name })]
    return good


  @staticmethod
  def _get_num_args(test_body):

    class CallVisitor(compiler.visitor.ASTVisitor):
      def __init__(self):
        self.num_args = -1

      def visitCallFunc(self, node):
        try:
          if node.node.name == "FUNCTION":
            self.num_args = len(node.args)
        except:
          pass

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


