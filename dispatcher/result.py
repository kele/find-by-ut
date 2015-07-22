from google.appengine.ext import ndb

class Result(ndb.Model):
  _use_cache = False
  matched_functions = ndb.JsonProperty()
