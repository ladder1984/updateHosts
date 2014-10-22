# -*- coding: utf-8 -*-

#############################
#name:updateHosts
#author:https://github.com/ladder1984
#version:0.0.2
#python version:2.7.8
############################


from urllib import urlretrieve
import shutil

hostsSource="https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hostsLocation="C:\Windows\System32\drivers\etc\hosts"
urlretrieve(hostsSource,"hosts")
shutil.move("hosts",hostsLocation)