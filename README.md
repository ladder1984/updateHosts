updateHosts
============

##简介
自动从网络下载hosts文件，hosts源由用户设置

##使用说明
下载地址：https://github.com/ladder1984/updateHosts/archive/master.zip

解压即可使用，无需安装Python。点击start.vbs运行，点击addToStartup.js加入启动项。

**config.ini** 文件设置参数，包括选择更新源、是否关闭hosts中的网站过滤。详见config.ini中的注释


**hosts_user_defined.txt** 文件可填入自定义hosts内容

**注意：**

- 可能需要授予程序管理员权限：右击python27.exe，选中“属性”，在“兼容性”里勾选“以管理员身份运行此程序”。
- 建议使用notepad++编辑文件
- 删除启动：删除“启动”文件夹内的快捷方式，“启动”文件夹在开始菜单内


##运行环境
- 操作系统：Windows

##功能描述
- **（已完成）**下载hosts文件并更新本地hosts
- **（已完成）**可单文件执行updateHosts
- **（已完成）**可添加启动项
- **（已完成）**生成错误日志errorLog.txt
- **（已完成）**备份hosts文件
- **（已完成）**分离出单独的配置文件
- **（已完成）**可选的hosts更新源
- **（已完成）**运行时不显示窗口
- **（已完成）**打包成exe文件，无需安装python即可使用
- **（已去除）**可去除AdBlock部分
- **（已完成）** 用户可自定义hosts内容
- 待添加


##hosts源
hosts源来源于网络，收录入[someHosts](https://github.com/ladder1984/someHosts)项目，并选取如下hosts：

- smarthosts <https://code.google.com/p/smarthosts/>
- imouto.host <https://github.com/zxdrive/imouto.host>
- google-hosts <https://github.com/txthinking/google-hosts>
- simpleu-hosts <https://github.com/vokins/simpleu>

用户可在config.ini中选择，或者自定义hosts源


##其他
- updateHosts项目地址：<https://github.com/ladder1984/updateHosts>
- ChangeLog：<https://github.com/ladder1984/updateHosts/blob/master/ChangeLog.txt>
- 作者：<https://github.com/ladder1984> 博客：<http://www.itoldme.net>
- 欢迎反馈问题和建议，地址：<https://github.com/ladder1984/updateHosts/issues>

##版权声明
- 本软件使用MIT协议
