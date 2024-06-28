#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 创建并初始化xxxxxxx_root用户
from bin.ssh_util import *

def grant_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, version, xxxxxxx_user, grant_db, grant_role):
    client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
    if version == '8.0':
        if grant_role == 'write':
            # write
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant ALL PRIVILEGES ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant ALL PRIVILEGES ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'read':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, LOCK TABLES, SHOW VIEW ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, LOCK TABLES, SHOW VIEW ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'ddl':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'dml':
            # master host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, INSERT, UPDATE, DELETE, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, SHOW VIEW, EVENT, TRIGGER ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, INSERT, UPDATE, DELETE, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, SHOW VIEW, EVENT, TRIGGER ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant XA_RECOVER_ADMIN ON *.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
    elif version == '5.7':
        if grant_role == 'write':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant ALL PRIVILEGES ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                     vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant ALL PRIVILEGES ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'read':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, LOCK TABLES, SHOW VIEW ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, LOCK TABLES, SHOW VIEW ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'ddl':
            # master host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'dml':
            # master host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, INSERT, UPDATE, DELETE, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, SHOW VIEW, EVENT, TRIGGER ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, INSERT, UPDATE, DELETE, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, SHOW VIEW, EVENT, TRIGGER ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
    elif version == '5.6':
        if grant_role == 'write':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant ALL PRIVILEGES ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant ALL PRIVILEGES ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'read':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, LOCK TABLES, SHOW VIEW ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, LOCK TABLES, SHOW VIEW ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'ddl':
            # master host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
        elif grant_role == 'dml':
            # master host
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, INSERT, UPDATE, DELETE, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, SHOW VIEW, EVENT, TRIGGER ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, masterip))

            # slave host

            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT, INSERT, UPDATE, DELETE, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, SHOW VIEW, EVENT, TRIGGER ON \`%s\`.* TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, grant_db, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.general_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.proc TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.slow_log TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.event TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_keyword TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_transition_type TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_topic TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.func TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_category TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.help_relation TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))
            exec_cmd(client, ssh_user,
                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant SELECT ON mysql.time_zone_leap_second TO '%s'@'%s';flush privileges;\"" % (
                         vip, root_pwd, xxxxxxx_user, slaveip))

def revoke_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, xxxxxxx_user, version):
    client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
    old_version = ['5.6','5.7']
    if version in old_version:
        # on master host
        # revoke about masterip
        stdin,stdout,stderr = exec_cmd(client, ssh_user,
                 "mysql -uroot -h%s -p'%s' -P6033 -e \"show grants for '%s'@'%s'\"" % (
                     vip, root_pwd, xxxxxxx_user, masterip))
        # 返回结果为一个单值列表
        get_grants_masterip = stdout.readlines()
        exec_cmd(client, ssh_user,"echo '%s' > grant_tmp.txt" % get_grants_masterip)
        exec_cmd(client, ssh_user,"sh xxxxxxx_revoke.sh >> xxxxxxx_update_grant.log 2>&1")
        exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 < xxxxxxx_revoke.txt" % (vip, root_pwd))
        # revoke about slaveip
        stdin,stdout,stderr = exec_cmd(client, ssh_user,
                 "mysql -uroot -h%s -p'%s' -P6033 -e \"show grants for '%s'@'%s'\"" % (
                     vip, root_pwd, xxxxxxx_user, slaveip))
        get_grants_slaveip = stdout.readlines()
        exec_cmd(client, ssh_user,"echo '%s' > grant_tmp.txt" % get_grants_slaveip)
        exec_cmd(client, ssh_user,"sh xxxxxxx_revoke.sh >> xxxxxxx_update_grant.log 2>&1")
        exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 < xxxxxxx_revoke.txt" % (vip, root_pwd))
    elif version == '8.0':
        # on master host
        # revoke about masterip
        stdin,stdout,stderr = exec_cmd(client, ssh_user,
                 "mysql -uroot -h%s -p'%s' -P6033 -e \"show grants for '%s'@'%s'\"" % (
                     vip, root_pwd, xxxxxxx_user, masterip))
        # 返回结果为一个多值列表
        # 转换成str
        get_grants_masterip = ''.join(stdout.readlines())
        exec_cmd(client, ssh_user,"echo '%s' > grant_tmp.txt" % get_grants_masterip)
        exec_cmd(client, ssh_user,"sh xxxxxxx_revoke.sh >> xxxxxxx_update_grant.log 2>&1")
        exec_cmd(client, ssh_user,"sed \"s/$/&';/g\" xxxxxxx_revoke.txt > xxxxxxx_revoke_8.txt")
        exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 < xxxxxxx_revoke_8.txt" % (vip, root_pwd))
        # revoke about slaveip
        stdin,stdout,stderr = exec_cmd(client, ssh_user,
                 "mysql -uroot -h%s -p'%s' -P6033 -e \"show grants for '%s'@'%s'\"" % (
                     vip, root_pwd, xxxxxxx_user, slaveip))
        get_grants_slaveip = ''.join(stdout.readlines())
        exec_cmd(client, ssh_user,"echo '%s' > grant_tmp.txt" % get_grants_slaveip)
        exec_cmd(client, ssh_user,"sh xxxxxxx_revoke.sh >> xxxxxxx_update_grant.log 2>&1")
        exec_cmd(client, ssh_user,"sed \"s/$/&';/g\" xxxxxxx_revoke.txt > xxxxxxx_revoke_8.txt")
        exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 < xxxxxxx_revoke_8.txt" % (vip, root_pwd))


# 不允许操作的系统用户
sys_users = ['root','admin','backup','proxysql_monitor','proxysql_user','xxxxxxx_root','p8s_exporter','monitor','proxy_test']
def create_user(masterip, slaveip, accout_type, xxxxxxx_user, xxxxxxx_pwd, ssh_user, ssh_pwd, ssh_port, root_pwd, vip, version, grant_dict):
    try:
        client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
        if bool(grant_dict): # 用户选择了权限，这里只能有普通用户
            create_num = 0 # 用户只创建一次
            for grant_db,grant_role in grant_dict.items():
                if xxxxxxx_user not in sys_users:
                    if version == '8.0':
                        try:
                            if create_num == 0:
                                # 创建用户
                                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"create user '%s'@'%s' identified with mysql_native_password by '%s'\"" % (vip,root_pwd,xxxxxxx_user,masterip,xxxxxxx_pwd))
                                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"create user '%s'@'%s' identified with mysql_native_password by '%s'\"" % (vip,root_pwd,xxxxxxx_user,slaveip,xxxxxxx_pwd))
                                create_num = create_num + 1
                            if accout_type == '2':
                                # 授权
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, masterip))
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, slaveip))
                                # 调用授权函数
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, masterip))
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, slaveip))

                                grant_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, version, xxxxxxx_user, grant_db, grant_role)
                        except:
                            raise
                    elif version == '5.7':
                        try:

                            if accout_type == '2':
                                # 创建用户
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, masterip, xxxxxxx_pwd))
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, slaveip, xxxxxxx_pwd))
                                # 调用授权函数
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, masterip))
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, slaveip))
                                grant_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, version, xxxxxxx_user, grant_db, grant_role)

                        except:
                            raise
                    elif version == '5.6':
                        try:
                            if accout_type == '2':

                                # 创建用户
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, masterip, xxxxxxx_pwd))
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, slaveip, xxxxxxx_pwd))


                                # 调用授权函数
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, masterip))
                                exec_cmd(client, ssh_user,
                                         "mysql -uroot -h%s -p'%s' -P6033 -e \"grant PROCESS, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                             vip, root_pwd, xxxxxxx_user, slaveip))

                                grant_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, version, xxxxxxx_user, grant_db, grant_role)

                        except:
                            raise
                else:
                    #主动抛个异常
                    raise Exception('the system account is not allowed to be used!!!')
            exec_cmd(client, ssh_user, "sh /var/lib/proxysql/proxysql/bin/add_user.sh %s '%s'" % (xxxxxxx_user, xxxxxxx_pwd))
        else: # 权限给空，普通用户没有授权，和管理用户
            if xxxxxxx_user not in sys_users:
                if version == '8.0':
                    try:
                        # 创建用户
                        exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"create user '%s'@'%s' identified with mysql_native_password by '%s'\"" % (vip,root_pwd,xxxxxxx_user,masterip,xxxxxxx_pwd))
                        exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"create user '%s'@'%s' identified with mysql_native_password by '%s'\"" % (vip,root_pwd,xxxxxxx_user,slaveip,xxxxxxx_pwd))
                        if accout_type == '1':
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant all on *.* to '%s'@'%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,masterip))
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant all on *.* to '%s'@'%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,slaveip))
                        elif accout_type == '2':
                            # 授权
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                         vip, root_pwd, xxxxxxx_user, masterip))
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s';flush privileges;\"" % (
                                         vip, root_pwd, xxxxxxx_user, slaveip))
                    except:
                        raise
                elif version == '5.7':
                    try:
                        if accout_type == '1':
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant all on *.* to '%s'@'%s' identified by '%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,masterip, xxxxxxx_pwd))
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant all on *.* to '%s'@'%s' identified by '%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,slaveip, xxxxxxx_pwd))
                        elif accout_type == '2':
                            # 创建用户
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                         vip, root_pwd, xxxxxxx_user, masterip, xxxxxxx_pwd))
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                         vip, root_pwd, xxxxxxx_user, slaveip, xxxxxxx_pwd))

                    except:
                        raise
                elif version == '5.6':
                    try:
                        if accout_type == '1':
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant all on *.* to '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                     vip, root_pwd, xxxxxxx_user, masterip, xxxxxxx_pwd))
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant all on *.* to '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                     vip, root_pwd, xxxxxxx_user, slaveip, xxxxxxx_pwd))
                        elif accout_type == '2':
                            # 创建用户
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                         vip, root_pwd, xxxxxxx_user, masterip, xxxxxxx_pwd))
                            exec_cmd(client, ssh_user,
                                     "mysql -uroot -h%s -p'%s' -P6033 -e \"grant usage ON *.* TO '%s'@'%s' identified by '%s';flush privileges;\"" % (
                                         vip, root_pwd, xxxxxxx_user, slaveip, xxxxxxx_pwd))
                    except:
                        raise
            else:
                #主动抛个异常
                raise Exception('the system account is not allowed to be used!!!')
            exec_cmd(client, ssh_user, "sh /var/lib/proxysql/proxysql/bin/add_user.sh %s '%s'" % (xxxxxxx_user, xxxxxxx_pwd))

    except Exception as e:
        print("error: %s" % e)
    else:
        return "create_ok"


def drop_user(masterip, slaveip, xxxxxxx_user, ssh_user, ssh_pwd, ssh_port, root_pwd, vip):
    try:
        if xxxxxxx_user not in sys_users:
            client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
            exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"drop user '%s'@'%s';flush privileges;\"" % (vip,root_pwd, xxxxxxx_user, masterip))
            exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"drop user '%s'@'%s';flush privileges;\"" % (vip,root_pwd, xxxxxxx_user, slaveip))
            #清掉proxysql信息
            exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/drop_user.sh %s" % xxxxxxx_user)
        else:
            #主动抛个异常
            raise Exception('the system account is not allowed to be dropped!!!')
    except Exception as e:
        print("error: %s" % e)
    else:
        return "drop_ok"

def change_user_pwd(masterip, slaveip, xxxxxxx_user, xxxxxxx_pwd, ssh_user, ssh_pwd, ssh_port, root_pwd, vip, verion):
    try:
        if verion == '8.0':
            if (xxxxxxx_user not in sys_users):
                client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"alter user '%s'@'%s' identified with mysql_native_password by '%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,masterip,xxxxxxx_pwd))
                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"alter user '%s'@'%s' identified with mysql_native_password by '%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,slaveip,xxxxxxx_pwd))
                #更新proxysql信息
                exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/drop_user.sh %s" % (xxxxxxx_user))
                exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/add_user.sh %s '%s'" % (xxxxxxx_user,xxxxxxx_pwd))
            else:
                #主动抛个异常
                raise Exception('the system account is not allowed to be changed!!!')
        elif verion == '5.7':
            if (xxxxxxx_user not in sys_users):
                client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"alter user '%s'@'%s' identified by '%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,masterip,xxxxxxx_pwd))
                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"alter user '%s'@'%s' identified by '%s';flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,slaveip,xxxxxxx_pwd))
                #更新proxysql信息
                exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/drop_user.sh %s" % (xxxxxxx_user))
                exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/add_user.sh %s '%s'" % (xxxxxxx_user,xxxxxxx_pwd))
            else:
                # 主动抛个异常
                raise Exception('the system account is not allowed to be changed!!!')
        elif verion == '5.6':
            if (xxxxxxx_user not in sys_users):
                client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"SET PASSWORD FOR '%s'@'%s' = PASSWORD('%s');flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,masterip,xxxxxxx_pwd))
                exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"SET PASSWORD FOR '%s'@'%s' = PASSWORD('%s');flush privileges;\"" % (vip,root_pwd,xxxxxxx_user,slaveip,xxxxxxx_pwd))
                # 更新proxysql信息
                exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/drop_user.sh %s" % (xxxxxxx_user))
                exec_cmd(client, ssh_user,"sh /var/lib/proxysql/proxysql/bin/add_user.sh %s '%s'" % (xxxxxxx_user,xxxxxxx_pwd))
            else:
                # 主动抛个异常
                raise Exception('the system account is not allowed to be changed!!!')
    except Exception as e:
        print("error: %s" % e)
    else:
        return "change_ok"


def change_user_grant(masterip, slaveip, vip, xxxxxxx_user, ssh_user, ssh_pwd, ssh_port, root_pwd, version, grant_dict):
    try:
        revoke_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, xxxxxxx_user, version)
        for grant_db, grant_role in grant_dict.items():
            # grant new
            grant_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, version, xxxxxxx_user, grant_db, grant_role)

    except Exception as e:
        print("error: %s" % e)
    else:
        return "change_grant_ok"