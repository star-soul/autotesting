import unittest
import os,sys
import json
sys.path.append("/autotesting")
import src.Server.sqlFile.S_ConnectSql as ConnSql
import src.Server.sqlFile.S_ConnectSql as CURD
import src.Server.method.interfaceMethod as IR


# # @ConnSql.Database.Insert_Sql
# def test_insert():
#     table = "TestCase"
#     test = "test"
#     val = {
#         'C_Name' : test,
#         'C_Url' : 'www.baidu.com',
#         'C_Class' : 'get',
#         'C_Api' : '/abcd',
#     }
#
#     A = ConnSql.Database().Insert_Sql(table,val)
#     print(A)
# def test_insert2():
#     table = "TestCase"
#     test = "test"
#     val = {
#         'C_Name' : test,
#         'C_Url' : 'www.baidu.com',
#         'C_Class' : 'get',
#         'C_Api' : '/abcd',
#     }
#
#     A = ConnSql.Database().Insert_Sql(table,val)
#     print(A)
# def test_query():
#     table = "TestCase"
#     field = "*"
#     # asslgn = "C_Id = 2"
#     # T=False
#     # co = ConnSql.Database().connectDataTable()
#     # print(co)
#     A = ConnSql.Database().query_Sql(table=table,field=field)
#     print(A)
#
# def test_update():
#     table = "TestCase"
#     field = "C_Api = '/qwer', C_Class = 'update'"
#     asslgn = "C_Id = 2"
#     T=True
#     # co = ConnSql.Database().connectDataTable()
#     # print(co)
#     A = ConnSql.Database().update_Sql(table=table,field=field,asslgn=asslgn)
#     print(A)
#
#
# def test_interfaceRequest():
#     a = IR.case_Request(C_ProjectName="HR",C_CaseName="test",get_one=True)
#     print(a)
#     C_ProjectName = input("项目名称")
#     C_CaseName = input("用例名称")
#     C_Url = input("地址名称")
#     C_Api = input("API")
#
#     IR.write_Case(C_ProjectName=C_ProjectName,C_CaseName=C_CaseName,C_Url=C_Url,C_Class='post',
#                   C_Api=C_Api,C_Body='{"a":"asd"}',C_Expectation='1',C_Practical='1',C_Comment="")

def Case_Return_Val(C_ResCaseName,C_MapId,C_ResProjectName,C_CaseResult):
    # 表名
    table = "TestCaseResult"
    # while True:
    # try:

    # if C_ResCaseName == "" or C_ResCaseName == []:
    #     return {"result": False, "message": "必填字段不得为空,请重新填写"}
    # if C_MapId == "" or C_MapId == []:
    #     return {"result": False, "message": "必填字段不得为空,请重新填写"}
    # if C_ResProjectName == "" or C_ResProjectName == []:
    #     return {"result": False, "message": "必填字段不得为空,请重新填写"}
    # if C_CaseResult == "" or C_CaseResult == []:
    #     return {"result": False, "message": "必填字段不得为空,请重新填写"}

    # 写入字段
    val = {
        'C_ResCaseName': C_ResCaseName,
        'C_MapId': C_MapId,
        'C_ResProjectName': C_ResProjectName,
        'C_CaseResult': C_CaseResult,
    }

    A = CURD.Database().Insert_Sql(table=table, val_obj=val)
    print(A)
    # return {"result": True, "message": "写入成功"}
    # except:
    #     print("写入失败A",A)
        # return {"result": False, "message": "写入失败..."}

if __name__=='__main__':
    # test_insert()
    # test_query()
    # test_update()
    # test_query()
    # test_interfaceRequest()
    Case_Return_Val(C_ResCaseName="pp", C_MapId="1", C_ResProjectName="poi",
                    C_CaseResult=json.dumps({'result': True, 'message': '{"result":{"accessToken":"kZQtplF5nYKBQBErkAOdxLb4MOOzum0iD0guYcHEztzbyIpqzFwDtCzbwDv9xAEzG8LDpJD1/tStzlwUTApWCXXNitng3gI07FOB5PjgZFM617BQTgi4d8ApaxQSiw1DsoloSOUxMNK0TzuqCvfjTaMuMZiot4i50H2ykPFMLu2ij6k8mYNP7NPK3RTAgqC22kFA9B/INzW14psRdw15++LLUJrnH+ifW7toYzhUtSi/xu5zDTNyeATEzJ/9bNYzZmX3Kt5MXvHQYT0YZTznu6CIlRAFrtsuWEZ0B87cWtzdpFfvv+RZ/o2DEtisNli4wQ8D3LpiHCVII6lGvEQ2lg=="},"statusCode":1000,"message":"OK"}'}))


