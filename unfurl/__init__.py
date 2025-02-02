# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "Ryan Benson"
__version__ = "2021.06.15"
__email__ = "ryan@dfir.blog"

import logging
import sys

log = logging.getLogger(__name__)
log.setLevel('WARNING')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s.%(msecs).03d | %(name)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
log.addHandler(handler)
