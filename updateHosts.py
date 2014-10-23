# -*- coding: utf-8 -*-

#############################
#name:updateHosts
#author:https://github.com/ladder1984
#python version:2.7.8
#version:0.0.3
############################


from urllib import urlretrieve
import shutil
from  datetime  import  *

hostsSource="https://raw.githubusercontent.com/zxdrive/imouto.host/master/imouto.host.txt"
hostsLocation="C:\Windows\System32\drivers\etc\hosts"
errorLog=open('errorLog.txt','a')

try:
    urlretrieve(hostsSource,"hosts")
except IOError, e:
    errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')
try:
    shutil.move("hosts",hostsLocation)
except IOError, e:
    errorLog.write(str(datetime.now())+'\n'+str(e)+'\n\n')