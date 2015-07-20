import compiler
import json
import os

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
  _recurse_on_node(ast)

def _recurse_on_node(node):
  for child in node.getChildNodes():
    _recurse_on_node(child)
  if isinstance(node, compiler.ast.Function):
    add_to_guido(node)

def add_to_guido(node):
  print node

if __name__ == '__main__':
  scan_config()
