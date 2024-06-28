#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *
from xxxxxxx_users import *

# 系统db不允许操作
sys_db = ["information_schema","mysql","performance_schema","proxysql_db","sys"]
def create_database(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, dbname, xxxxxxx_user,version):
    grant_role = 'write'
    try:
        if (dbname not in sys_db):
            client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
            exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"create database \`%s\`\"" % (vip,root_pwd,dbname))
            # aliyun only dml privileges ## static privileges are administrative and can only be granted globally
        else:
            # 主动抛个异常
            raise Exception('the system database is not allowed to be created!!!')
        if xxxxxxx_user != 'xxxxxxx_root':
            grant_sql(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, version, xxxxxxx_user, dbname,
                      grant_role)
    except Exception as e:
        print("error: %s" % e)
    else:
        return "create_ok"

def drop_database(masterip, ssh_user, ssh_pwd, ssh_port, root_pwd, vip,dbname):
    try:
        if (dbname not in sys_db):
            client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
            exec_cmd(client, ssh_user,"mysql -uroot -h%s -p'%s' -P6033 -e \"drop database \`%s\`\"" % (vip,root_pwd,dbname))
        else:
            # 主动抛个异常
            raise Exception('the system database is not allowed to be dropped!!!')
    except Exception as e:
        print("error: %s" % e)
    else:
        return "drop_ok"