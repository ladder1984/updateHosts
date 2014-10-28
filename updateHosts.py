# -*- coding: utf-8 -*-

#############################
#name:updateHosts
#author:https://github.com/ladder1984
#python version:2.7.8
#version:1.1.2
############################


from urllib import urlretrieve
from datetime import *
import re
import os
import shutil
import ConfigParser

#default setting
hosts_source = "https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hosts_folder = os.environ['SYSTEMROOT']+"\\System32\drivers\etc\\"
hosts_location = hosts_folder + "hosts"
noAdBlock = 1
#default setting

errorLog = open('errorLog.txt', 'a')


def get_config():
    global hosts_source
    global noAdBlock
    if os.path.exists('config.ini'):
        #清除Windows记事本自动添加的BOM
        content = open('config.ini').read()
        content = re.sub(r"\xfe\xff", "", content)
        content = re.sub(r"\xff\xfe", "", content)
        content = re.sub(r"\xef\xbb\xbf", "", content)
        open('config.ini', 'w').write(content)

        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        source_id = config.get('source_select', 'source_id')
        hosts_source = config.get('source_select', 'source'+source_id)
        #noAdBlock = config.getint('other', 'noadblock')


def backup_hosts():
    if (not os.path.isfile(hosts_folder + 'backup_hosts_original_by_updateHosts')) and \
            os.path.isfile(hosts_folder + 'hosts'):
        shutil.copy(hosts_folder+'hosts', hosts_folder+'backup_hosts_original_by_updateHosts')
    if os.path.isfile(hosts_folder + 'hosts'):
        shutil.copy(hosts_folder+'hosts', hosts_folder+'backup_hosts_last_by_updateHosts')


def download_hosts():
    try:
        urlretrieve(hosts_source, "hosts_from_web")
    except IOError, e:
        errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')

def process_hosts():
    hosts_content = open('hosts','w')
    file_from_web = open('hosts_from_web')
    hosts_from_web = file_from_web.read()
    file_user_defined=open('hosts_user_defined.txt')
    hosts_user_defined=file_user_defined.read()
    hosts_content.write('#hosts_user_defined\n')
    hosts_content.write(hosts_user_defined)
    hosts_content.write('\n#hosts_user_defined\n')
    hosts_content.write('\n\n#hosts_by_hostsUpdate\n\n')
    hosts_content.write(hosts_from_web)
    hosts_content.write('\n#hosts_by_hostsUpdate')
    hosts_content.close()
    file_from_web.close()
    file_user_defined.close()
    os.remove('hosts_from_web')

# def del_adblock():
#     if noAdBlock == 1:
#         file_to_open = open('hosts', 'r')
#         hosts_content = file_to_open.read()
#         hosts_content = re.sub('#AdBlock START([\s\S]*)#AdBlock END', "#", hosts_content)
#         file_to_open.close()
#
#         file_to_open = open('hosts', 'w')
#         file_to_open.write(hosts_content)
#         file_to_open.close()


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
    process_hosts()
#    del_adblock()
    move_hosts()

if __name__ == '__main__':
    main()