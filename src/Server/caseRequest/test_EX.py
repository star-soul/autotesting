import os,sys
import requests
import json
sys.path.append("/autotesting")
import src.Server.method.interfaceMethod as IM

file = json.dumps({"C_ProjectName":"hr1", "C_Id":"19",'tokens': None})
TK = 'tokens'

class testFile():
    #读取一条指定测试用例模块
    def interfaceRequestReadInfoOnly(self,acceptInfo):
        while True:
            print(json.loads(acceptInfo))
            self.accept = json.loads(acceptInfo)
            print(self.accept["C_ProjectName"])
            print(self.accept["C_Id"])
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
        while True:
            self.interfaceRequestReadInfoOnly(acceptInfo)
            # 判断是否有数据
            if self.result['result'] == False :
                return {"result": False, "message": "数据获取错误"}
            elif self.result['message'] == None or self.result['message'] == [] or self.result['message'] == "":
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
                    IM.case_Return_Val(C_MapId=str(val['C_Id']), C_ResCaseName=val['C_CaseName'],
                                       C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": json.dumps(self.only_Res.text)["result"]["accessToken"]}
                elif res[4] == 'post':
                    self.only_Res = requests.post(url=val['C_Url'] + val['C_Api'], data=val['C_Body'], headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']), C_ResCaseName=val['C_CaseName'],
                                       C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": str(self.only_Res.text)}
                elif res[4] == 'delete':
                    self.only_Res = requests.delete(url=val['C_Url'] + val['C_Api'], data=val['C_Body'],
                                                    headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']), C_ResCaseName=val['C_CaseName'],
                                       C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": json.dumps(self.only_Res.text)}
                elif res[4] == 'put':
                    self.only_Res = requests.put(url=val['C_Url'] + val['C_Api'], data=val['C_Body'], headers=headers)
                    IM.case_Return_Val(C_MapId=str(val['C_Id']), C_ResCaseName=val['C_CaseName'],
                                       C_ResProjectName=val['C_ProjectName'],
                                       C_CaseResult=json.dumps(self.only_Res.text))
                    return {"result": True, "message": json.dumps(self.only_Res.text)}
                else:
                    return {"result": False, "message": "数据写入错误"}

    #判断用例结果是否通过
    def date_comtrast(self,acceptInfo):
        # self.interfaceRequestReadInfoOnly(acceptInfo)
        self.test_Execute_Request(acceptInfo)
        res = self.result['message']
        # 获取预期结果
        val = {
            'C_Id': res[0],
            'C_ProjectName': res[1],
            'C_CaseName': res[2],
            'C_Expectation': res[7],
        }
        # if self.only_Res.text == None or self.only_Res.text == []:
        #     return {"result": False, "message": "数据获取错误"}

        try:
            self.res = self.only_Res.text
            if json.loads(self.res)["statusCode"] == int(val["C_Expectation"]):
                IM.updata_Case_Return_Val(C_Id=val['C_Id'],
                                          C_ProjectName=val['C_ProjectName'],
                                          C_Practical=True)
                print(self.res)
                find_res = {
                        '用例ID': self.res[1][0],
                        '项目名称': self.res[1][1],
                        '用例标题': self.res[1][2],
                        '请求地址': self.res[1][3],
                        '请求类型': self.res[1][4],
                        '请求接口': self.res[1][5],
                        '请求体': self.res[1][6],
                        '期望值': self.res[1][7],
                        '是否通过': self.res[1][8],
                        'C_Comment': self.res[1][9],
                    }
                print("查询成功1",find_res)

                return {"result": True, "message": "测试用例执行《通过》 *★,°*:.☆(￣▽￣)/$:*.°★* 。"}
            else:

                return {"result": False, "message": "测试用例执行《未通过》 ≧ ﹏ ≦ "}
        except AttributeError as e:
            print(e)
            return {"result": False, "message": "填写信息错误"}


if __name__=='__main__':
    # testFile().interfaceRequestReadInfoOnly(file)
    # testFile().test_Execute_Request(file)
    testFile().date_comtrast(file)