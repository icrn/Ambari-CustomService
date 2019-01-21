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
from resource_management.libraries.functions.check_process_status import check_process_status

class Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        self.install_packages(env)
        logstash()
        self.configure(env)

    def configure(self, env):
        import params
        File(format("/etc/logstash/logstash.conf"),
               owner=params.logstash_user,
               group=params.logstash_group,
               content=Template("logstash.conf.j2")
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
        reload_cmd = format("systemctl daemon-reload")
        Execute(reload_cmd)

        Execute('echo "Configuration complete"')

    def stop(self, env):
        stop_cmd = format("service logstash stop")
        Execute(stop_cmd)
        Execute('echo "stop complete"')

    def status(self, env):
        print "check start"
        os.system(r"ps -ef | grep org.logstash.Logstash | grep -v grep | awk '{print $2}' > /var/run/logstash.pid")

        import status_params
        env.set_params(status_params)
        check_process_status(status_params.logstash_pid_file)

    def start(self, env):
        start_cmd = format("service logstash start")
        print "check start"
        Execute(start_cmd)

if __name__ == "__main__":
    Master().execute()
