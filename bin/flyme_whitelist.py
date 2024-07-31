#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *
from xxxxxxx_users import *

# 系统内置白名单
def system_whitelist(masterip, slaveip, ssh_user, ssh_pwd, ssh_port):
    client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
    exec_cmd(client, ssh_user, "systemctl restart firewalld")


    # 系统
    # prod
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10. port port=96 protocol=tcp accept' --permanent")

    # test
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.0 port port=910006 protocol=tcp accept' --permanent")

    # 集群主身互访
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=%s/32 accept' --permanent" % masterip)
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=%s/32 accept' --permanent" % slaveip)
    # 重启防火墙
    exec_cmd(client, ssh_user, "firewall-cmd --reload")
    exec_cmd(client, ssh_user, "firewall-cmd --list-rich-rules")

# 用户自定义开通白名单
def user_whitelist(masterip, slaveip, op_type, ssh_user, ssh_pwd, ssh_port, ip_list):
    if op_type == 'add':
        try:
            master_client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
            for ip in ip_list:
                exec_cmd(master_client, ssh_user,
                         "firewall-cmd --add-rich-rule='rule family=ipv4 source address=%s port port=6033 protocol=tcp accept' --permanent" % ip)
            exec_cmd(master_client, ssh_user, "firewall-cmd --reload")
            master_client.close()
            slave_client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
            for ip in ip_list:
                exec_cmd(slave_client, ssh_user,
                         "firewall-cmd --add-rich-rule='rule family=ipv4 source address=%s port port=6033 protocol=tcp accept' --permanent" % ip)
            exec_cmd(slave_client, ssh_user, "firewall-cmd --reload")
            slave_client.close()
        except Exception as e:
            print("error: %s" % e)
        else:
            return "add_ok"
    elif op_type == 'remove':
        try:
            master_client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
            for ip in ip_list:
                exec_cmd(master_client, ssh_user,
                         "firewall-cmd --remove-rich-rule='rule family=ipv4 source address=%s port port=6033 protocol=tcp accept' --permanent" % ip)
            exec_cmd(master_client, ssh_user, "firewall-cmd --reload")
            master_client.close()
            slave_client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
            for ip in ip_list:
                exec_cmd(slave_client, ssh_user,
                         "firewall-cmd --remove-rich-rule='rule family=ipv4 source address=%s port port=6033 protocol=tcp accept' --permanent" % ip)
            exec_cmd(slave_client, ssh_user, "firewall-cmd --reload")
            slave_client.close()
        except Exception as e:
            print("error: %s" % e)
        else:
            return "remove_ok"

