from google.appengine.ext import ndb

from constants import RESULT_KEYNAME

def get_result_key_from_id(ident):
  return ndb.Key(RESULT_KEYNAME, ident)
