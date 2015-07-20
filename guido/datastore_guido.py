import guido

from google.appengine.ext import ndb

class FunctionMetadata(ndb.Model):
  name = ndb.StringProperty()
  args = ndb.JsonProperty()
  num_of_args = ndb.IntegerProperty()
  def_args = ndb.JsonProperty()
  num_of_def_args = ndb.IntegerProperty()
  filepath = ndb.StringProperty()
  location_start = ndb.IntegerProperty()
  location_end = ndb.IntegerProperty()

class DatastoreGuido(guido.Guido):
  def add_function(self, name, args, def_args, filepath, location):
    f = FunctionMetadata(
        name=name,
        args=args,
        num_of_args=len(args),
        def_args=def_args,
        num_of_def_args=len(def_args),
        filepath=filepath
        location_start=location[0],
        location_end=location[1])
    f.put()

  def search(self, num_args):
    q = FunctionMetadata.query(FunctionMetadata.num_of_args <= num_args)
    return [f for f in q.fetch() if f.num_of_args + f.num_of_def_args >= num_args]
