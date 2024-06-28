#!/usr/bin/python3
# encoding:utf-8
import sys
import subprocess
import datetime
import logging

phoneNumberList = 'xxxxxxx,xxxxxxx'
emailAddressList = 'xxxxxxx'

BASE_DIR = "/tmp"
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] [%(levelname)s] %(message)s',
                    # datefmt='%Y-%m-%d %H:%M:%S %p',
                    filename=BASE_DIR + '/keepalived_notify.log',
                    filemode='a')


def runcmd(cmd):
    result_msg = None
    result_status = False
    ret = None
    try:
        ret = subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True, timeout=5, check=False, encoding='utf-8')
        result_status = True
    except Exception as e:
        result_msg = e

    if result_status:
        result_msg = "%s %s" % (ret.stdout, ret.stderr)
        if ret.returncode == 0:
            result_status = True
            # print("success:",ret)
        else:
            result_status = False
            # print("error:",ret)
    return result_status, result_msg, ret


def sendSMS(phoneNumber, smsMsg):
    smsMsg = "[%s] %s" % (datetime.datetime.now(), smsMsg)
    smsCMD = "/bin/zbxcli sms -n %s -m '%s' 2>&1" % (phoneNumber, smsMsg)
    (smsResultStatus, smsResultMsg, smsRet) = runcmd(smsCMD)

    logging.info('SMS sended. exitCode: %s, stdout: %s, CMD:%s' % (
        smsResultStatus,
        smsResultMsg,
        smsCMD
    ))


# zbxcli mail -t 收件人 -s 主题 -m 内容
def sendEmail(emailAddress, subject, emailMsg):
    if not subject:
        subject = '【xxxxxxxDB短信告警】'

    emailMsg = "[%s] %s" % (datetime.datetime.now(), emailMsg)
    emailCMD = "/bin/zbxcli mail -t '%s' -s '%s' -m '%s' 2>&1" % (emailAddress, subject, emailMsg)
    (emailResultStatus, emailResultMsg, emailRet) = runcmd(emailCMD)

    logging.warn('Email sended. exitCode: %s, stdout: %s, CMD:%s' % (
        emailResultStatus,
        emailResultMsg,
        emailCMD
    ))


def showHelp():
    note = '''using python keepalived_notify.py [master | backup] ip vip
    '''
    print(note)
    exit(1)


if __name__ == "__main__":
    time_stamp = datetime.datetime.now()
    (result_status, result_msg, ret) = runcmd('hostname')

    if result_status:
        hostname = result_msg.split('\n')[0]
    else:
        logging.error('fetch hostname failed. %s' % result_msg)
        exit(1)

    if len(sys.argv) != 4:
        showHelp()
    elif sys.argv[1] == 'master':
        message_content = 'server: %s(%s) change to Master, VIP: %s' % (sys.argv[2], hostname, sys.argv[3])
        subject = '%s change to Master -- keepalived notify' % (sys.argv[2])
        sendEmail(emailAddressList, subject, message_content)
        sendSMS(phoneNumberList, message_content)
    elif sys.argv[1] == 'backup':
        message_content = 'server: %s(%s) change to Backup, VIP: %s' % (sys.argv[2], hostname, sys.argv[3])
        subject = '%s change to Backup -- keepalived notify' % (sys.argv[2])
        sendEmail(emailAddressList, subject, message_content)
        sendSMS(phoneNumberList, message_content)
    else:
        showHelp()