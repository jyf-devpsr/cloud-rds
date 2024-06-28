#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ssh_util import *
from worker import *
import sys
from time import sleep
from upload_file_const import mha_script_upload_file_list

def build_mha(client,username,port,masterip,slaveip,mhapwd,replpwd,second_check_ip, version):
    new_version = ['8.0','5.7']
    old_version = ['5.6']
    conf_file = "/etc/masterha/proxy_app_default.cnf"
    util_file = "/etc/masterha/app1/scripts/mysql_proxy_util"
    failover_file = "/etc/masterha/app1/scripts/master_ip_failover_proxy"
    failover_online = "/etc/masterha/app1/scripts/master_ip_online_change_proxy"
    report_file = "/etc/masterha/app1/scripts/send_report_proxy"
    exec_cmd(client,username,"yum install -y perl perl-DBD-MySQL perl-Config-Tiny perl-Log-Dispatch perl-Parallel-ForkManager perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker perl-CPAN perl-Config-IniFiles")
    if (version in new_version):
        exec_cmd(client, username, "rpm -ivh --force mha4mysql-node-0.58-0.el7.centos.noarch.rpm mha4mysql-manager-0.58-0.el7.centos.noarch.rpm")
    elif (version in old_version): #mysql5.6只能使用0.56的mha
        exec_cmd(client, username, "rpm -ivh --force manager_0.56.rpm node_0.56.rpm")
    exec_cmd(client,username,"tar xvf masterha.tar -C /etc/")
    exec_cmd(client, username, "sed -i 's/@sshport/" + str(port) + "/g' " + conf_file)
    exec_cmd(client, username, "sed -i 's/@mhapwd/" + mhapwd + "/g' " + conf_file)
    exec_cmd(client, username, "sed -i 's/@replpwd/" + replpwd + "/g' " + conf_file)
    exec_cmd(client, username, "sed -i 's/@masterip/" + masterip + "/g' " + conf_file)
    exec_cmd(client, username, "sed -i 's/@slaveip/" + slaveip + "/g' " + conf_file)
    exec_cmd(client, username, "sed -i 's/@second_check_ip/" + second_check_ip + "/g' " + conf_file)
    #exec_cmd(client, username, "sed -i 's/root/dbadm/g'" + util_file)
    exec_cmd(client, username, "sed -i 's/@masterip/" + masterip + "/g' " + util_file)
    exec_cmd(client, username, "sed -i 's/@slaveip/" + slaveip + "/g' " + util_file)
    exec_cmd(client, username, "sed -i 's/@sshport/" + str(port) + "/g' " + util_file)
    exec_cmd(client,username,"chmod +x /etc/masterha/app1/scripts/*")
    exec_cmd(client,username,"chmod 700 /etc/masterha")
    exec_cmd(client,username,"chown root.mysql /etc/masterha")
    print("mha build_mha done!")


def install(masterip,slaveip,port,username,password,mhapwd,replpwd,second_check_ip, version):
    master_client = get_ssh_client(masterip, username, password, port)
    slave_client = get_ssh_client(slaveip, username, password, port)
    master_install = my_thread(build_mha,(master_client,username, port,masterip, slaveip, mhapwd, replpwd, second_check_ip, version))
    slave_install = my_thread(build_mha,(slave_client,username, port,masterip, slaveip, mhapwd, replpwd, second_check_ip, version))
    master_install.start()
    sleep(10)
    slave_install.start()
    
    while(master_install.is_alive() or slave_install.is_alive()):
        print("waiting mha install to finish... 15s")
        sleep(15)

    #mha check
    stdin,replstdout,stderr = exec_cmd(slave_client, username, "masterha_check_repl --conf=/etc/masterha/proxy_app_default.cnf")
    stdin,sshstdout,stderr = exec_cmd(slave_client, username, "masterha_check_ssh --conf=/etc/masterha/proxy_app_default.cnf")

    #修复masterha_secondary_check 只能使用22端口的一个bug
    exec_cmd(master_client,username,"sed -i 's/22/8888/g' /usr/bin/masterha_secondary_check")
    exec_cmd(slave_client,username,"sed -i 's/22/8888/g' /usr/bin/masterha_secondary_check")
    #启动MHA
    exec_cmd(slave_client, username, "sh /etc/masterha/start.sh")
    
    return

def init_mha_user(masterip, slaveip,second_check_ip,port,username,password,rootpwd,mhapwd):
    client = get_ssh_client(masterip, username, password, port)
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = low'")
    exec_cmd(client, username, "mysql -u root -e \"create user mha@\'%s\' identified with mysql_native_password by \'%s\'\"" % (masterip,mhapwd))
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to mha@\'%s\'\"" % (masterip))
    exec_cmd(client, username, "mysql -u root -e \"create user mha@\'%s\' identified with mysql_native_password by \'%s\'\"" % (slaveip,mhapwd))
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to mha@\'%s\'\"" % (slaveip))
    exec_cmd(client, username, "mysql -u root -e \"create user mha@\'%s\' identified with mysql_native_password by \'%s\'\"" % (second_check_ip,mhapwd))
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to mha@\'%s\'\"" % (second_check_ip))
    exec_cmd(client, username, "mysql -u root -e \"flush privileges\"")
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = MEDIUM'")
    print("mha init_mha_user done!")
    return

def init_mha_user_5(masterip, slaveip,second_check_ip,port,username,password,rootpwd,mhapwd):
    client = get_ssh_client(masterip, username, password, port)
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = low'")
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to mha@\'%s\' identified by \'%s\'\"" % (masterip,mhapwd))
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to mha@\'%s\' identified by \'%s\'\"" % (slaveip,mhapwd))
    exec_cmd(client, username, "mysql -u root -e \"grant all on *.* to mha@\'%s\' identified by \'%s\'\"" % (second_check_ip,mhapwd))
    exec_cmd(client, username, "mysql -u root -e \"flush privileges\"")
    exec_cmd(client, username, "mysql -u root -e 'set global validate_password_policy = MEDIUM'")
    print("mha init_mha_user done!")
    return

def main(masterip,slaveip,port,rootpwd,mhapwd,replpwd,username,password,second_check_ip, version):
    print("mha script install began.")
    upload_file(masterip, username, password, port, mha_script_upload_file_list)
    upload_file(slaveip, username, password, port, mha_script_upload_file_list)
    try:
        if (version == '8.0'):
            init_mha_user(masterip, slaveip, second_check_ip, port, username, password, rootpwd, mhapwd)
            install(masterip, slaveip, port, username, password, mhapwd, replpwd, second_check_ip, version)
        elif (version == '5.7'):
            init_mha_user_5(masterip, slaveip, second_check_ip, port, username, password, rootpwd, mhapwd)
            install(masterip, slaveip, port, username, password, mhapwd, replpwd, second_check_ip, version)
        elif (version == '5.6'):
            init_mha_user_5(masterip, slaveip, second_check_ip, port, username, password, rootpwd, mhapwd)
            install(masterip, slaveip, port, username, password, mhapwd, replpwd, second_check_ip, version)

    except Exception as e:
        print("error: %s" % e)
    else:
        return "mha_install_ok"
        print("mha script install finished")
