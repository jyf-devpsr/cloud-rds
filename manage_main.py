#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.xxxxxxx_manage import *
import sys

masterip = sys.argv[1]
slaveip = sys.argv[2]
vip = sys.argv[3]
op_type = sys.argv[4]

# 暂不开放传参
ssh_user = 'xxxxxxxx'
ssh_pwd = 'xxxxxxxxxxxx'
ssh_port = 8888
root_pwd = 'xxxxxxxxxxxxxx'


if op_type == "reboot":

    result = reboot_mysql(masterip, slaveip, ssh_user, ssh_pwd, ssh_port, root_pwd, vip)
    if result == "create_ok":
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")

elif op_type == "stop":
    pass

elif op_type == "start":
    pass

elif op_type == "switch":
    pass

