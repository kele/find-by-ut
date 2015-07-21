import compiler
import json
import logging
import os

from guido import DefaultGuido


_GUIDO = DefaultGuido()
_DEFAULT_CONFIG = os.path.join(os.path.dirname(__file__), 'fake-codebase.json')

def scan_config(config_file=_DEFAULT_CONFIG):
  config = json.load(open(config_file))
  for root, extensions in config:
    scan_dir(root, extensions)

def scan_dir(path, extensions):
  """Recursively scan the directory located at path."""
  logging.warning(path)
  for root, unused_dirs, files in os.walk(path):
    for f in files:
      if any([f.endswith(ext) for ext in extensions]):
        try:
          ingest_file(os.path.join(root, f))
        except Exception as e:
          logging.warning(e.message)

def ingest_file(path):
  ast = compiler.parseFile(path)
  visitor = FunctionVisitor(path)
  compiler.walk(ast, visitor)

class FunctionVisitor(compiler.visitor.ASTVisitor):
  def __init__(self, filepath):
    self.filepath = filepath

  def visitFunction(self, node):
    num_defaults = len(node.defaults)
    _GUIDO.add_lazy(name=node.name,
                    args=node.argnames[:-num_defaults],
                    def_args=node.argnames[-num_defaults:],
                    filepath=self.filepath,
                    location=node.lineno)

def main():
  scan_config()
  _GUIDO.flush()

if __name__ == '__main__':
  main()
