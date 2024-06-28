#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *
import random
import os

# 匹配关键字进行删除，crontab删除任务可以使用
#exec_cmd_no_check(client, username, "sed -i /.*" + ip + ".*/d " + keys_file)


# 生产机房备份
def config_backup_prod(slaveip, ssh_user, ssh_pwd, ssh_port, rds_id):
    try:
        my_host_id = '1'
        backup_hour= str(random.randint(0,6))
        client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
        # 使用gocron管理备份任务
        # 1、get token
        exec_cmd(client, ssh_user, "chmod +x get_gocron_token.sh")
        stdin, stdout, stderr = exec_cmd(client, ssh_user, "sh get_gocron_token.sh")
        l = stdout.readlines()
        get_token = l[0].split(',')[3].split(':')[1].split('"')[1]
        print(get_token)
        # 2、add gocron jobs
        exec_cmd(client, ssh_user, "sed -i 's/@gocron_token/" + get_token + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@rds_id/" + rds_id + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@my_host_id/" + my_host_id + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@backup_hour/" + backup_hour + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@slaveip/" + slaveip + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "chmod +x add_gocron_jobs.sh")
        stdin, stdout, stderr = exec_cmd(client, ssh_user, "sh add_gocron_jobs.sh")
        l_add = stdout.readlines()
        add = l_add[0].split(',')[0].split(':')[1]
        add_res = add.encode('utf-8')
        if add_res == '0':
            print("gocron job add ok.")
            print("base-backup config ok!")
        else:
            print("error: gocron job add failed!!! %s" % l_add)

    except Exception as e:
        print("error: %s" % e)
    else:
        return "config_backup_ok"

# 安装cfs插件
def install_cfs(slaveip, ssh_user, ssh_pwd, ssh_port, second_check_ip):
    try:
        client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
        exec_cmd(client, ssh_user, "modprobe fuse")
        exec_cmd(client, ssh_user, "yum install -y fuse")
        exec_cmd(client, ssh_user, "rm -rf /cfs")
        exec_cmd(client, ssh_user, "mkdir -p /cfs /mnt/cloudBackup")
        exec_cmd(client, ssh_user, "wget http://%s:8080/software/mysql/client.tar" % (second_check_ip))
        exec_cmd(client, ssh_user, "tar xvf client.tar && mv client /cfs/")
        exec_cmd(client, ssh_user, "nohup /cfs/client/cfs-client -f -c /cfs/client/config.json &")
    except Exception as e:
        print("error: %s" % e)
    else:
        return "install_cfs_ok"

# 测试机房备份
# 测试机房需要单独单价gocron，因为要迁移，短期先使用slave直接备份方案
def config_backup_dev(slaveip, ssh_user, ssh_pwd, ssh_port, second_check_ip, keep_days="180"):
    try:
        backup_hour = random.randint(1,5)
        backup_min = random.randint(1,59)
        # 配置cfs备份存储
        install_cfs(slaveip, ssh_user, ssh_pwd, ssh_port, second_check_ip)
        client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
        data_dir = 'mnt/cloudBackup'
        exec_cmd(client, ssh_user, "yum localinstall -y mydumper-0.15.0-7.el7.x86_64.rpm")
        exec_cmd(client, ssh_user, "mkdir -p /data/dbbackup/{logs,scripts}")
        exec_cmd(client, ssh_user, "sed -i 's/@slavehost/" + slaveip + "/g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "sed -i 's:@data_dir:" + data_dir + ":g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@mzbackupdir/" + slaveip + "/g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@keep_days/" + keep_days + "/g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user,
                 "mv xxxxxxx_mydumper_backup.sh /data/dbbackup/scripts/xxxxxxx_mydumper_backup_%s.sh" % slaveip)
        exec_cmd(client, ssh_user, "chmod +x /data/dbbackup/scripts/xxxxxxx_mydumper_backup_%s.sh" % slaveip)

        exec_cmd(client, ssh_user,
                 "(echo \"%s %s * * * /data/dbbackup/scripts/xxxxxxx_mydumper_backup_%s.sh >> /data/dbbackup/logs/xxxxxxx_mysql_backup_%s.log 2>&1\" ; crontab -l )| crontab" % (
                 backup_min, backup_hour, slaveip, slaveip))
        print("local crontab config ok!")
        print("base-backup config ok!")
    except Exception as e:
        print("error: %s" % e)
    else:
        return "config_backup_ok"



