#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.xxxxxxx_users import *
import sys
from bin.xxxxxxx_whitelist import *

masterip = sys.argv[1]
slaveip = sys.argv[2]
op_type = sys.argv[3]


# 对传过来的ip串进行处理，转换成list
ip_list = (sys.argv[4].split(","))


# 暂不开放传参
ssh_user = 'xxxxxx'
ssh_pwd = 'xxxxxxxxxxx'
ssh_port = 8888


# 增加白名单
if (op_type == "add"):
    result = user_whitelist(masterip, slaveip, op_type, ssh_user, ssh_pwd, ssh_port,  ip_list)
    if result == "add_ok":
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")

# 删除白名单
elif (op_type == "remove"):
    result = user_whitelist(masterip, slaveip, op_type, ssh_user, ssh_pwd, ssh_port,  ip_list)
    if (result == "remove_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")
else:
    pass
