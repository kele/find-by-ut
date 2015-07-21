import guido

from google.appengine.ext import ndb

class FunctionMetadata(ndb.Model):
  name = ndb.StringProperty()
  args = ndb.JsonProperty()
  num_of_args = ndb.IntegerProperty()
  def_args = ndb.JsonProperty()
  num_of_def_args = ndb.IntegerProperty()
  filepath = ndb.StringProperty()
  location = ndb.IntegerProperty()


class DatastoreGuido(guido.Guido):
  def __init__(self, buffer_limit = 100000):
    self.buffer_limit = buffer_limit
    self.buffer = []

  def add_lazy(self, name, args, def_Args, filepath, location):
    f = FunctionMetadata(
        name=name,
        args=args,
        num_of_args=len(args),
        def_args=def_args,
        num_of_def_args=len(def_args),
        filepath=filepath,
        location=location)
    self.buffer.append(f)

    if len(self.buffer) >= self.buffer_limit:
      self.flush()

  def add(self, name, args, def_args, filepath, location):
    self.add_lazy(name, args, def_args, filepath, location)
    self.flush()

  def flush(self):
    for f in self.buffer:
      q = FunctionMetadata.query(f.name == name)
      q = q.filter(f.filepath == filepath).get()
      if q:
        return
      f.put()

    self.buffer = []

  def search(self, num_args):
    q = FunctionMetadata.query(FunctionMetadata.num_of_args <= num_args)
    return [f for f in q.fetch() if f.num_of_args + f.num_of_def_args >= num_args]
