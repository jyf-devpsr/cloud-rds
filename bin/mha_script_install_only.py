#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ssh_util import *
from bin.mha_script_install import *
from upload_file_const import mha_script_upload_file_list


def genPassword():
    passwd = os.popen(
        "< /dev/urandom tr -dc '1234567890qwert_QWERTasdfgASDFGzxcvbZXCVByhnujmikolp' 2>/dev/null | head -c 16 ").readlines()[
        0]
    return passwd


def mha_script_install_only(config, username, password, port):
    for info in config:
        masterip = info[0]
        slaveip = info[1]
        secondCheckIP = info[2]
        rootpwd = info[3]
        client = get_ssh_client(slaveip, username, password, port)
        stdin, stdout, stderr = exec_cmd(client, username,
                                         "mysql -uroot -p%s -Nse 'select user_password from mysql.slave_master_info'" % (
                                             rootpwd))
        replpwd = ''.join(stdout.readlines()).strip('\n')
        mhapwd = genPassword()
        print("mha script install began.")
        init_mha_user(masterip, slaveip, secondCheckIP, port, username, password, rootpwd, mhapwd)
        upload_file(masterip, username, password, port, mha_script_upload_file_list)
        upload_file(slaveip, username, password, port, mha_script_upload_file_list)
        install(masterip, slaveip, port, username, password, mhapwd, replpwd, secondCheckIP)
        print("mha script install finished")
