import os,sys
sys.path.append("/autotesting")
import src.Server.sqlFile.S_ConnectSql as CURD
import src.Server.Logs.logs as log
logger = log.logger

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:用于登录和注册的校验
"""

#客户端登录
def Login_info(phoneNum,passWd):
    # 表名
    table = "LoginInfo"
    # 查询字段
    field = "D_Passwd,D_Phone,D_Name"
    # 键
    asslgn = "D_Phone={phoneNum}".format(phoneNum=phoneNum)
    val = CURD.Database().query_Sql(table=table,field=field,get_one=False,asslgn=asslgn)

    try:
        if len(passWd) < 5 or len(passWd) > 20:
            return {"result":False,"message":"请检查密码长度..."}

        elif passWd == val[1][0][0]:
            return {"result":True,"message":"登录成功..."}

    except (TypeError,IndexError) as e:
        logger.error("输入的账号/密码有误...%s"%e)
        return {"result":False,"message":"输入的账号/密码有误..."}

    else:
        return {"result":False,"message":"输入的账号/密码有误..."}




#客户端注册
def Register_Info(reuserName,rephoneNum,repassWd):
    #表名
    table = "LoginInfo"
    #查询字段
    val = {
        'D_Name': reuserName,
        'D_Phone': rephoneNum,
        'D_Passwd': repassWd,
    }
    #键
    field = "D_Phone"
    asslgn = "D_Phone={phoneNum}".format(phoneNum=rephoneNum)
    find_val = CURD.Database().query_Sql(table=table, field=field, get_one=False, asslgn=asslgn)

    try:
        if len(rephoneNum) != 11:
            return {"result":False,"message":"手机号格式不正确..."}

        elif rephoneNum == find_val[1][0][0]:
            return {"result":False,"message":"该手机号已注册..."}

        elif len(repassWd) < 5 or len(repassWd) > 20:
            return {"result":False,"message":"密码长度不符合要求，请输入6-20个字符..."}

    except (TypeError) as e:
        logger.error("其他错误 %s" % e)
        return {"result":True,"message":"其他错误..."}

    except IndexError as e:
        CURD.Database().Insert_Sql(table=table, val_obj=val)
        logger.error("插入数据校验时，查询错误list=NULL，忽略",e)
        return {"result":True,"message":"注册成功，请登录系统"}




