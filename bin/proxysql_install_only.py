#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ssh_util import *
from bin.proxysql_install import *
from upload_file_const import proxy_upload_file_list

def proxysql_install_only(config,username,password,port):
    for info in config:
        masterip = info[0]
        slaveip = info[1] 
        appUser = info[2]
        appPwd = info[3]
        rootpwd = info[4]
        print("install proxysql began.")
        client = get_ssh_client(masterip, username, password, port)     
        exec_cmd(client, username, "mysql -u root -p%s -e \"grant usage on *.* to %s@\'%s\' identified by \'%s\'\"" % (rootpwd,"proxy_test",masterip,"proxy_ping"))
        exec_cmd(client, username, "mysql -u root -p%s -e \"grant usage on *.* to %s@\'%s\' identified by \'%s\'\"" % (rootpwd,"proxy_test",slaveip,"proxy_ping"))
        exec_cmd(client, username, "mysql -u root -p%s -e \"grant usage on *.* to %s@\'localhost\' identified by \'%s\'\"" % (rootpwd,"proxy_test","proxy_ping"))
        upload_file(masterip, username, password, port, proxy_upload_file_list)
        upload_file(slaveip, username, password, port, proxy_upload_file_list)
        install(masterip, slaveip, port, username, password, appUser, appPwd)
        print("install proxysql finished.")
