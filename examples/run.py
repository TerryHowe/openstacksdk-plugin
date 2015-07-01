# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Run Example Plugin

Run this script and it creates a connection loading the openstacksdk_plugin
example.  it prints hello and goodbye which is all the example does.  To keep
things simple, this example only works with os-client-configuration  It
doesn't need to authenticate at all, but it needs to build a proper
connection.

For example:
    python -m examples.run
"""

import os
import sys

import os_client_config

from examples import common
from openstack import connection
from openstack import profile


if __name__ == "__main__":
    os_cloud = os.environ.get('OS_CLOUD', None)
    cloud = os_client_config.OpenStackConfig().get_one_cloud(os_cloud)
    auth = cloud.config['auth']
    prof = profile.Profile(extensions=['openstacksdk_plugin.example'])
    conn = connection.Connection(profile=prof, **auth)
    print conn.example.return_hello()
    print conn.example.return_goodbye()
