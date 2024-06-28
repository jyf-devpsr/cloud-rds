#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#
def add_prefix(file_list):
    rs_list=[]
    for i in range(len(file_list)):
        rs_list.append(path_prefix + file_list[i])
    return rs_list 
        
path_prefix=os.path.dirname(os.path.abspath("__file__")) + "root/file/"
mysql_upload_file_list=add_prefix(["build_mysql_80.sh","build_mysql_57.sh","build_mysql_56.sh","my_80.cnf","my_57.cnf","my_56.cnf","init_hostname.py","keepalived_notify.py","mydumper-0.15.0-7.el7.x86_64.rpm","xxxxxxx_mydumper_backup.sh","xxxxxxx_revoke.sh"])
proxy_upload_file_list=add_prefix(["proxysql.tar","proxysql-2.4.8-1-centos7.x86_64.rpm","install_db_exporter.bash"])
mha_script_upload_file_list=add_prefix(["manager_0.56.rpm","node_0.56.rpm","mha4mysql-node-0.58-0.el7.centos.noarch.rpm","mha4mysql-manager-0.58-0.el7.centos.noarch.rpm","masterha.tar","get_gocron_token.sh","add_gocron_jobs.sh"])
