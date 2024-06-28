#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
import ntpath

def get_ssh_client(hostname,username,password,port,timeout=60):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, username=username, password=password,port=port,timeout=timeout)
    except Exception as e:
        print("error: get_ssh_client is failed,please check the network. error info: %s" % e)
    return client

def get_sftp_client(hostname,username,password,port):
    client = paramiko.Transport((hostname,port))
    client.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport(client)
    return sftp

def upload_file(hostname, username, password, port,uploadFileList):
    sftp = get_sftp_client(hostname, username, password, port)
    if (username == "root"):
        homedir = "/root/"
    else:
        homedir = "/home/" + username + "/"
    for path in uploadFileList:
        filename = ntpath.basename(path)
        #notice: here , the destination can't be a dir ,which will result in an error.
        #notice: ~ can't use
        sftp.put(path,homedir + filename)
        #print("Uploading " + filename + " to " + hostname + " succeeds.")          
        
def exec_cmd(client,username,cmd):
    #print(cmd)
    if (username == "root"):
        stdin,stdout,stderr=client.exec_command(cmd)
    else:
        stdin,stdout,stderr=client.exec_command("sudo " + cmd)

    #wait for the cmd to finish
    if (stdout.channel.recv_exit_status() != 0):
        for line in stdout.readlines():
            print(line)
        for line in stderr.readlines():
            print(line)
        raise Exception(client.get_transport().sock.getpeername()[0] + " execute '" + cmd + "' failed. " )
    return stdin,stdout,stderr

def exec_cmd_no_check(client,username,cmd):
    if (username == "root"):
        stdin,stdout,stderr=client.exec_command(cmd)
    else:
        stdin,stdout,stderr=client.exec_command("sudo " + cmd)
    #wait for the cmd to finish
    return stdin,stdout,stderr

