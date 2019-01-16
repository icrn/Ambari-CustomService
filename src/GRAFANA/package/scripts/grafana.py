#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
from resource_management.libraries.resources.properties_file import PropertiesFile
import sys, os


def grafana():
    import params
    #create pid dir
    Directory([params.grafana_pid_dir],
            owner=params.grafana_user,
            group=params.grafana_group,
            recursive=True
    )

    Directory([params.conf_dir],
            owner=params.grafana_user,
            group=params.grafana_group,
            recursive=True
    )

    #create config file
    File(format("{conf_dir}/grafana.ini"),
               owner=params.grafana_user,
               group=params.grafana_group,
               content=Template("grafana.ini.j2")
        )
    File(format("{conf_dir}/ldap.toml"),
               owner=params.grafana_user,
               group=params.grafana_group,
               content=Template("ldap.toml.j2")
        )
    File(format("/etc/default/grafana-server"),
               owner=params.grafana_user,
               group=params.grafana_group,
               content=Template("grafana-server.j2")
        )

