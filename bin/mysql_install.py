#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ssh_util import *
import sys
import os
from random import choice
from worker import *
from time import sleep
import string
import keepalived_install
import proxysql_install
import mha_script_install
import build_ssh_trust_to_ip_list
from upload_file_const import *
import random
from xxxxxxx_backup import *
from xxxxxxx_whitelist import *


# 生成符合数据库要求的随机密码
def gen_password():
    number = string.digits
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    random_list = (random.sample(number, 4) + random.sample(uppercase, 5) + random.sample(lowercase, 5) + random.sample(
        '._-%#', 2))
    random.shuffle(random_list)
    passwd = ''.join(random_list)
    return passwd


# 多线程循环检查存活状态
def wait_all_to_finish(thread_list):
    # wait for other thread to begin so sleep 30 second.
    sleep(30)
    alive = False
    for thread in thread_list:
        if (thread.is_alive()):
            alive = True
    while alive:
        print("wait mysql install to finish 30s ...")
        sleep(30)
        alive = False
        for thread in thread_list:
            if (thread.is_alive()):
                alive = True


# 修改root密码
def change_root_pwd(masterip, username, password, port, rootpwd, version):
    client = get_ssh_client(masterip, username, password, port)
    if (version =='8.0'):
        exec_cmd(client, username,
                 "mysql -u root -e \"create USER 'root'@'%'  IDENTIFIED WITH mysql_native_password BY 'xxxxxxxxxxxxxx.!@#'\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"grant all on *.* to 'root'@'%' with grant option;flush privileges;\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"ALTER USER 'root'@'localhost'  IDENTIFIED WITH mysql_native_password BY 'xxxxxxxxxxxxxx.!@#';flush privileges;\"")
        # 注册到proxysql
        exec_cmd(client, username, "sh /var/lib/proxysql/proxysql/bin/add_user.sh root '%s'" % (rootpwd))
        print("password for root@'localhost' on " + masterip + " is changed!")
    elif (version =='5.7'):
        exec_cmd(client, username,
                 "mysql -u root -e \"grant all on *.* to 'root'@'%' IDENTIFIED BY 'xxxxxxxxxxxxxx.!@#' with grant option;flush privileges;\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"ALTER USER 'root'@'localhost' IDENTIFIED BY 'xxxxxxxxxxxxxx.!@#';flush privileges;\"")
        # 注册到proxysql
        exec_cmd(client, username, "sh /var/lib/proxysql/proxysql/bin/add_user.sh root '%s'" % (rootpwd))
        print("password for root@'localhost' on " + masterip + " is changed!")
    elif  (version =='5.6'):
        exec_cmd(client, username,
                 "mysql -u root -e \"grant all on *.* to 'root'@'%' IDENTIFIED BY 'xxxxxxxxxxxxxx.!@#' with grant option;flush privileges;\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"SET PASSWORD FOR 'root'@'localhost' = PASSWORD('xxxxxxxxxxxxxx.!@#');flush privileges;\"")
        # 注册到proxysql
        exec_cmd(client, username, "sh /var/lib/proxysql/proxysql/bin/add_user.sh root '%s'" % (rootpwd))
        print("password for root@'localhost' on " + masterip + " is changed!")


# 删除安装的产生的临时文件
def rm_temp_file(ip, username, password, port):
    client = get_ssh_client(ip, username, password, port)
    try:
        print("on %s clear temp files..." % (ip))
        exec_cmd(client, username,
                 "rm -rf mha4mysql-* build_mysql* Percona-Server-* proxysql* masterha* my_80.cnf* my_5* init_hostname.py mydumper-0.15.0* mysql-5.6*")
        exec_cmd(client, username,
                 "rm -rf xxxxxxx_mydumper_backup.sh client.tar install_monitor.sh monmysql.tar.gz mysql8-xxxxxxx-cloud* mysql_run.err manager_0.56.rpm node_0.56.rpm")
    except Exception as e:
        print("Install temp file rm fail: %s" % (e))


# 创建并初始化xxxxxxx_root用户
def init_xxxxxxx_root(masterip, slaveip, username, password, port, xxxxxxx_rootpwd, version):
    client = get_ssh_client(masterip, username, password, port)
    if (version == '8.0'):
        exec_cmd(client, username,
                 "mysql -u root -e \"create user 'xxxxxxx_root'@'%' identified with mysql_native_password by '" + xxxxxxx_rootpwd + "';grant all on *.* to 'xxxxxxx_root'@'%' with grant option;flush privileges;\"")
    else:
        exec_cmd(client, username,
                 "mysql -u root -e \"grant all on *.* to 'xxxxxxx_root'@'%' identified by '" + xxxxxxx_rootpwd + "' with grant option;flush privileges;\"")
    exec_cmd(client, username, "/etc/init.d/mysqld restart")
    print(
        " password for 'xxxxxxx_root'@'%' on " + masterip + " is " + xxxxxxx_rootpwd + ",also the password is stored in /root/.mysql_secret_xxxxxxx_root of master mysql")
    if (username == 'root'):
        exec_cmd(client, username, "echo " + xxxxxxx_rootpwd + " > /root/.mysql_secret_xxxxxxx_root")
    else:
        exec_cmd(client, "root", "echo " + xxxxxxx_rootpwd + " | sudo tee --append  /root/.mysql_secret_xxxxxxx_root")
    return


# 初始化内置管理用户
def init_inner_users(masterip, username, password, port, version):
    client = get_ssh_client(masterip, username, password, port)
    if (version == '8.0'):
        # 备份用户
        exec_cmd(client, username,
                 "mysql -u root -e \"create user 'backup'@'%' identified with mysql_native_password by 'xxxxxxx'\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"GRANT SELECT, RELOAD, BACKUP_ADMIN, PROCESS, SHOW DATABASES, SUPER, LOCK TABLES, REPLICATION SLAVE, REPLICATION CLIENT, SHOW VIEW, EVENT, TRIGGER ON *.* TO 'backup'@'%'\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"create user 'backup'@'localhost' identified with mysql_native_password by 'xxxxxxxx'\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"GRANT SELECT, RELOAD, BACKUP_ADMIN, PROCESS, SHOW DATABASES, SUPER, LOCK TABLES, REPLICATION SLAVE, REPLICATION CLIENT, SHOW VIEW, EVENT, TRIGGER ON *.* TO 'backup'@'localhost'\"")
        # zabbix、夜莺等外部监控用户
        exec_cmd(client, username,
                 "mysql -u root -e \"create user 'monitor'@'localhost' identified with mysql_native_password by 'xxxxx'\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"GRANT SELECT,SUPER,SHOW DATABASES,REPLICATION SLAVE,PROCESS,REPLICATION CLIENT on *.* to 'monitor'@'localhost'\"")
    else:
        # 备份用户
        exec_cmd(client, username,
                 "mysql -u root -e \"GRANT all ON *.* TO 'backup'@'%' identified by 'bxxxxxxxxxxxxzu'\"")
        exec_cmd(client, username,
                 "mysql -u root -e \"GRANT all ON *.* TO 'backup'@'localhost' identified by 'bacxxxxxxxxzu'\"")
        # zabbix、夜莺等外部监控用户
        exec_cmd(client, username,
                 "mysql -u root -e \"GRANT SELECT,SUPER,SHOW DATABASES,REPLICATION SLAVE,PROCESS,REPLICATION CLIENT on *.* to 'monitor'@'localhost' identified by 'Moxxxxxxxxxxxxxeizu'\"")
    exec_cmd(client, username, "mysql -u root -e \"flush privileges\"")
    exec_cmd(client, username, "/etc/init.d/mysqld restart")
    print(" Inner users is added!!!")
    exec_cmd(client, username, "mysql -u root -e \"select user,host from mysql.user\"")
    print(
        " User:backup@'localhost' Password:backudxxxxxxxxxxxxxxxu\n User:backup@'%' Password:backupxxxxxxxxxxxxxxu\n User:monitor@'localhost' Password:Monxxxxxxxxxxxxxxxu\n")
    return


# 检查mysql存活状态
def check_mysql_running(ip, username, password, port):
    client = get_ssh_client(ip, username, password, port)
    try:
        exec_cmd(client, username, "/etc/init.d/mysqld status")
    except Exception:
        print(ip + " install mysql failed,mysql is not running.")
        raise
        exit(2)
    return

def check_repl_is_ok(ip, username, password, port):
    client = get_ssh_client(ip, username, password, port)
    try:
        exec_cmd(client, username, "mysql -u root -e \"show slave status\"")
    except Exception:
        print(ip + " repl config failed,repl is not ok.")
        raise
        exit(2)
    return

# 检查mysql主从复制状态
def check_repl(masterip, slaveip, client, username):
    stdin, stdout, stderr = exec_cmd(client, username, "mysql -u root -e 'show slave status\G'")
    slave_status = stdout.readlines()
    for line in slave_status:
        if (line.find("Slave_IO_Running:") > -1 and not (line.find("Yes") > -1)):
            print(line)
            print("Build master-slave replication for %s(m)-%s(s) failed,please check." % (masterip, slaveip))
            exit(2)
        if (line.find("Slave_SQL_Running:") > -1 and not (line.find("Yes") > -1)):
            print(line)
            print("Build master-slave replication  for %s(m)-%s(s) failed,please check." % (masterip, slaveip))
            exit(2)
    print("build master-slave replication for %s(m)-%s(s) successfully." % (masterip, slaveip))
    return


# 配置主从复制
def config_repl(masterip, slaveip, username, password, port, replpwd, version):
    masterClient = get_ssh_client(masterip, username, password, port)
    slaveClient = get_ssh_client(slaveip, username, password, port)
    if (version == '8.0'):
        create_repl_user_tmp = "create user repl@\"%s\" identified with mysql_native_password by \"%s\""
        grant_repl_user_tmp = "grant replication client,replication slave on *.* to repl@\"%s\""
        # create user
        create_repl_user = create_repl_user_tmp % (slaveip, replpwd)
        exec_cmd(masterClient, username, "mysql -u root -e '" + create_repl_user + "'")
        create_repl_user = create_repl_user_tmp % (masterip, replpwd)
        exec_cmd(masterClient, username, "mysql -u root -e '" + create_repl_user + "'")
        # grant
        grant_repl_user = grant_repl_user_tmp % (slaveip)
        exec_cmd(masterClient, username, "mysql -u root -e '" + grant_repl_user + "'")
        grant_repl_user = grant_repl_user_tmp % (masterip)
        exec_cmd(masterClient, username, "mysql -u root -e '" + grant_repl_user + "'")
    else:
        grant_repl_user_tmp = "grant replication client,replication slave on *.* to repl@\"%s\" identified by \"%s\""
        # grant
        grant_repl_user = grant_repl_user_tmp % (slaveip, replpwd)
        exec_cmd(masterClient, username, "mysql -u root -e '" + grant_repl_user + "'")
        grant_repl_user = grant_repl_user_tmp % (masterip, replpwd)
        exec_cmd(masterClient, username, "mysql -u root -e '" + grant_repl_user + "'")

    change_master_to = "change master to master_host=\"%s\",master_port=3306,master_user=\"repl\",master_password=\"%s\",master_auto_position=1;"
    change_master_to = change_master_to % (masterip, replpwd)
    sleep(10)
    exec_cmd(slaveClient, username, "mysql -u root -e  'set global read_only=on;'")
    exec_cmd(slaveClient, username, "mysql -u root -e  'stop slave;reset slave all;" + change_master_to + "start slave;'")
    exec_cmd(slaveClient, username, "/etc/init.d/mysqld restart")
    sleep(10)
    print(" repl password is " + replpwd + " and stored in /root/.repl_secret of slave node ")
    if (username == 'root'):
        exec_cmd(slaveClient, username, "echo " + replpwd + " > /root/.repl_secret")
    else:
        exec_cmd(slaveClient, "root", "echo " + replpwd + " | sudo tee --append  /root/.repl_secret")
    return

# 启动多线程配置主从
def install_repl(masterip, slaveip, username, password, port, datadir, rootpwd, replpwd, upload_file_list,
                 xxxxxxx_rootpwd, second_check_ip, version):
    try:
        # 启动多线程,安装mysql软件
        master_worker = my_thread(install, (
        masterip, username, password, port, datadir, upload_file_list, second_check_ip, version))
        slave_worker = my_thread(install, (
        slaveip, username, password, port, datadir, upload_file_list, second_check_ip, version))
        master_worker.start()
        sleep(5)
        slave_worker.start()

        while (master_worker.is_alive() or slave_worker.is_alive()):
            sleep(30)

        check_mysql_running(masterip, username, password, port)
        check_mysql_running(slaveip, username, password, port)

        config_repl(masterip, slaveip, username, password, port, replpwd, version)
        sleep(30)
        # check repl
        check_repl_is_ok(slaveip, username, password, port)

        init_xxxxxxx_root(masterip, slaveip, username, password, port, xxxxxxx_rootpwd, version)
        init_inner_users(masterip, username, password, port, version)
    except Exception as e:
        print("error: %s" % e)
    else:
        return "repl_install_ok"

# 安装mysql软件
def install(ip, username, password, port, datadir, upload_file_list, second_check_ip, version):
    try:
        my_files = ['Percona-Server-5.7.43-47-Linux.x86_64.glibc2.17.tar.gz','mysql-5.6.51-linux-glibc2.12-x86_64.tar.gz']
        print(ip + " install mysql began.")
        upload_file(ip, username, password, port, upload_file_list)
        client = get_ssh_client(ip, username, password, port)
        # 调用主机名初始化脚本，对主机名进行初始化
        exec_cmd(client, username, "yum install -y python3")
        #exec_cmd(client, username, "python init_hostname.py")
        exec_cmd(client, username, "chmod +x build_mysql*")
        # 清空老互信
        exec_cmd(client, username, "rm -rf /root/.ssh")
        # 安装mysql
        if (version == '8.0'):
            exec_cmd(client, username, "sed -i 's#@datadir#" + datadir + "#g' build_mysql_80.sh")
            exec_cmd(client, username, "sed -i 's/ftp_host/" + second_check_ip + "/g' build_mysql_80.sh")
            exec_cmd(client, username, "sh build_mysql_80.sh > mysql_install.log 2>&1")
        elif (version == '5.7'):
            exec_cmd(client, username, "sed -i 's#@datadir#" + datadir + "#g' build_mysql_57.sh")
            exec_cmd(client, username, "sed -i 's/ftp_host/" + second_check_ip + "/g'  build_mysql_57.sh")
            exec_cmd(client, username, "sed -i 's/@mysql_xxxxxxx_file/" + my_files[0] + "/g'  build_mysql_57.sh")
            exec_cmd(client, username, "sh build_mysql_57.sh > mysql_install_5.log 2>&1")
        elif (version == '5.6'):
            exec_cmd(client, username, "sed -i 's#@datadir#" + datadir + "#g' build_mysql_56.sh")
            exec_cmd(client, username, "sed -i 's/ftp_host/" + second_check_ip + "/g'  build_mysql_56.sh")
            exec_cmd(client, username, "sed -i 's/@mysql_xxxxxxx_file/" + my_files[1] + "/g'  build_mysql_56.sh")
            exec_cmd(client, username, "sh build_mysql_56.sh > mysql_install_5.log 2>&1")

        # 安装监控
        # exec_cmd(client, username, "sh install_monitor.sh > mysql_install.log 2>&1")
        exec_cmd(client, username, "sed -i '/\[mysqld\]/a validate-password = FORCE_PLUS_PERMANENT' /etc/my.cnf")
        exec_cmd(client, username, "sed -i '/\[mysqld\]/a plugin-load-add = validate_password.so' /etc/my.cnf")

        client.close()
    except Exception as e:
        print("error: %s" % e)
    else:
        print(ip + " install mysql finished.")



# 安装mha
def install_mha(masterip, slaveip, vip, second_check_ip, ssh_user, ssh_password, ssh_port, datadir, rootpwd, replpwd,
                app_user,
                app_pwd, app_database, upload_file_list, xxxxxxx_rootpwd, version, zone, rds_id):
    try:
        mhapwd = 'mhameizu123'
        repl_result = install_repl(masterip, slaveip, ssh_user, ssh_password, ssh_port, datadir, rootpwd, replpwd,
                                   upload_file_list, xxxxxxx_rootpwd, second_check_ip, version)
        sleep(3)
        keep_result = keepalived_install.main(vip, ssh_user, ssh_password, ssh_port, masterip, slaveip)
        proxy_result = proxysql_install.main(masterip, slaveip, ssh_port, ssh_user, ssh_password, rootpwd, app_user,
                                             app_pwd, app_database, xxxxxxx_rootpwd, version)
        ip_to_list = [masterip, slaveip, second_check_ip]
        build_ssh_trust_to_ip_list.main(masterip, ssh_user, ssh_password, ssh_port, ip_to_list)
        build_ssh_trust_to_ip_list.main(slaveip, ssh_user, ssh_password, ssh_port, ip_to_list)
        sleep(5)
        mha_result = mha_script_install.main(masterip, slaveip, ssh_port, rootpwd, mhapwd, replpwd, ssh_user, ssh_password,
                                             second_check_ip, version)
        print("begin config base-backup...")
        # 配置备份
        if (zone == "default_prod" or zone == "default_prod_b" or zone == "default_prod_c" or zone == "default_prod_d" or zone == "default_prod_e"):
            # only prod backup
            config_backup_prod(slaveip, ssh_user, ssh_password, ssh_port, rds_id)
        else:
            # 测试和开发环境
            config_backup_dev(slaveip, ssh_user, ssh_password, ssh_port, second_check_ip)

        # 添加系统白名单
        # mater host
        system_whitelist(masterip, slaveip, ssh_user, ssh_password, ssh_port)
        # slave host
        system_whitelist(slaveip, masterip, ssh_user, ssh_password, ssh_port)


        # 修改root密码
        sleep(5)
        change_root_pwd(masterip, ssh_user, ssh_password, ssh_port, rootpwd,version)
        if (repl_result == 'repl_install_ok' and keep_result == 'keep_install_ok' and proxy_result == 'prxysql_install_ok' and mha_result == 'mha_install_ok'):
            print("all components install ok")
            return "all_install_ok"
    except Exception as e:
        print("error: %s" % e)
        


# 安装单点
def mysql_single_install(config, username, password, port, second_check_ip):
    thread_list = []
    for info in config:
        ip = info[0]
        datadir = info[1]
        thread = my_thread(install, (ip, username, password, port, datadir, mysql_upload_file_list, second_check_ip))
        thread.start()
        thread_list.append(thread)
        sleep(5)
    wait_all_to_finish(thread_list)
    for info in config:
        ip = info[0]
        rootpwd = gen_password()
        change_root_pwd(ip, username, password, port, rootpwd)
    print("all finished.")


# 安装主从
def mysql_repl_install(config, username, password, port):
    thread_list = []
    for info in config:
        masterip = info[0]
        slaveip = info[1]
        datadir = info[2]
        rootpwd = gen_password()
        replpwd = gen_password()
        thread = my_thread(config_repl, (
            masterip, slaveip, username, password, port, datadir, rootpwd, replpwd, mysql_upload_file_list))
        thread.start()
        thread_list.append(thread)
        sleep(5)
    wait_all_to_finish(thread_list)
    print("all finished.")

# 安装mha高可用架构
def mysql_mha_install(masterip, slaveip, vip, ssh_user, ssh_password, ssh_port, second_check_ip, datadir, app_user,
                        app_pwd, app_database, version, zone, rds_id):
    thread_list = []
    # mysql root密码
    rootpwd = 'xxxxxxxxxxxxxx.!@#'
    replpwd = gen_password()
    # 初始化内置用户
    xxxxxxx_rootpwd = gen_password()
    # 多线程并发
    try:
        thread = my_thread(install_mha, (
        masterip, slaveip, vip, second_check_ip, ssh_user, ssh_password, ssh_port, datadir, rootpwd, replpwd, app_user,
        app_pwd, app_database, mysql_upload_file_list, xxxxxxx_rootpwd, version, zone, rds_id))
        thread.start()
        thread_list.append(thread)
        wait_all_to_finish(thread_list)
        # 清理临时安装文件
        rm_temp_file(masterip, ssh_user, ssh_password, ssh_port)
        rm_temp_file(slaveip, ssh_user, ssh_password, ssh_port)
        if (thread.get_result() != 'all_install_ok'):
            raise Exception('all_install_not_ok')
    except Exception as e:
        print("error: %s " % e)
    else:
        print("all components finished.")
        return "deploy_ok"


