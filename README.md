updateHosts
============

## 简介
自动从网络下载hosts文件，hosts源由用户设置。
### hosts是什么？
>hosts文件是一个用于储存计算机网络中各节点信息的计算机文件。这个文件负责将主机名映射到相应的IP地址。hosts文件通常用于补充或取代网络中DNS的功能。和DNS不同的是，计算机的用户可以直接对hosts文件进行控制。 ——[hosts文件 - 维基百科，自由的百科全书](http://zh.wikipedia.org/zh-cn/Hosts%E6%96%87%E4%BB%B6 "hosts文件 - 维基百科，自由的百科全书")

### updateHosts是什么？
updateHosts可以自动从网络下载最新的hosts文件，并自动替换本机的hosts文件。请注意，updateHosts本身 **不** 生成hosts，hosts的来源由用户指定，或者你可可以使用默认推荐的源。更多更能请见下文描述。

### hosts的功能
> hosts文件也可以用于其它情况，例如可以将已知的广告服务器重定向到无广告的机器（通常是本地的IP地址：127.0.0.1）上来过滤广告。同时也可以通过不下载网络广告，从而减少带宽。使用hosts文件还可以减少对DNS服务器的访问来加快访问速度并减少带宽消耗。
> 
> hosts文件的另一个重要用途就是用于拦截一些恶意网站的请求，从而防止访问欺诈网站或感染一些病毒或恶意软件。但同时，这个文件也可能被病毒或恶意软件所利用来阻止用户更新杀毒软件或访问特定网站。
> 
> 在中国大陆，由于防火长城的DNS劫持，有一些网民也借使用hosts文件来强制将特定网站指定到未封锁的IP上。例如网络上有很多教授修改hosts文件来访问Google搜索的教程。比如就有维基媒体基金会的图片服务器IP地址被ISP封锁，通过修改hosts文件以正常显示图片的方法流传。  ——[hosts文件 - 维基百科，自由的百科全书](http://zh.wikipedia.org/zh-cn/Hosts%E6%96%87%E4%BB%B6 "hosts文件 - 维基百科，自由的百科全书")




## 使用说明
下载地址：<https://github.com/ladder1984/updateHosts/archive/master.zip> 解压即可使用。

### 运行方法

- **Windows用户**：点击**start.vbs**运行，点击**addToStartup.js**加入启动项。无须安装Python。
- **Linux/Mac OS用户**：如未安装Python，请自行安装Python 2.x。点击**updateHosts.py**执行程序。

### 文件说明

- **config.ini：** 设置参数，包括选择更新源、开启关闭功能。详见config.ini中的注释 
- **hosts_user_defined.txt：** 可填入自定义hosts内容

### 设置说明
目前可以在config.ini文件中方设置功能。0为不开启，1为开启此功能。目前可设置的功能有：

- not_block_sites 开启后，将注释掉通过127.0.0.1屏蔽的网址
- always_on 开启后，将常驻内存，每小时执行一次更新
 
### 注意事项：

- 如果不确定是否更新成功，可查看hosts文件，Windows系统通常在C:\Windows\System32\drivers\etc下的hosts文件。
- 本软件不提供hosts文件，而是从从用户定义的地址下载hosts，默认提供几个流行的hosts，参见config.ini
- 建议使用前手动备份hosts文件
- Windows用户可能需要授予程序管理员权限：右击python27.exe，选中“属性”，在“兼容性”里勾选“以管理员身份运行此程序”。
- 建议使用Notepad++、Sublime Text编辑文件
- 删除启动项（Windows用户）：删除“启动”文件夹内的快捷方式，“启动”文件夹在开始菜单内


## 运行环境
- 操作系统：Windows、Linux、Mac OS


## 功能描述
- 下载hosts文件并更新本地hosts
- 用户可自定义hosts内容
- 可选的hosts更新源
- 可以选择下载多个hosts文件并合并
- 备份hosts文件
- 可去除屏蔽广告部分
- 可常驻后台，可每小时执行一次
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
