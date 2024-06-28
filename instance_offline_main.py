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
ssh_pwd = 'xxxxxxxxxxxx'
ssh_port = 8888
root_pwd = 'xxxxxxxxxxxxxxx'

# 实例下线流程 目前仅做 1、取消gocron备份任务；

