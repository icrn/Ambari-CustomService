#!/usr/bin/env python
"""
Redis service params

"""

from resource_management import *

config = Script.get_config()

grafana_pid_file = format("/var/run/grafana/grafana.pid")
