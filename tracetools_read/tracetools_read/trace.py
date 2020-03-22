# Copyright 2019 Robert Bosch GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module with functions for reading traces."""

import os
from typing import List

from . import DictEvent
from .babeltrace import get_babeltrace_impl


impl = get_babeltrace_impl()


def is_trace_directory(path: str) -> bool:
    """
    Check recursively if a path is a trace directory.

    :param path: the path to check
    :return: `True` if it is a trace directory, `False` otherwise
    """
    path = os.path.expanduser(path)
    if not os.path.isdir(path):
        return False
    return impl.is_trace_directory(path)


def get_trace_events(trace_directory: str) -> List[DictEvent]:
    """
    Get the events of a trace.

    :param trace_directory: the path to the main/top trace directory
    :return: events
    """
    return impl.get_trace_events(trace_directory)
