#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *
from xxxxxxx_users import *

# 系统内置白名单
def system_whitelist(masterip, slaveip, ssh_user, ssh_pwd, ssh_port):
    client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
    exec_cmd(client, ssh_user, "systemctl restart firewalld")
    # 运维管理平台
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.52.91/32 accept' --permanent")
    # 神州发布平台
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.5.116/32 accept' --permanent")
    # 长江北发布平台
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.24.88/32 accept' --permanent")
    # 测试环境备份服务器
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.15.28/32 accept' --permanent")
    # 生产环境备份gocron任务节点
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=100.68.97.68/32 accept' --permanent")



    # 夜莺监控系统
    # prod
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.18.59 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.16.225 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.16.224 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.16.219 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.16.220 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.16.223 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.128.122.0/23 port port=9100-9306 protocol=tcp accept' --permanent")
    # test
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.248.29 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.248.27 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.248.28 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.248.30 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.248.31 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.74.0/24 port port=9100-9306 protocol=tcp accept' --permanent")
    exec_cmd(client, ssh_user,
             "firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.131.160.0/20 port port=9100-9306 protocol=tcp accept' --permanent")

    # 集群主从自身互访
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

