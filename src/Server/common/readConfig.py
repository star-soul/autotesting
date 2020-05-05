import configparser
import os,sys
sys.path.append("/autotesting")

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:读取配置文件
"""

#读取配置文件
config = configparser.ConfigParser()
config.read('/autotesting/src/Server/common/config.conf')

#信息
myUser = config.get("mysql", "user")
myPwd = config.get("mysql", "Passwd")
myIp = config.get("mysql", "Ip")
myPort = int(config.get("mysql", "Port"))
myDb = config.get("mysql", "Db")
myAuth_plugin = config.get("mysql", "Auth_plugin")

cli_Host = config.get("socket", "S_Ip")
cli_Port = int(config.get("socket", "S_Port"))