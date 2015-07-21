#! /usr/bin/env python2

class Guido:
  def add_lazy(self, name, args, def_args, filepath, location):
    """
    Eventually add entry to Guido. Use flush() afterwards.

    Args:
      name (string): name of the function
      args ([string]): list of non-default arguments names
      def_args ([string]): list of default arguments names
      filepath (string): full filepath
      location (int): start line and end line of the function
    """
    raise NotImplementedError

  def add(self, name, args, def_args, filepath, location):
    """
    The same as add_lazy, but flush() afterwards immediately.
    """
    raise NotImplementedError

  def flush(self):
    """
    Flushses the buffer filled with add_lazy() calls.
    """
    raise NotImplementedError

  def search(self, num_args, file_regex=None):
    """
    Args:
      num_args (int): number of arguments that the function should be able to take
      file_regex (string): regex to filter filepath

    Returns:
      Object with following properties:
        module : string,        # name of the module to import
        name: string,           # name of the function
        filepath : string,      # filepath
        location : (int, int),  # start line and end line
        args : [string],        # names of the non-default arguments
        def_args: [string]      # names of the default arguments
    """
    raise NotImplementedError
