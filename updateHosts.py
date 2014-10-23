# -*- coding: utf-8 -*-

#############################
#name:updateHosts
#author:https://github.com/ladder1984
#python version:2.7.8
#version:0.0.4
############################


from urllib import urlretrieve
import shutil
from datetime import *
import re

#setting
hostsSource = "https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hostsLocation = "C:\Windows\System32\drivers\etc\hosts"
noAdBlock = 1
#seting
errorLog = open('errorLog.txt', 'a')


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

download_hosts()
if noAdBlock == 1:
    del_adblock()
move_hosts()