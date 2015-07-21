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
  def __init__(self, cache_limit = 100000):
    self.cache_limit = cache_limit
    self.cache = []

  def add_lazy(self, name, args, def_Args, filepath, location):
    f = FunctionMetadata(
        name=name,
        args=args,
        num_of_args=len(args),
        def_args=def_args,
        num_of_def_args=len(def_args),
        filepath=filepath,
        location=location)
    self.cache.append(f)

    if len(self.cache) >= self.cache_limit:
      self.flush()

  def add(self, name, args, def_args, filepath, location):
    self.add_lazy(name, args, def_args, filepath, location)
    self.flush()

  def flush(self):
    for f in self.cache:
      q = FunctionMetadata.query(f.name == name)
      q = q.filter(f.filepath == filepath).get()
      if q:
        return
      f.put()

    self.cache = []

  def search(self, num_args):
    q = FunctionMetadata.query(FunctionMetadata.num_of_args <= num_args)
    return [f for f in q.fetch() if f.num_of_args + f.num_of_def_args >= num_args]
