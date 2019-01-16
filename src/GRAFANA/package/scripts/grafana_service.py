import sys, os, pwd, signal, time
from resource_management import *
from resource_management.core import sudo
from resource_management.core.exceptions import ComponentIsNotRunning
from resource_management.core.logger import Logger
from subprocess import call
from grafana import grafana

class grafana_service(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml

    self.install_packages(env)
    self.configure(env)

  def configure(self, env):
    import params
    env.set_params(params)
    grafana()

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    stop_cmd = format("service grafana-server stop")
    Execute(stop_cmd)

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    import status_params
    env.set_params(status_params)
    self.configure(env)
    start_cmd = format('service grafana-server start')
    Execute(start_cmd)

  #To get status of the, use the linux service status command
  def status(self, env):
    import status_params
    env.set_params(status_params)
    status_cmd = format("service grafana-server status")
    Execute(status_cmd)
    
if __name__ == "__main__":
    grafana_service().execute()