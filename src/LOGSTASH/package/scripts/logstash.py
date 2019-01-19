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


def logstash():
    import params
    #create pid dir
    Directory(
        [params.logstash_base_dir],
        mode=0755,
        cd_access='a',
        owner=params.logstash_user,
        group=params.logstash_group,
        create_parents=True
    )
    File(params.logstash_install_log,
         mode=0644,
         owner=params.logstash_user,
         group=params.logstash_group,
         content=''
         )
    File(format("/etc/sysconfig/logstash"),
               owner="root",
               group="root",
               content=Template("logstash.j2")
        )
    File(format("/etc/systemd/system/logstash.service"),
               owner="root",
               group="root",
               content=Template("logstash.service.j2")
        )
