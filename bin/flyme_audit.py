#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *
import random

# 匹配关键字进行删除，crontab删除任务可以使用
#exec_cmd_no_check(client, username, "sed -i /.*" + ip + ".*/d " + keys_file)


# only use prod
def config_audit(slaveip, ssh_user, ssh_pwd, ssh_port, second_check_ip, rds_id, keep_days="180"):
    try:
        install_audit(slaveip, ssh_user, ssh_pwd, ssh_port, second_check_ip)
        client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
        data_dir = 'mnt/DBbackup'
        exec_cmd(client, ssh_user, "yum localinstall -y mydumper-0.15.0-7.el7.x86_64.rpm")
        exec_cmd(client, ssh_user, "mkdir -p /data/dbbackup/{logs,scripts}")
        exec_cmd(client, ssh_user, "sed -i 's/@slavehost/" + slaveip + "/g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "sed -i 's:@data_dir:" + data_dir + ":g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@mzbackupdir/" + slaveip + "/g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@keep_days/" + keep_days + "/g' xxxxxxx_mydumper_backup.sh")
        exec_cmd(client, ssh_user, "mv xxxxxxx_mydumper_backup.sh /data/dbbackup/scripts/xxxxxxx_mydumper_backup_%s.sh" % slaveip)
        exec_cmd(client, ssh_user, "chmod +x /data/dbbackup/scripts/xxxxxxx_mydumper_backup_%s.sh" % slaveip)
        """
        # 迭代成gocron
        exec_cmd(client, ssh_user,
                 "(echo \"%s %s * * * /data/dbbackup/scripts/xxxxxxx_mydumper_backup_%s.sh >> /data/dbbackup/logs/xxxxxxx_mysql_backup_%s.log 2>&1\" ; crontab -l )| crontab" % (
                 backup_min, backup_hour, slaveip, slaveip))
        """
        # 使用gocron管理备份任务
        # 1、get token
        exec_cmd(client, ssh_user, "sed -i 's/@job_host/" + job_host + "/g' get_gocron_token.sh")
        stdin, stdout, stderr = exec_cmd(client, ssh_user, "chmod +x && sh add_gocron_jobs.sh")
        print(stdout.readlines())
        get_token = stdout.readlines()

        # 2、add gocron jobs
        exec_cmd(client, ssh_user, "sed -i 's/@gocron_token/" + get_token + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@rds_id/" + rds_id + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@job_host/" + job_host + "/g' add_gocron_jobs.sh")
        exec_cmd(client, ssh_user, "sed -i 's/@backup_hour/" + backup_hour + "/g' add_gocron_jobs.sh")
        stdin, stdout, stderr = exec_cmd(client, ssh_user, "chmod +x && sh add_gocron_jobs.sh")
        if stdout.readlines()["code"] == 0 and stdout.readlines()["message"] == "保存成功":
            print("gocron job add ok.")
        else:
            raise
        # drop gocron jobs:

    except Exception as e:
        print("error: %s" % e)
    else:
        return "config_backup_ok"


def install_audit(slaveip, ssh_user, ssh_pwd, ssh_port, second_check_ip):
    try:
        client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
        exec_cmd(client, ssh_user, "modprobe fuse")
        exec_cmd(client, ssh_user, "yum install -y fuse")
        exec_cmd(client, ssh_user, "rm -rf /cfs")
        exec_cmd(client, ssh_user, "mkdir -p /cfs /mnt/DBbackup")
        exec_cmd(client, ssh_user, "wget http://%s:8080/software/mysql/client.tar" % (second_check_ip))
        exec_cmd(client, ssh_user, "tar xvf client.tar && mv client /cfs/")
        exec_cmd(client, ssh_user, "nohup /cfs/client/cfs-client -f -c /cfs/client/config.json &")
    except Exception as e:
        print("error: %s" % e)
    else:
        return "install_cfs_ok"



