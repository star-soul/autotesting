import os,sys
import requests
import json
sys.path.append("/autotesting")
import src.Server.method.interfaceMethod as IM
import src.Server.Logs.logs as log
logger = log.logger

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:用于server端接口传递用例相关数据
"""

#读取测试用例模块
def interfaceRequestReadInfo(acceptInfo):
    while True:
        accept = json.loads(acceptInfo)
        res = IM.read_Case_Request(C_ProjectName=accept["C_ProjectName"], get_one=accept["get_one"],
                              C_CaseName=accept[ "C_CaseName"])
        if res:
            result = res
            return result
        else:
            result = res
            return result



#写入测试用例模块
def interfaceRequestWriteInfo(acceptInfo):
    while True:
        accept = json.loads(acceptInfo)
        res = IM.write_Case(C_ProjectName=accept["C_ProjectName"],C_CaseName=accept["C_CaseName"],C_Url=accept["C_Url"],C_Class=accept["C_Class"],
                            C_Api=accept["C_Api"],C_Body=accept["C_Body"],C_Expectation=accept["C_Expectation"],C_Comment=accept["C_Comment"])
        if res:
            result = res
            return result
        else:
            result = res
            return result