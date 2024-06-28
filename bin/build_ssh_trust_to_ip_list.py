# -*- coding: UTF-8 -*-
from ssh_util import *

def publish_pubkey(pubkey, ip_to_list, username, password, port):
    keys_file = "/root/.ssh/authorized_keys"
    for ip in ip_to_list:
        # print(ip)
        # print(pubkey)
        client = get_ssh_client(ip, username, password, port)
        exec_cmd(client, username, "mkdir -p /root/.ssh")
        exec_cmd(client, username, "touch " + keys_file)
        # 匹配关键字进行删除
        #exec_cmd_no_check(client, username, "sed -i /.*" + ip + ".*/d " + keys_file)
        if (username == "root"):
            exec_cmd(client, username, "echo \'" + pubkey + "\' | tee --append  " + keys_file)
        else:
            exec_cmd(client, "root", "echo \'" + pubkey + "\' | sudo tee --append  " + keys_file)
        client.close()
    return

def change_ssh_config(ip_to_list, username, password, port):
    ssh_cfg_file = "/etc/ssh/ssh_config"
    for ip in ip_to_list:
        client = get_ssh_client(ip, username, password, port)
        exec_cmd(client, username, "echo 'StrictHostKeyChecking no' | tee --append " + ssh_cfg_file)
    return

def disable_strict_knowhosts(ip_to_list, username, password, port):
    ssh_cfg_file = "/root/.ssh/config"
    for ip in ip_to_list:
        client = get_ssh_client(ip, username, password, port)
        exec_cmd_no_check(client, username, "sed -i '/^StrictHostKeyChecking.*/d' " + ssh_cfg_file)
        if (username == "root"):
            exec_cmd(client, username, "echo 'StrictHostKeyChecking no' | tee --append " + ssh_cfg_file)
        else:
            exec_cmd(client, "root", "echo 'StrictHostKeyChecking no' | sudo tee --append " + ssh_cfg_file)
    return

def establish_ssh_trust_to(ip_from, ip_to_list, username, password, port=8888):
    from_client = get_ssh_client(hostname=ip_from, username=username, password=password, port=port)
    privateKeyFile = "/root/.ssh/id_rsa"
    exec_cmd(from_client, username, "rm -f " + privateKeyFile)
    exec_cmd(from_client, username, "rm -f " + privateKeyFile + ".pub")
    exec_cmd(from_client, username, "mkdir -p /root/.ssh")
    stdin, stdout, stderr = exec_cmd(from_client, username, "/usr/bin/ssh-keygen -t rsa -f " + privateKeyFile + " -P ''")
    if (stdout.channel.recv_exit_status() == 0):
        print("ok for generate pub key.")
        stdin, stdout, stderr = exec_cmd(from_client, username, 'cat ' + privateKeyFile + '.pub ')
        if (stdout.channel.recv_exit_status() == 0):
            print("ok for get pub key.")
            pubkey = stdout.readlines()[0]
            print(pubkey)
            publish_pubkey(pubkey, ip_to_list, username, password, port)
            disable_strict_knowhosts(ip_to_list, username, password, port)
            change_ssh_config(ip_to_list, username, password, port)
        if (username != "root"):
            exec_cmd(from_client, username, "rm -f /root/.ssh/id_rsa /root/.ssh/id_rsa.pub")
            exec_cmd(from_client, username, "cp /root/.ssh/id_rsa /root/.ssh/id_rsa")
            exec_cmd(from_client, username, "cp /root/.ssh/id_rsa.pub /root/.ssh/id_rsa.pub")

def main(ip_from, username, password, port, ip_to_list):
    establish_ssh_trust_to(ip_from, ip_to_list, username, password, port)
