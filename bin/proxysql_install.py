#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from time import sleep

from ssh_util import *
from upload_file_const import proxy_upload_file_list


def deploy_proxysql(client,username,masterip,slaveip,version):
    #安装2.4.8的proxysql
    conf_file = "/etc/proxysql.cnf"
    exec_cmd(client, username, "yum localinstall -y proxysql-2.4.8-1-centos7.x86_64.rpm")
    #启动会初始化并创建目录和相关文件
    stdin,stdout,stderr = exec_cmd(client, username, "systemctl start proxysql.service")
    sleep(3)
    stdin,stdout,stderr = exec_cmd(client, username, "systemctl stop proxysql.service")
    #把临时生成的proxysql.db删掉，proxysql.db不可轻易删除，会丢失注册的信息
    exec_cmd(client, username, "rm -f /var/lib/proxysql/proxysql.db")
    #tar xvf
    exec_cmd(client, username, "tar xvf proxysql.tar -C /var/lib/proxysql")
    #conf file
    exec_cmd(client, username, "mv /etc/proxysql.cnf /etc/proxysql.cnf_bak")
    exec_cmd(client, username, "cp /var/lib/proxysql/proxysql/conf/proxysql.cnf /etc/proxysql.cnf")
    exec_cmd(client, username, "sed -i 's/@masterip/" + masterip + "/g' " + conf_file)
    exec_cmd(client, username, "sed -i 's/@slaveip/" + slaveip + "/g' " + conf_file)
    if version == '8.0':
        my_version = '8.0.34'
        exec_cmd(client, username, "sed -i 's/@my_version/" + my_version + "/g' " + conf_file)
    elif version == '5.7':
        my_version = '5.7.43'
        exec_cmd(client, username, "sed -i 's/@my_version/" + my_version + "/g' " + conf_file)
    elif version == '5.6':
        my_version = '5.6.51'
        exec_cmd(client, username, "sed -i 's/@my_version/" + my_version + "/g' " + conf_file)
    #自启动
    exec_cmd(client, username, "systemctl enable proxysql.service")
    stdin,stdout,stderr = exec_cmd(client, username, "systemctl start proxysql.service")
    # 重启集群，避开集群 ERROR 9001 bug
    sleep(15)
    exec_cmd(client, username, "systemctl restart proxysql.service")
    print('proxysql deploy done!')
    return
#注册mysql master到proxysql
def register_proxysql(client,username,masterip, xxxxxxx_rootpwd, appUser, appPwd):
    #app user config
    exec_cmd(client, username, "sh /var/lib/proxysql/proxysql/bin/add_user.sh %s '%s'" % (appUser,appPwd))
    exec_cmd(client, username, "sh /var/lib/proxysql/proxysql/bin/add_user.sh proxy_test 'proxy_ping-.MZ123'")
    #监控用户
    exec_cmd(client, username, "sh /var/lib/proxysql/proxysql/bin/add_user.sh proxysql_monitor 'proxysql123'")
    #注册master服务到proxysql
    exec_cmd(client,username,"sh /var/lib/proxysql/proxysql/bin/set_server.sh " + masterip + " online")
    #注册xxxxxxx root到proxysql
    exec_cmd(client,username,"sh /var/lib/proxysql/proxysql/bin/add_user.sh xxxxxxx_root '%s'" % (xxxxxxx_rootpwd))
    print('register proxysql done!')
    return

def install(masterip,slaveip,port,username,password,appUser,appPwd, xxxxxxx_rootpwd,version):
    masterClient = get_ssh_client(masterip, username, password, port)    
    slaveClient = get_ssh_client(slaveip, username, password, port)
    deploy_proxysql(masterClient, username, masterip,slaveip,version)
    deploy_proxysql(slaveClient,username,masterip,slaveip,version)
    register_proxysql(masterClient,username, masterip, xxxxxxx_rootpwd, appUser, appPwd)



def init_app(masterip,slaveip,port,username,password,rootpwd,appUser,appPwd,appDatabase):
    print(appDatabase)
    client = get_ssh_client(masterip, username, password, port)
    exec_cmd(client, username, "mysql -u root -e \"create database if not exists %s\"" % (appDatabase))
    exec_cmd(client, username, "mysql -u root -e \"create user %s@\'10.%%\' identified with mysql_native_password by \'%s\'\"" % (appUser,appPwd))
    exec_cmd(client, username, "mysql -u root -e \"grant all on %s.* to %s@'10.%%\'\"" % (appDatabase, appUser))
    exec_cmd(client, username, "mysql -u root -e \"create user %s@\'%s\' identified with mysql_native_password by \'%s\'\"" % ("proxy_test",masterip,"proxy_ping-.MZ123"))
    exec_cmd(client, username, "mysql -u root -e \"grant usage on *.* to %s@\'%s\'\"" % ("proxy_test",masterip))
    exec_cmd(client, username, "mysql -u root -e \"create user %s@\'%s\' identified with mysql_native_password by \'%s\'\"" % ("proxy_test",slaveip,"proxy_ping-.MZ123"))
    exec_cmd(client, username, "mysql -u root -e \"grant usage on *.* to %s@\'%s\'\"" % ("proxy_test",slaveip))
    exec_cmd(client, username, "mysql -u root -e \"create user %s@\'localhost\' identified with mysql_native_password by \'%s\'\"" % ("proxy_test","proxy_ping-.MZ123"))
    exec_cmd(client, username, "mysql -u root -e \"grant usage on *.* to %s@\'localhost\'\"" % ("proxy_test"))
    #proxysql自身监控用户
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = low'")
    exec_cmd(client, username, "mysql -u root -e \"create user %s@\'10.%%\' identified with mysql_native_password by \'%s\'\"" % ("proxysql_monitor","proxysql123"))
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to %s@\'10.%%\'\"" % ("proxysql_monitor"))
    exec_cmd(client, username, "mysql -u root -e \"flush privileges\"")
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = MEDIUM'")
    print('proxysql init app done!')

def init_app_5(masterip,slaveip,port,username,password,rootpwd,appUser,appPwd,appDatabase):
    print(appDatabase)
    client = get_ssh_client(masterip, username, password, port)
    exec_cmd(client, username, "mysql -u root -e \"create database if not exists %s\"" % (appDatabase))
    exec_cmd(client, username, "mysql -u root -e \"grant all on %s.* to %s@'10.%%\' identified by \'%s\'\"" % (appDatabase, appUser, appPwd))
    exec_cmd(client, username, "mysql -u root -e \"grant usage on *.* to %s@\'%s\' identified by \'%s\'\"" % ("proxy_test",masterip,"proxy_ping-.MZ123"))
    exec_cmd(client, username, "mysql -u root -e \"grant usage on *.* to %s@\'%s\' identified by \'%s\'\"" % ("proxy_test",slaveip,"proxy_ping-.MZ123"))
    exec_cmd(client, username, "mysql -u root -e \"grant usage on *.* to %s@\'localhost\' identified by \'%s\'\"" % ("proxy_test","proxy_ping-.MZ123"))
    #proxysql自身监控用户
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = low'")
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to %s@\'10.%%\' identified by \'%s\'\"" % ("proxysql_monitor","proxysql123"))
    exec_cmd(client, username, "mysql -u root -e \"flush privileges\"")
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = MEDIUM'")
    print('proxysql init app done!')

def main(masterip,slaveip,port,username,password,rootpwd,appUser,appPwd,appDatabase,xxxxxxx_rootpwd, version):
    print("install proxysql began.")
    try:
        if (version == '8.0'):
            init_app(masterip, slaveip, port, username, password, rootpwd, appUser, appPwd, appDatabase)
        else:
            init_app_5(masterip, slaveip, port, username, password, rootpwd, appUser, appPwd, appDatabase)
        upload_file(masterip, username, password, port, proxy_upload_file_list)
        upload_file(slaveip, username, password, port, proxy_upload_file_list)
        install(masterip, slaveip, port, username, password, appUser, appPwd, xxxxxxx_rootpwd, version)
    except Exception as e:
        print("error: %s" % e)
    else:
        return "prxysql_install_ok"
        print("install proxysql finished.")




    


