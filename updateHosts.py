# -*- coding: utf-8 -*-

#############################
#author:https://github.com/ladder1984
#version:0.0.1
#python version:2.7.8
############################


from urllib import urlretrieve
import shutil
url="https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hostsLocation="C:\Windows\System32\drivers\etc\hosts"
urlretrieve(url,"hosts")
shutil.move("hosts",hostsLocation);