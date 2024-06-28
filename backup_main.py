#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.xxxxxxx_databases import *
import sys

masterip = sys.argv[1]
slaveip = sys.argv[2]
vip = sys.argv[3]
op_type = sys.argv[4]
dbname = sys.argv[5]
xxxxxxx_user = sys.argv[6]

# 暂不开放传参
ssh_user = 'xxxxxxxxx'
ssh_pwd = 'xxxxxxx'
ssh_port = 8888
root_pwd = 'xxxxxxxxxxx'

# 修改备份保留天数
if op_type == "update_days":
    # 密码复杂度检查
    # parse()
    # 创建用户
    result = create_database(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, root_pwd, dbname, xxxxxxx_user)
    if result == "create_ok":
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")
# 拉取备份文件信息
elif op_type == "list_backupset":
    # 删除用户
    result = drop_database(masterip, ssh_user, ssh_pwd, ssh_port, root_pwd, vip, dbname)
    if result == "drop_ok":
        print("{\"code\":200,\"msg\":\"ok\"}")
    else:
        print("{\"code\":400,\"msg\":\"failed\"}")
