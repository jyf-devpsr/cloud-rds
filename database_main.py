#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.xxxxxxx_databases import *
import sys

masterip = sys.argv[1]
slaveip = sys.argv[2]
vip = sys.argv[3]
op_type = sys.argv[4]
dbname = sys.argv[5]
charset = sys.argv[6]
version = sys.argv[7]


#暂不开放传参
ssh_user = 'xxxxx'
ssh_pwd = 'xxxxxxxxxxxx'
ssh_port = 8888
root_pwd = 'xxxxxxxxxxxxxx'


xxxxxxx_user = 'xxxxxx'
grant_num = len(sys.argv)
for i in range(8, grant_num):
    xxxxxxx_user = sys.argv[i]




if (op_type == "create_database"):
    #密码复杂度检查
    #parse()
    #创建用户
    result = create_database(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, dbname, xxxxxxx_user ,version)
    if (result == "create_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")

elif (op_type == "drop_database"):
    #删除用户
    result = drop_database(masterip, ssh_user, ssh_pwd, ssh_port, root_pwd, vip, dbname)
    if (result == "drop_ok"):
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")
