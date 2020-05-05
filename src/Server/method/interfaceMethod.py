import os,sys
sys.path.append("/autotesting")
import src.Server.sqlFile.S_ConnectSql as CURD
import src.Server.Logs.logs as log
logger = log.logger


"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:用于server端操作数据库的用例数据
"""

#查询测试用例，get_one=False 执行一条，True执行多条
def read_Case_Request(C_ProjectName,get_one,C_CaseName = None):
    try:
        # 表名
        table = "TestCase"
        # 查询字段
        field = "C_Id,C_ProjectName,C_CaseName,C_Url,C_Class,C_Api,C_Body,C_Expectation,C_Practical,C_Comment"
        asslgn1 = "C_ProjectName='{C_ProjectName}'".format(C_ProjectName=C_ProjectName)

        #执行单条或多条数据进行查看
        find_val = CURD.Database().query_Sql(table=table, field=field, asslgn=asslgn1, get_one=get_one)
        if C_CaseName:
            asslgn2 = "C_ProjectName='{C_ProjectName}' and C_CaseName='{C_CaseName}'".format(
                C_ProjectName=C_ProjectName, C_CaseName=C_CaseName)
            find_val = CURD.Database().query_Sql(table=table, field=field, get_one=get_one, asslgn=asslgn2)
        if find_val[1] == [] or find_val[1] == "" or find_val[1] == None:
            return {"result": False, "message": "查询失败..."}

        return {"result": True, "message": find_val[1]}
    except:
        print("查询失败")
        return {"result": False, "message": "查询失败..."}

#配合requests请求执行一条指定用例
def case_Request_One(C_ProjectName,C_Id):
    try:
        if C_ProjectName == "" or C_ProjectName == [] :
            return {"result": False, "message": "项目名称必填字段不得为空,请重新填写"}
        if C_Id == "" or C_Id == [] :
            return {"result": False, "message": "用例ID必填字段不得为空,请重新填写"}
        # 表名
        table = "TestCase"
        # 查询字段
        field = "C_Id,C_ProjectName,C_CaseName,C_Url,C_Class,C_Api,C_Body,C_Expectation,C_Practical,C_Comment"
        # 值
        asslgn = "C_ProjectName='{C_ProjectName}' and C_Id='{C_Id}'".format(C_ProjectName=C_ProjectName, C_Id=C_Id)
        #执行单条
        find_val = CURD.Database().query_Sql(table=table, field=field, get_one=True, asslgn=asslgn)

        if find_val[1] == [] or find_val[1] == "" or find_val[1] == None:
            return {"result": False, "message": "查询失败..."}
        else:
            return {"result": True, "message": find_val[1]}


    except:
        print("查询失败")
        return {"result": False, "message": "查询失败..."}

#写入接口返回的实际结果
def case_Return_Val(C_ResCaseName,C_MapId,C_ResProjectName,C_CaseResult):
    # 表名
    table = "TestCaseResult"
    while True:
        try:

            if C_ResCaseName == "" or C_ResCaseName == []:
                return {"result": False, "message": "C_ResCaseName写入错误"}
            if C_MapId == "" or C_MapId == []:
                return {"result": False, "message": "C_MapId写入错误"}
            if C_ResProjectName == "" or C_ResProjectName == []:
                return {"result": False, "message": "C_ResProjectName写入错误"}
            if C_CaseResult == "" or C_CaseResult == []:
                return {"result": False, "message": "C_CaseResult写入错误"}

            # 写入字段
            val = {
                'C_ResCaseName': C_ResCaseName,
                'C_MapId': C_MapId,
                'C_ResProjectName': C_ResProjectName,
                'C_CaseResult': C_CaseResult,
            }

            CURD.Database().Insert_Sql(table=table, val_obj=val)
            print("写入成功")
            return {"result": True, "message": "写入成功"}
        except:
            print("写入失败")
            return {"result": False, "message": "写入失败..."}

#填写接口测试用例
def write_Case(C_ProjectName,C_CaseName,C_Url,C_Class,C_Api,C_Body,C_Expectation,C_Comment):
    # 表名
    table = "TestCase"
    while True:
        try:

            if C_ProjectName == "" or C_ProjectName == []:
                return {"result": False, "message": "测试项目名称必填字段不得为空,请重新填写"}
            elif C_CaseName == "" or C_CaseName == []:
                return {"result": False, "message": "用例名称必填字段不得为空,请重新填写"}
            elif C_Url == "" or C_Url == []:
                return {"result": False, "message": "请求地址必填字段不得为空,请重新填写"}
            elif C_Class == "" or C_Class == []:
                return {"result": False, "message": "请求类型必填字段不得为空,请重新填写"}
            elif C_Api == "" or C_Api == []:
                return {"result": False, "message": "请求接口必填字段不得为空,请重新填写"}

            # 写入字段
            val = {
                'C_ProjectName': C_ProjectName,
                'C_CaseName': C_CaseName,
                'C_Url': C_Url,
                'C_Class': C_Class.lower(),
                'C_Api': '/' + C_Api.strip('/'),
                'C_Body': C_Body,
                'C_Expectation': C_Expectation,
                'C_Comment': C_Comment,
            }

            CURD.Database().Insert_Sql(table=table, val_obj=val)
            print("写入成功")
            return {"result": True, "message": "写入成功"}
        except:
            print("写入失败")
            return {"result": False, "message": "写入失败..."}

# 更新用例结果
def updata_Case_Return_Val(C_Id,C_ProjectName,C_Practical,):
    # 表名
    table = "TestCase"
    while True:
        try:

            if C_Id == "" or C_Id == []:
                return {"result": False, "message": "用例ID写入错误"}
            elif C_ProjectName == "" or C_ProjectName == []:
                return {"result": False, "message": "测试项目名称写入错误"}
            elif C_Practical == "" or C_Practical == []:
                return {"result": False, "message": "实际结果写入错误"}

            # 写入字段
            field = "C_Practical='{C_Practical}' ".format(C_Practical=C_Practical)

            asslgn = "C_ProjectName='{C_ProjectName}' and C_Id='{C_Id}'".format(C_ProjectName=C_ProjectName, C_Id=C_Id)

            CURD.Database().update_Sql(table=table,field=field,asslgn=asslgn)
            print("写入成功")
            return {"result": True, "message": "写入成功"}
        except:
            print("写入失败")
            return {"result": False, "message": "写入失败..."}