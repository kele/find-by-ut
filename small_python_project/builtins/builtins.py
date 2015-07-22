import sys

def builtin_abs(number):
  return abs(number)

def builtin_all(iterable):
  return all(iterable)

def builtin_any(iterable):
  return any(iterable)

def builtin_bin(number):
  return bin(number)

def builtin_callable(object):
  return callable(object)

def builtin_chr(i):
  return chr(i)

def builtin_cmp(x, y):
  return cmp(x, y)

def builtin_dir(object=None):
  return dir(object)

def builtin_divmod(x, y):
  return divmod(x, y)

def builtin_filter(function_or_none, sequence):
  return filter(function_or_none, sequence)

def builtin_getattr(object, name, default=None):
  return getattr(object, name, default)

def builtin_globals():
  return globals()

def builtin_hasattr(object, name):
  return hasattr(object, name)

def builtin_hash(object):
  return hash(object)

def builtin_hex(number):
  return hex(number)

def builtin_id(object):
  return id(object)

def builtin_isinstance(object, class_or_type_or_tuple):
  return isinstance(object, class_or_type_or_tuple)

def builtin_issubclass(C, B):
  return issubclass(C, B)

def builtin_iter(o, sentinel=None):
  return iter(o, sentinel)

def builtin_len(object):
  return len(object)

def builtin_locals():
  return locals()

def builtin_map(function, sequence, *sequence_1):
  return map(function, sequence, *sequence_1)

def builtin_next(iterator, default=None):
  return next(iterator, default)

def builtin_oct(number):
  return oct(number)

def builtin_ord(c):
  return ord(c)

def builtin_pow(x, y, z=None):
  return pow(x, y, z)

def builtin_range(start, stop=None, step=None):
  return range(start, stop, step)

def builtin_reduce(function, sequence, initial=None):
  return reduce(function, sequence, initial)

def builtin_repr(object):
  return repr(object)

def builtin_round(number, ndigits=None):
  return round(number, ndigits)

def builtin_unichr(i):
  return unichr(i)

def builtin_vars(object=None):
  return vars(object=None)

def builtin_zip(*iterables):
  return zip(*iterables)

def builtin_str(o):
  return str(o)

def builtin_sorted(iterable):
  return sorted(iterable)

def builtin_enumerate(sequence, start=0):
  return enumerate(sequence, start)
