import sys,os
import json
sys.path.append("/autotesting")
import src.Server.method.loginAndRegister as LRA


"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:用于server端传递登录相关数据
"""

#登录模块
def loginManage(acceptInfo):
    while True:
        accept = json.loads(acceptInfo)
        res = LRA.Login_info(phoneNum=accept["phoneNum"], passWd=accept["passWd"])
        if res:
            result = res
            return result
        else:
            result = res
            return result


#注册模块
def registerManage(acceptInfo):
    while True:
        accept = json.loads(acceptInfo)
        res = LRA.Register_Info(reuserName=accept["userName"],
                          rephoneNum=accept["phoneNum"],
                          repassWd=accept["passWd"])
        if res:
            result = res
            return result
        else:
            result = res
            return result