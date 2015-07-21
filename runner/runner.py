#! /usr/bin/env python2

class Runner:
  @staticmethod
  def get_supported_languages():
    """
    Returns:
      [string]: list of supported languages
    """

    return []

  def run(self, test, env):
    """
    Execute the test in a specified environment.

    Args:
      test (string): the test code
      env (implementation specific): environment to run the test

    Returns:
      bool: result of the test
    """

    raise NotImplementedError



