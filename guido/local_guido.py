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

import guido
import os

class LocalGuido(guido.Guido):
  def __init__(self):
    self.codebase = []

  def add_function(self, name, args, def_args, filepath, location):

    module = os.path.basename(filepath)
    module = os.path.splitext(module)[0]

    self.codebase.append({
        'name' : name,
        'args' : args,
        'def_args' : def_args,
        'filepath' : filepath,
        'location' : location,
        'module' : module
        })

  def search(self, num_args):
    # TODO: actually use num_args :)
    return self.codebase
