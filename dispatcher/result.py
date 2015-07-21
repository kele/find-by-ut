from google.appengine.ext import ndb

class Result(ndb.Model):
  matched_functions = ndb.JsonProperty()
