# -*- coding: utf-8 -*-

#############################
#name:updateHosts
#author:https://github.com/ladder1984
#python version:2.7.8
#version:0.1.2
############################


from urllib import urlretrieve
from datetime import *
import re
import os
import shutil
import ConfigParser

#default setting
hosts_source = "https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hosts_folder = "C:\Windows\System32\drivers\etc\\"
hosts_location = "C:\Windows\System32\drivers\etc\hosts"
noAdBlock = 1
#default setting

errorLog = open('errorLog.txt', 'a')


def get_config():
    global hosts_source
    global noAdBlock
    if os.path.exists('config.ini'):
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        source_id = config.get('source_select', 'source_id')
        hosts_source = config.get('source_select', 'source'+source_id)
        noAdBlock = config.getint('other', 'noadblock')


def backup_hosts():
    if not os.path.isfile(hosts_folder + 'backup_hosts_original_by_updateHosts'):
        if os.path.isfile(hosts_folder + 'hosts'):
            shutil.copy(hosts_folder+'hosts', hosts_folder+'backup_hosts_original_by_updateHosts')
    if os.path.isfile(hosts_folder + 'hosts'):
        shutil.copy(hosts_folder+'hosts', hosts_folder+'backup_hosts_last_by_updateHosts')


def download_hosts():
    try:
        urlretrieve(hosts_source, "hosts")
    except IOError, e:
        errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')


def del_adblock():
    if noAdBlock == 1:
        file_to_open = open('hosts', 'r')
        hosts_content = file_to_open.read()
        hosts_content = re.sub('#AdBlock START([\s\S]*)#AdBlock END', "#", hosts_content)
        file_to_open.close()

        file_to_open = open('hosts', 'w')
        file_to_open.write(hosts_content)
        file_to_open.close()


def move_hosts():
    try:
        shutil.move("hosts", hosts_location)
    except IOError, e:
        errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')

errorLog.close()


def main():
    get_config()
    backup_hosts()
    download_hosts()
    del_adblock()
    move_hosts()

if __name__ == '__main__':
    main()