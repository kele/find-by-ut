#! /usr/bin/env python2

class Guido:
  def add_function(self, name, args, def_args, filepath, location):
    """
    Args:
      name (string): name of the function
      args ([string]): list of non-default arguments names
      def_args ([string]): list of default arguments names
      filepath (string): full filepath
      location ((int, int)): start line and end line of the function
    """
    raise NotImplementedError

  def search(self, min_args, max_args):
    """
    Args:
      min_args (int): minimum number of arguments that the function should take
      max_args (int or None): maximum number of arguments that the function can take
        None means unlimited number of arguments

    Returns:
      {
        'module' : string,        # name of the module to import
        'name': string,           # name of the function
        'filepath' : string,      # filepath
        'location' : (int, int),  # start line and end line
        'args' : [string],        # names of the non-default arguments
        'def_args': [string]      # names of the default arguments
      }
    """
    raise NotImplementedError
