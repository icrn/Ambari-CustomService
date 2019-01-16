#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License") you may not use this file except in compliance
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
from resource_management.libraries.resources.template_config import TemplateConfig

import json

# server configurations
root_user="root"
root_group="root"


config = Script.get_config()

grafana_user = config['configurations']['grafana-env']['GRAFANA_USER']
grafana_group = config['configurations']['grafana-env']['GRAFANA_GROUP']
grafana_home = config['configurations']['grafana-env']['GRAFANA_HOME']
log_dir = config['configurations']['grafana-env']['LOG_DIR']
data_dir = config['configurations']['grafana-env']['DATA_DIR']
max_open_files = config['configurations']['grafana-env']['MAX_OPEN_FILES']
conf_dir = config['configurations']['grafana-env']['CONF_DIR']
conf_file = config['configurations']['grafana-env']['CONF_FILE']
restart_on_upgrade = config['configurations']['grafana-env']['RESTART_ON_UPGRADE']
grafana_pid_dir = config['configurations']['grafana-env']['grafana_pid_dir']

#grafana config
app_mode = config['configurations']['grafana-conf']['app_mode']
data = config['configurations']['grafana-conf']['data']
logs = config['configurations']['grafana-conf']['logs']
protocol = config['configurations']['grafana-conf']['protocol']
http_addr =config['configurations']['grafana-conf']['http_addr']
http_port = config['configurations']['grafana-conf']['http_port']
domain = config['configurations']['grafana-conf']['domain']

enforce_domain = str(config['configurations']['grafana-conf']['enforce_domain']).lower()

root_url = config['configurations']['grafana-conf']['root_url']

router_logging = str(config['configurations']['grafana-conf']['router_logging']).lower()

static_root_path = config['configurations']['grafana-conf']['static_root_path']

enable_gzip = str(config['configurations']['grafana-conf']['enable_gzip']).lower()

cert_file =config['configurations']['grafana-conf']['cert_file']
cert_key =config['configurations']['grafana-conf']['cert_key']

database_type = config['configurations']['grafana-conf']['database_type']
database_host = config['configurations']['grafana-conf']['database_host']
database_name = config['configurations']['grafana-conf']['database_name']
database_user = config['configurations']['grafana-conf']['database_user']
database_password = config['configurations']['grafana-conf']['database_password']

database_ssl_mode = str(config['configurations']['grafana-conf']['database_ssl_mode']).lower()

database_path = config['configurations']['grafana-conf']['database_path']

provider = config['configurations']['grafana-conf']['provider']
provider_config = config['configurations']['grafana-conf']['provider_config']

cookie_name = config['configurations']['grafana-conf']['cookie_name']
cookie_secure = str(config['configurations']['grafana-conf']['cookie_secure']).lower()

session_life_time = config['configurations']['grafana-conf']['session_life_time']

reporting_enabled = str(config['configurations']['grafana-conf']['reporting_enabled']).lower()

google_analytics_ua_id = str(config['configurations']['grafana-conf']['google_analytics_ua_id']).lower()

admin_user = config['configurations']['grafana-conf']['admin_user']

admin_password = config['configurations']['grafana-conf']['admin_password']

secret_key = config['configurations']['grafana-conf']['secret_key']

login_remember_days = config['configurations']['grafana-conf']['login_remember_days']
cookie_username = config['configurations']['grafana-conf']['cookie_username']
cookie_remember_name = config['configurations']['grafana-conf']['cookie_remember_name']

disable_gravatar = str(config['configurations']['grafana-conf']['disable_gravatar']).lower()

allow_sign_up = str(config['configurations']['grafana-conf']['allow_sign_up']).lower()

allow_org_create = str(config['configurations']['grafana-conf']['allow_org_create']).lower()

auto_assign_org = str(config['configurations']['grafana-conf']['auto_assign_org']).lower()

auto_assign_org_role = config['configurations']['grafana-conf']['auto_assign_org_role']


auth_anonymous_enabled = str(config['configurations']['grafana-auth']['auth_anonymous_enabled']).lower()

auth_anonymous_org_name = config['configurations']['grafana-auth']['auth_anonymous_org_name']
auth_anonymous_org_role = config['configurations']['grafana-auth']['auth_anonymous_org_role']

auth_github_enabled = str(config['configurations']['grafana-auth']['auth_github_enabled']).lower()
auth_github_allow_sign_up = str(config['configurations']['grafana-auth']['auth_github_allow_sign_up']).lower()
auth_github_client_id = config['configurations']['grafana-auth']['auth_github_client_id']
auth_github_client_secret = config['configurations']['grafana-auth']['auth_github_client_secret']
auth_github_scopes = config['configurations']['grafana-auth']['auth_github_scopes']
auth_github_auth_url = config['configurations']['grafana-auth']['auth_github_auth_url']
auth_github_token_url = config['configurations']['grafana-auth']['auth_github_token_url']
auth_github_api_url = config['configurations']['grafana-auth']['auth_github_api_url']
auth_github_team_ids = config['configurations']['grafana-auth']['auth_github_team_ids']
auth_github_allowed_domains = config['configurations']['grafana-auth']['auth_github_allowed_domains']
auth_github_allowed_organizations = config['configurations']['grafana-auth']['auth_github_allowed_organizations']

auth_google_enabled = str(config['configurations']['grafana-auth']['auth_google_enabled']).lower()
auth_google_allow_sign_up = str(config['configurations']['grafana-auth']['auth_google_allow_sign_up']).lower()
auth_google_client_id = config['configurations']['grafana-auth']['auth_google_client_id']
auth_google_client_secret = config['configurations']['grafana-auth']['auth_google_client_secret']
auth_google_scopes = config['configurations']['grafana-auth']['auth_google_scopes']
auth_google_auth_url = config['configurations']['grafana-auth']['auth_google_auth_url']
auth_google_token_url = config['configurations']['grafana-auth']['auth_google_token_url']
auth_google_api_url = config['configurations']['grafana-auth']['auth_google_api_url']
auth_google_allowed_domains = config['configurations']['grafana-auth']['auth_google_allowed_domains']

auth_proxy_enabled = str(config['configurations']['grafana-auth']['auth_proxy_enabled']).lower()
auth_proxy_header_name = config['configurations']['grafana-auth']['auth_proxy_header_name']
auth_proxy_header_property = config['configurations']['grafana-auth']['auth_proxy_header_property']
auth_proxy_auto_sign_up = str(config['configurations']['grafana-auth']['auth_proxy_auto_sign_up']).lower()

auth_basic_enabled = str(config['configurations']['grafana-auth']['auth_basic_enabled']).lower()

auth_ldap_enabled = str(config['configurations']['grafana-auth']['auth_ldap_enabled']).lower()
auth_ldap_config_file = config['configurations']['grafana-auth']['auth_ldap_config_file']

smtp_enabled = str(config['configurations']['grafana-conf']['smtp_enabled']).lower()
smtp_host = config['configurations']['grafana-conf']['smtp_host']
smtp_user = config['configurations']['grafana-conf']['smtp_user']
smtp_password = config['configurations']['grafana-conf']['smtp_password']
smtp_cert_file = config['configurations']['grafana-conf']['smtp_cert_file']
smtp_key_file = config['configurations']['grafana-conf']['smtp_key_file']
smtp_skip_verify = str(config['configurations']['grafana-conf']['smtp_skip_verify']).lower()
smtp_from_address = config['configurations']['grafana-conf']['smtp_from_address']

welcome_email_on_sign_up = str(config['configurations']['grafana-conf']['welcome_email_on_sign_up']).lower()

mode = config['configurations']['grafana-conf']['mode']

buffer_len = config['configurations']['grafana-conf']['buffer_len']

level = config['configurations']['grafana-conf']['level']

log_console_level = config['configurations']['grafana-conf']['log_console_level']

log_file_level = config['configurations']['grafana-conf']['log_file_level']
log_rotate = str(config['configurations']['grafana-conf']['log_rotate']).lower()
max_lines = config['configurations']['grafana-conf']['max_lines']

max_lines_shift = config['configurations']['grafana-conf']['max_lines_shift']
daily_rotate = str(config['configurations']['grafana-conf']['daily_rotate']).lower()
max_days = config['configurations']['grafana-conf']['max_days']

event_publisher_enabled = str(config['configurations']['grafana-conf']['event_publisher_enabled']).lower()
event_publisher_url = config['configurations']['grafana-conf']['event_publisher_url']
event_publisher_exchange = config['configurations']['grafana-conf']['event_publisher_exchange']

dashboards_json_enabled = str(config['configurations']['grafana-conf']['dashboards_json_enabled']).lower()
dashboards_json_path = config['configurations']['grafana-conf']['dashboards_json_path']

#ldap config
verbose_logging = str(config['configurations']['grafana-ldap']['verbose_logging']).lower()

ldap_host = config['configurations']['grafana-ldap']['ldap_host']
ldap_port = config['configurations']['grafana-ldap']['ldap_port']
use_ssl = str(config['configurations']['grafana-ldap']['use_ssl']).lower()
ssl_skip_verify = str(config['configurations']['grafana-ldap']['ssl_skip_verify']).lower()
bind_dn = config['configurations']['grafana-ldap']['bind_dn']
search_filter = config['configurations']['grafana-ldap']['search_filter']
search_base_dns = config['configurations']['grafana-ldap']['search_base_dns']
server_attributes= config['configurations']['grafana-ldap']['server_attributes']
servers_group_mappings = config['configurations']['grafana-ldap']['servers_group_mappings']


