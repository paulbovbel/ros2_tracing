# Copyright 2020 Christophe Bedard
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

"""Utilities for selecting the right babeltrace version."""

from importlib import util
from types import ModuleType


def get_babeltrace_impl() -> ModuleType:
    """
    Get a babeltrace implementation module, depending on what version is available.

    :return: the babeltrace implementation module
    """
    bt1_found = util.find_spec('babeltrace') is not None
    bt2_found = util.find_spec('bt2') is not None
    if not bt1_found and not bt2_found:
        raise ModuleNotFoundError('could not find any babeltrace version')
    if bt1_found:
        print('babeltrace1 found')
    from . import babeltrace1
    return babeltrace1
