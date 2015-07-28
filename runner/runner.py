#! /usr/bin/env python2
#
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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



