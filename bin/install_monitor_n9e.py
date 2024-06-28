#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *

def install_monitor_prod(ip, ssh_user, ssh_pwd, ssh_port):
    try:
        client = get_ssh_client(ip, ssh_user, ssh_pwd, ssh_port)
        exec_cmd(client, ssh_user,"bash install_db_exporter.bash install node")
        exec_cmd(client, ssh_user,"bash install_db_exporter.bash install mysql")
    except Exception as e:
        return e
    else:
        return "install_ok"

def install_monitor_dev(ip, ssh_user, ssh_pwd, ssh_port):
    try:
        client = get_ssh_client(ip, ssh_user, ssh_pwd, ssh_port)
        exec_cmd(client, ssh_user,"bash install_db_exporter.bash install node")
        exec_cmd(client, ssh_user,"bash install_db_exporter.bash install mysql")
    except Exception as e:
        return e
    else:
        return "install_ok"
