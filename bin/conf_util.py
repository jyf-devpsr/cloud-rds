#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import system as system_call  # Execute a shell command
import os
from platform import system as system_name  # Returns the system/OS name
import subprocess
from time import sleep

from ssh_util import *

ip_set=set()
def check_ip_duplicated(ip):
    old_len = len(ip_set)
    ip_set.add(ip)
    newlen = len(ip_set)
    if (old_len == newlen):        
        print("Invalid format,%s is configured twice in config file." % ip)
        exit(2)
def ping(host):
    try:
        # Ping parameters as function of OS
        parameters = "-n 1 -w 2" if system_name().lower()=="windows" else "-c 1 -w 2"
        rs = subprocess.call(("ping " + parameters + " " + host),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        # Pinging
    except:
        raise Exception('ping is not ok！')
    else:
        return rs

def sure_length(line,length,install_type):
    if (len(line) != length):
        print("%s, Invalid conf file format for install_type %s" % (line,install_type))
        exit(2)
def sure_ip_reachable(ip,ssh_user,ssh_pwd,ssh_port, timeout):
    #response = os.system("ping -c 1 -w 2 " + ip + " > /dev/null 2>&1")
    response = ping(ip)
    if (response != 0):
        print("error: ping " + ip + " failed,exit ")
        exit(1)
    client = get_ssh_client(ip,  ssh_user, ssh_pwd, ssh_port, timeout)
    client.close()

def sure_vip_not_reachable(ip):
    response = ping(ip)
    if (response == 0):
        print("error: vip " + ip + " is used somewhere !")
        exit(2)
    
def sure_dir_empty(ip,ssh_user,ssh_pwd,ssh_port,datadir):
    client = get_ssh_client(ip,  ssh_user, ssh_pwd, ssh_port)
    stdin,stdout,stderr = exec_cmd_no_check(client, ssh_user, "test -d " + datadir)
    if (stdout.channel.recv_exit_status() == 0):
        stdin,stdout,stderr = exec_cmd_no_check(client, ssh_user, "test \"$(ls -A %s)\" " % (datadir))
        if (stdout.channel.recv_exit_status() == 0):
            print("error: %s datadir %s is not empty ,can't install mysql." % (ip,datadir))
            exit(2)
def check_file_exist(file):
    if not os.path.isfile(file):       
        print('Files %s not found,exit' % file)
        exit(2)

def pre_install_check(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, second_checkip, datadir, install_type):
    if ( install_type == "single"):
        parse_single(install_type,ssh_user,ssh_pwd,ssh_port)
    elif (install_type == "repl"):
        parse_repl(install_type,ssh_user,ssh_pwd,ssh_port)
    elif (install_type == "mha"):
        parse_mha(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, second_checkip, datadir)
    elif (install_type == "cluster"):
        parse_add_slave(install_type,ssh_user,ssh_pwd,ssh_port)

#ip datadir    
def parse_single(line,install_type,ssh_user,ssh_pwd,ssh_port):
    sure_length(line,2,install_type)
    ip = line[0]
    check_ip_duplicated(ip)
    datadir = line[1]
    sure_ip_reachable(ip,  ssh_user, ssh_pwd, ssh_port)
    sure_dir_empty(ip,  ssh_user, ssh_pwd, ssh_port,datadir)

#masterip slaveip datadir
def parse_repl(line,install_type,ssh_user,ssh_pwd,ssh_port):
    sure_length(line,3,install_type)
    masterip = line[0]
    check_ip_duplicated(masterip)
    slaveip = line[1]
    check_ip_duplicated(slaveip)
    datadir = line[2]
    sure_ip_reachable(masterip,  ssh_user, ssh_pwd, ssh_port)
    sure_dir_empty(masterip,  ssh_user, ssh_pwd, ssh_port,datadir)
    sure_ip_reachable(slaveip,  ssh_user, ssh_pwd, ssh_port)
    sure_dir_empty(slaveip,  ssh_user, ssh_pwd, ssh_port,datadir)


#masterip slaveip vip second_checkip datdir appUser appPwd
def parse_mha(masterip, slaveip, vip, ssh_user, ssh_pwd, ssh_port, second_checkip, datadir):
    try:
        timeout = 10
        print("began pre-install check...")
        check_ip_duplicated(masterip)
        check_ip_duplicated(slaveip)
        sure_ip_reachable(masterip, ssh_user, ssh_pwd, ssh_port, timeout)
        sure_dir_empty(masterip, ssh_user, ssh_pwd, ssh_port,datadir)
        sure_ip_reachable(slaveip, ssh_user, ssh_pwd, ssh_port, timeout)
        sure_dir_empty(slaveip, ssh_user, ssh_pwd, ssh_port,datadir)
        sure_vip_not_reachable(vip)
        sure_ip_reachable(second_checkip,ssh_user, ssh_pwd, ssh_port, timeout)
        print("pre-install check finished.")
    except:
        raise Exception('parse_mha is failed!')

#masterip slaveip vip
def parse_keep_alived(line,install_type,ssh_user,ssh_pwd,ssh_port):
    sure_length(line,3,install_type)
    vip = line[2]
    check_ip_duplicated(vip)
    sure_vip_not_reachable(vip)

#masterip slaveip second_checkip rootpwd
def parse_mha_script(line,install_type,ssh_user,ssh_pwd,ssh_port):
    sure_length(line, 4, install_type)
    second_checkip = line[2]
    sure_ip_reachable(second_checkip,  ssh_user, ssh_pwd, ssh_port)

#newslaveip datadir backupip backupuser backupwd masterip slaveip
def parse_add_slave(line,install_type,ssh_user,ssh_pwd,ssh_port):
    sure_length(line, 7, install_type)
    newslaveip = line[0]
    check_ip_duplicated(newslaveip)
    datadir = line[1]
    sure_ip_reachable(newslaveip,  ssh_user, ssh_pwd, ssh_port)
    sure_dir_empty(newslaveip,  ssh_user, ssh_pwd, ssh_port,datadir)