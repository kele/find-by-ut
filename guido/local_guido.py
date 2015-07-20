#! /usr/bin/env python2

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
