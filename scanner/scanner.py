import compiler
import json
import os

from guido import Guido


_GUIDO = Guido()


def scan_config(config_file='codebase.json'):
  config = json.load(open(config_file))
  for root, extensions in config:
    scan_dir(root, extensions)

def scan_dir(path, extensions):
  """Recursively scan the directory located at path."""
  for root, unused_dirs, files in os.walk(path):
    for f in files:
      if any([f.endswith(ext) for ext in extensions]):
        ingest_file(os.path.join(root, f))

def ingest_file(path):
  ast = compiler.parseFile(path)
  visitor = FunctionVisitor(path)
  compiler.walk(ast, visitor)

class FunctionVisitor(compiler.visitor.ASTVisitor):
  def __init__(self, filepath):
    self.filepath = filepath

  def visitFunction(self, node):
    _GUIDO.add_function(name=node.name,
                        args=node.argnames,
                        def_args=node.defaults,
                        filepath=self.filepath,
                        line=node.lineno)

if __name__ == '__main__':
  scan_config()
