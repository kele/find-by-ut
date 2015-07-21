import compiler
import json
import logging
import os

from guido import DefaultGuido


_GUIDO = DefaultGuido()
_DEFAULT_CONFIG = os.path.join(os.path.dirname(__file__), 'fake_codebase.json')

def scan_config(config_file=_DEFAULT_CONFIG):
  config = json.load(open(config_file))
  count = 0
  for root, extensions in config:
    count += scan_dir(root, extensions)
  return count

def scan_dir(path, extensions):
  count = 0
  """Recursively scan the directory located at path."""
  logging.warning(path)
  for root, unused_dirs, files in os.walk(path):
    for f in files:
      if any([f.endswith(ext) for ext in extensions]):
        try:
          count += ingest_file(os.path.join(root, f))
        except Exception as e:
          logging.warning(e.message)
  return count

def ingest_file(path):
  ast = compiler.parseFile(path)
  visitor = FunctionVisitor(path)
  compiler.walk(ast, visitor)
  return visitor.count

class FunctionVisitor(compiler.visitor.ASTVisitor):
  def __init__(self, filepath):
    self.filepath = filepath
    self.count = 0

  def visitFunction(self, node):
    num_defaults = len(node.defaults)
    _GUIDO.add_lazy(name=node.name,
                    args=node.argnames[:-num_defaults],
                    def_args=node.argnames[-num_defaults:],
                    filepath=self.filepath,
                    location=node.lineno)
    self.count += 1

def main():
  count = scan_config()
  _GUIDO.flush()
  return count

if __name__ == '__main__':
  main()
