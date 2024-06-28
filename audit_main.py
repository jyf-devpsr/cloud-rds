#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.mysql_install import *
from bin.conf_util import *
from bin.install_monitor_n9e import *
import sys
import datetime
from bin.xxxxxxx_hostname import *

install_type = sys.argv[1]
zone = sys.argv[2]
version = sys.argv[3]
masterip = sys.argv[4]
slaveip = sys.argv[5]
vip = sys.argv[6]
rds_id = sys.argv[7]

# 集群关系映射
with open('/root/xxxxxxx_mysql_install_list_for_dba.txt','a+') as file:
    file.write(str(datetime.datetime.now()))
    file.write('\n')
    file.write('xxxxxxx mysql install config:' + '\n')
    file.write('python deploy_main.py '+install_type + ' ' + zone + ' '+ version + ' '+ masterip + ' ' + slaveip + ' ' + vip + '\n')
    file.write('\n')



# 暂不开放传参
ssh_user = 'xxxxxx'
ssh_pwd = 'xxxxxxxxxxx'
ssh_port = 8888

datadir = '/data/mysql/data/'
app_user = 'proxysql_user'
app_pwd =  'xxxxxxxx'
app_database = 'proxysql_db'

#second_check_ip 用于仲裁和脚本的ftp文件下载
if (zone == "default_prod" or zone == "default_prod_b" or zone == "default_prod_c" or zone == "default_prod_d" or zone == "default_prod_e"):
    second_check_ip = 'xxxx.xxxx.xxxx.xxx'
else:
    second_check_ip = 'xxxx.xxxx.xxxx.xxx'

print(datetime.datetime.now())
try:
    if (install_type == "single"):
        pass
        # 还未调试，后期调试

    elif (install_type == "repl"):
        pass
        # 还未调试，后期调试

    elif (install_type == "mha"):
        #安装前配置检查
        pre_install_check(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, second_check_ip, datadir, install_type)
        # 修改主机名
        change_xxxxxxx_hostname(masterip, slaveip, ssh_user, ssh_pwd, ssh_port, version, zone)
        # 执行安装
        #deploy mha
        deploy_result = mysql_mha_install(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, second_check_ip, datadir, app_user,
                          app_pwd, app_database, version, zone, rds_id)
        try:
            #install n9e exporter
            if (zone == "default_prod"):
                install_monitor_prod(masterip, ssh_user, ssh_pwd, ssh_port)
                install_monitor_prod(slaveip, ssh_user, ssh_pwd, ssh_port)
            else:
                install_monitor_dev(masterip, ssh_user, ssh_pwd, ssh_port)
                install_monitor_dev(slaveip, ssh_user, ssh_pwd, ssh_port)
        except Exception as e:
            print("error: %s" % e)

        if (deploy_result == 'deploy_ok'):
            print(datetime.datetime.now())
            print("{\"code\":200,\"msg\":\"ok\"}")
        else:
            raise Exception("deploy is failed.")

    elif (install_type == "cluster"):
        pass
    else:
        raise ValueError("Invalid install type " + install_type)
except Exception as e:
    print("error: %s" % e)
    print(datetime.datetime.now())
    print("{\"code\":400,\"msg\":\"fail\"}")

