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

import sys
import os
import glob
import pwd
import grp
import signal
import time
from resource_management import *
from logstash import logstash


class Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        self.install_packages(env)
        logstash()
        self.configure(env)
        reload_cmd = format("systemctl daemon-reload")
        Execute(reload_cmd)

    def configure(self, env):
        import params
        File(format("/etc/logstash/logstash.conf"),
               owner=params.logstash_user,
               group=params.logstash_group,
               content=Template("logstash.conf.j2")
        )
        Execute('echo "Configuration complete"')

    def stop(self, env):
        stop_cmd = format("service logstash stop")
        Execute(stop_cmd)
        Execute('echo "stop complete"')

    def start(self, env):
        stop_cmd = format("service logstash start")
        Execute(stop_cmd)
        Execute('echo "start complete"')

    def status(self, env):
        stop_cmd = format("service logstash status")
        print "check status"
        Execute(stop_cmd)

if __name__ == "__main__":
    Master().execute()
