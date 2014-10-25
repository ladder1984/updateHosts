updateHosts
============

##简介
自动更新hosts文件

##使用方法
下载地址：https://github.com/ladder1984/updateHosts/archive/master.zip

解压即可使用，无需安装Python。点击start.vbs运行，点击addToStartup.js加入启动项。

**注意：**可能需要授予程序管理员权限：右击python27.exe，选中“属性”，在“兼容性”里勾选“以管理员身份运行此程序”。

##运行环境
- 操作系统：Windows

##功能描述
- **（已完成）**下载hosts文件并更新本地hosts
- **（已完成）**可单文件执行updateHosts
- **（已完成）**可添加启动项
- **（已完成）**生成错误日志errorLog.txt
- **（已完成）**可去除AdBlock部分，默认启用
- **（已完成）**备份hosts文件
- **（已完成）**分离出单独的配置文件
- **（已完成）**可选的hosts更新源
- **（已完成）**运行时不显示窗口
- **（已完成）**打包成exe文件，无需安装python即可使用
- 待添加


##hosts源
hosts源来源于网络，用户可选或者自定义。目前收录了：
- smarthosts <https://code.google.com/p/smarthosts/>
- imouto.host <https://github.com/zxdrive/imouto.host>
- google-hosts <https://github.com/txthinking/google-hosts>

用户可在config.ini中选择


##其他
- updateHosts项目地址：<https://github.com/ladder1984/updateHosts>
- ChangeLog：<https://github.com/ladder1984/updateHosts/blob/master/ChangeLog.txt>
- 基于Python2.7.8开发，代码风格遵循[Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html "Google Python Style Guide")
- 版本号命名遵循[语义化版本控制规范（SemVer）](http://semver.org/lang/zh-CN/ "语义化版本控制规范（SemVer）")

##版权声明
- 本软件使用[MIT](https://github.com/ladder1984/updateHosts/blob/master/LICENSE)协议
- hosts源版权归原版权方所有
- Python运行环境取自[Goagent](https://github.com/goagent/goagent)，版权归原版权方所有
