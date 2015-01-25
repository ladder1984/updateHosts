updateHosts
============

## 简介
自动从网络下载hosts文件，hosts源由用户设置。

## 使用说明
下载地址：<https://github.com/ladder1984/updateHosts/archive/master.zip>

解压即可使用，无需安装Python。点击start.vbs运行，点击addToStartup.js加入启动项（Windows有效）。

**config.ini：** 设置参数，包括选择更新源、是否关闭hosts中的网站过滤。详见config.ini中的注释

**hosts_user_defined.txt：** 可填入自定义hosts内容

**注意：**

- 本软件不提供hosts文件，而是从从用户定义的地址下载hosts，默认提供几个流行的hosts，参见config.ini
- 建议使用前手动备份hosts文件
- 可能需要授予程序管理员权限：右击python27.exe，选中“属性”，在“兼容性”里勾选“以管理员身份运行此程序”。
- 建议使用notepad++编辑文件
- 删除启动：删除“启动”文件夹内的快捷方式，“启动”文件夹在开始菜单内


## 运行环境
- 操作系统：Windows、Linux、Mac OS


## 功能描述
- 下载hosts文件并更新本地hosts
- 用户可自定义hosts内容
- 可选的hosts更新源
- 可以选择下载多个hosts文件并合并
- 备份hosts文件
- 可去除屏蔽广告部分
- 分离出单独的配置文件
- 运行时不显示窗口
- 打包成exe文件，无需安装python即可使用
- 可单文件执行updateHosts
- 可添加启动项
- 生成错误日志errorLog.txt
- 待添加


## hosts源
hosts源来源于网络，收录入[someHosts](https://github.com/ladder1984/someHosts)项目，并选取如下hosts：

- simpleu-hosts <https://github.com/vokins/simpleu>
- google-hosts <https://github.com/txthinking/google-hosts>
- GavinHosts <http://blog.crpuer.com/GavinHosts.txt>
- General Hosts (ghosts) <http://h.heartnn.eu.org/hosts>
- imouto.host <https://github.com/zxdrive/imouto.host>

用户可在config.ini中选择，或者自定义hosts源。


## 其他
- updateHosts项目地址：<https://github.com/ladder1984/updateHosts>
- ChangeLog：<https://github.com/ladder1984/updateHosts/blob/master/ChangeLog.txt>
- 作者：<https://github.com/ladder1984> 博客：<http://www.itoldme.net>
- 欢迎反馈问题和建议，地址：<https://github.com/ladder1984/updateHosts/issues>

## 版权声明
- 本软件使用MIT协议
