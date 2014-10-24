# -*- coding: utf-8 -*-

#############################
#name:updateHosts
#author:https://github.com/ladder1984
#python version:2.7.8
#version:0.0.5
############################


from urllib import urlretrieve
from datetime import *
import re
import os
import shutil

#setting
hostsSource = "https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hosts_folder = "C:\Windows\System32\drivers\etc\\"
hostsLocation = "C:\Windows\System32\drivers\etc\hosts"
noAdBlock = 1
#seting

errorLog = open('errorLog.txt', 'a')


def backup_hosts():
    if not os.path.isfile(hosts_folder+'backup_hosts_original_by_updateHosts'):
        shutil.copy(hosts_folder+'hosts', hosts_folder+'backup_hosts_original_by_updateHosts')
    shutil.copy(hosts_folder+'hosts', hosts_folder+'backup_hosts_last_by_updateHosts')


def download_hosts():
    try:
        urlretrieve(hostsSource, "hosts")
    except IOError, e:
        errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')


def del_adblock():
    file_to_open = open('hosts', 'r')
    hosts_content = file_to_open.read()
    hosts_content = re.sub('#AdBlock START([\s\S]*)#AdBlock END', "#", hosts_content)
    file_to_open.close()

    file_to_open = open('hosts', 'w')
    file_to_open.write(hosts_content)
    file_to_open.close()


def move_hosts():
    try:
        shutil.move("hosts", hostsLocation)
    except IOError, e:
        errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')

errorLog.close()

#main
backup_hosts()
download_hosts()
if noAdBlock == 1:
    del_adblock()
move_hosts()