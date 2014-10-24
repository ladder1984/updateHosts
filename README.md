updateHosts
============

##运行环境
- 操作系统：Windows
- Python版本：2.x

##功能描述
- **（已完成）**下载hosts文件并更新本地hosts
- **（已完成）**可单文件执行updateHosts
- **（已完成）**可添加启动项
- **（已完成）**生成错误日志errorLog.txt
- **（已完成）**可去除AdBlock部分，默认启用
- **（已完成）**备份hosts文件
- **（已完成）**分离出单独的配置文件
- **（已完成）**可选的hosts更新源
- （未完成）运行时不显示窗口
- （未完成）打包成exe文件，无需安装python即可使用（v1.0.0时添加）
- 待添加


##hosts源
hosts源来源于网络，用户可选或者自定义。目前收录了：
- smarthosts <https://code.google.com/p/smarthosts/>
- imouto.host <https://github.com/zxdrive/imouto.host>
- google-hosts <https://github.com/txthinking/google-hosts>

用户可在config中选择

##使用方法
下载**updateHosts.py**、**addToStarup.js**和**config**到本地，直接运行updateHosts.py更新hosts，点击addToStarup.js将py文件的快捷方式加入启动项。亦可直接把updateHosts.py放到启动文件夹。


##其他
- updateHosts项目地址：<https://github.com/ladder1984/updateHosts>
- ChangeLog：<https://github.com/ladder1984/updateHosts/blob/master/ChangeLog.txt>
- 代码风格遵循[Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html "Google Python Style Guide")
- 版本号命名遵循[语义化版本控制规范（SemVer）](http://semver.org/lang/zh-CN/ "语义化版本控制规范（SemVer）")

##许可协议
使用[MIT](https://github.com/ladder1984/updateHosts/blob/master/LICENSE)协议
