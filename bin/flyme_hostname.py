#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bin.ssh_util import *



def change_xxxxxxx_hostname(masterip, slaveip, ssh_user, ssh_pwd, ssh_port, version, zone):
    if (zone == "default_prod" or zone == "default_prod_b" or zone == "default_prod_c" or zone == "default_prod_d" or zone == "default_prod_e"):
        zone_name = 'prod'
    elif zone == 'default_dev':
        zone_name = 'dev'
    elif zone == 'default_test':
        zone_name = 'test'
    else:
        zone_name = 'test'

    client = get_ssh_client(masterip, ssh_user, ssh_pwd, ssh_port)
    exec_cmd(client,ssh_user, "hostnamectl set-hostname xxxxxxx-cloud-mysql-%s-%s-%s-%s" %(version,zone_name,'master',masterip))
    client = get_ssh_client(slaveip, ssh_user, ssh_pwd, ssh_port)
    exec_cmd(client,ssh_user, "hostnamectl set-hostname xxxxxxx-cloud-mysql-%s-%s-%s-%s" %(version,zone_name,'slave',slaveip))


