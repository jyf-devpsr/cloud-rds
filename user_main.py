#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.xxxxxxx_users import *
import sys

masterip = sys.argv[1]
slaveip = sys.argv[2]
vip = sys.argv[3]
op_type = sys.argv[4]
accout_type = sys.argv[5]
xxxxxxx_user = sys.argv[6]
xxxxxxx_pwd = sys.argv[7]
version = sys.argv[8]



grant_num = len(sys.argv)
grant_dict = {}
for i in range(9, grant_num):
    g_list =sys.argv[i].split(":")
    grant_dict[g_list[0]] = g_list[1]


# 暂不开放传参
ssh_user = 'xxxxx'
ssh_pwd = 'xxxxxxxxxxx'
ssh_port = 8888
root_pwd = 'xxxxxxxxxxxxx'

# 替换掉转义符
xxxxxxx_pwd = xxxxxxx_pwd.replace("\\", "")

if (op_type == "create_user"):
    # 创建用户
    result = create_user(masterip, slaveip, accout_type, xxxxxxx_user, xxxxxxx_pwd, ssh_user, ssh_pwd, ssh_port, root_pwd, vip, version, grant_dict)
    if (result == "create_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")

elif (op_type == "drop_user"):
    # 删除用户
    result = drop_user(masterip, slaveip, xxxxxxx_user, ssh_user, ssh_pwd, ssh_port, root_pwd, vip)
    if (result == "drop_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")

elif (op_type == "update_user"):
    # 删除用户
    result = change_user_pwd(masterip, slaveip, xxxxxxx_user, xxxxxxx_pwd, ssh_user, ssh_pwd, ssh_port, root_pwd, vip, version)
    if (result == "change_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")
elif (op_type == "update_grant"):
    # 修改用户权限
    result = change_user_grant(masterip, slaveip, vip, xxxxxxx_user, ssh_user, ssh_pwd, ssh_port, root_pwd, version, grant_dict)
    if (result == "change_grant_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("change_user_grant is failed.")
        print("{\"code\":400,\"msg\":\"failed\"}")

