#!/usr/bin/env python
# -*- coding: utf-8 -*-
import keepalived_install
import argparse
import getpass

parser = argparse.ArgumentParser(description="MZKeepalived");
parser.add_argument("vip");
parser.add_argument("masterip");
parser.add_argument("slaveip");
parser.add_argument("--user",metavar="ssh_user",dest="username",required=True,help='ssh user for login which should have the sudo root privilege or is root.')

parser.add_argument("--password",metavar="ssh_password",dest="password",help='ssh password for login.')

parser.add_argument("--port",metavar="ssh_port",dest="port",type=int,default=8888,help='ssh port for login.')


args=parser.parse_args()
if (args.password == None):
    args.password = getpass.getpass("Enter password: ")


keepalived_install.main(args.vip, args.username, args.password, args.port, args.masterip, args.slaveip);
