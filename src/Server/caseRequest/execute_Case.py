import os,sys
import time
import requests
import json
sys.path.append("/autotesting")
import src.Server.Logs.logs as log
# import src.Server.common.HTMLTestRunner as HTMLTestRunner
import src.Server.method.interfaceMethod as IM
# import src.Server.caseRequest.contrast_Case as r
logger = log.logger

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/4
    @UpdateTime: 2020/5/5
    @model:单条测试model
"""


class testFile():
    #读取一条指定测试用例模块
    def interfaceRequestReadInfoOnly(self,acceptInfo):
        while True:
            self.accept = json.loads(acceptInfo)
            self.res = IM.case_Request_One(C_ProjectName=self.accept["C_ProjectName"],  C_Id=self.accept["C_Id"])
            print(self.res)
            if self.res:
                self.result = self.res
                return self.result
            else:
                self.result = self.res
                return self.result




    #执行测试用例
    def test_Execute_Request(self, acceptInfo):
        # while True:
        self.interfaceRequestReadInfoOnly(acceptInfo)
        # 判断是否有数据
        try:
            if  self.result['message'] == None or self.result['message'] == []:
                return {"result": False, "message": "数据获取错误"}
            else:
                res = self.result['message']
                val = {
                    'C_Id': res[0],
                    'C_ProjectName': res[1],
                    'C_CaseName': res[2],
                    'C_Url': res[3],
                    'C_Class': res[4],
                    'C_Api': res[5],
                    'C_Body': res[6],
                    'C_Expectation': res[7],
                }
                #判断是否需要token
                if self.accept["tokens"] == "":
                    headers = {'Content-Type': 'application/json'}
                else:
                    headers = {
                        'Content-Type': 'application/json',
                        'token': self.accept["tokens"],
                    }

                # 根据接口类型判断并执行请求
                if res[4] == 'get':
                    self.only_Res = requests.get(url=val['C_Url'] + val['C_Api'], headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']),C_ResCaseName=val['C_CaseName'],C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": json.dumps(self.only_Res.text)["result"]["accessToken"]}
                elif res[4] == 'post':
                    self.only_Res = requests.post(url=val['C_Url'] + val['C_Api'], data=val['C_Body'], headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']), C_ResCaseName=val['C_CaseName'],C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))

                    return {"result": True, "message": str(self.only_Res.text)}
                elif res[4] == 'delete':
                    self.only_Res = requests.delete(url=val['C_Url'] + val['C_Api'], data=val['C_Body'], headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']),C_ResCaseName=val['C_CaseName'],C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": json.dumps(self.only_Res.text)}
                elif res[4] == 'put':
                    self.only_Res = requests.put(url=val['C_Url'] + val['C_Api'], data=val['C_Body'], headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']),C_ResCaseName=val['C_CaseName'],C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": json.dumps(self.only_Res.text)}
                else:
                    return {"result": False, "message": "数据写入错误"}
        except AttributeError as e:
            logger.error("eC数据写入错误%s" % e)
            return {"result": False, "message": "必填项写入错误"}

    #判断用例结果是否通过
    def date_comtrast(self,acceptInfo):
        self.test_Execute_Request(acceptInfo)
        res = self.result['message']
        # 获取预期结果
        val = {
            'C_Id': res[0],
            'C_ProjectName': res[1],
            'C_CaseName': res[2],
            'C_Expectation': res[7],
        }


        try:
            self.res = self.only_Res.text
            if json.loads(self.res)["statusCode"] == int(val["C_Expectation"]):
                IM.updata_Case_Return_Val(C_Id=val['C_Id'],
                                          C_ProjectName=val['C_ProjectName'],
                                          C_Practical=True)
                return {"result": True, "message": "测试用例执行《通过》 *★,°*:.☆(￣▽￣)/$:*.°★* 。\n执行结果：%s" % self.res}
            else:

                return {"result": False, "message": "测试用例执行《未通过》 ≧ ﹏ ≦ "}
        except AttributeError as e:
            logger.error("eC填写信息错误%s"%e)
            return {"result": False, "message": "填写信息错误"}


