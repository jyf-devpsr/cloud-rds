#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mha_script_install
import argparse
import build_ssh_trust_to_ip_list
from mysql_install import gen_password
import getpass

parser = argparse.ArgumentParser(description="MeizuInstallMha")
parser.add_argument("masterip")
parser.add_argument("slaveip")
parser.add_argument("second_check_ip",help="when check found mysql died,mha need to login to anothoner ip to do a second check to see if mysql really down.")
parser.add_argument("rootpwd")
parser.add_argument("--user",metavar="ssh_user",dest="username",required=True,help='ssh user for login which should have the sudo root privilege or is root.')

parser.add_argument("--password",metavar="ssh_password",dest="password",help='ssh password for login.')

parser.add_argument("--port",metavar="ssh_port",dest="port",type=int,default=8888,help='ssh port for login.')

args=parser.parse_args()
if (args.password == None):
    args.password = getpass.getpass()
replpwd = gen_password()
mhapwd = gen_password()

ip_to_list=[args.masterip,args.slaveip,args.second_check_ip]
build_ssh_trust_to_ip_list.main(args.masterip, args.username, args.password, args.port, ip_to_list)
build_ssh_trust_to_ip_list.main(args.slaveip, args.username, args.password, args.port, ip_to_list)
mha_script_install.main(args.masterip, args.slaveip, args.port, args.rootpwd, mhapwd, replpwd, args.username, args.password, args.second_check_ip)
