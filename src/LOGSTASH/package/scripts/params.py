from resource_management import *

# service config
config = Script.get_config()
tmp_dir = Script.get_tmp_dir()

logstash_user = "root"
logstash_group = "root"
logstash_base_dir = config['configurations']['logstash-config']['logstash_base_dir']
logstash_download = config['configurations']['logstash-config']['logstash_download']
logstash_install_log = logstash_base_dir + "/logstash_install.log"


# logstash java_home

java_home = config['configurations']['logstash-config']['java_home']


# logstash.conf
logstash_conf = config['configurations']['logstash-config']['logstash.conf']