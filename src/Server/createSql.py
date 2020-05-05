import mysql.connector
import src.Server.common.readConfig as conf

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime: 2020/5/4
    @model:数据库相关建表
"""

def CreateDatabaseCase():

    myUser = conf.myUser
    myPwd = conf.myPwd
    myIp = conf.myIp
    myPort = conf.myPort
    myDb = conf.myDb
    myauth_plugin = conf.myAuth_plugin

    try:
        conn = mysql.connector.connect(
            host=myIp,
            user=myUser,
            passwd=myPwd,
            database=myDb,
            port=myPort,
            auth_plugin=myauth_plugin,
        )
        print(conn,"连接成功...")
        #建立游标指向
        cur = conn.cursor()

        sql = """create table TestCase(
        C_Id int not null auto_increment comment '用例ID',
        C_ProjectName varchar(30) not null comment '测试项目名称',
        C_CaseName varchar(30) not null comment '用例名称',
        C_Url varchar(200) not null comment '地址',
        C_Class varchar(10) not null comment '接口类型',
        C_Api varchar(150) not null comment '接口地址',
        C_Body varchar(500) null comment '参数结构体',
        C_Expectation varchar(200) null comment '预期结果',
        C_Practical varchar(200) null comment '实际结果',
        C_Comment varchar(200) null comment '备注',
        create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP comment '创建时间',
        update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP comment '更新时间',
        primary key(C_Id)
        )"""

        #执行建库
        cur.execute(sql)
        print("创建成功")
        #关闭数据库
        conn.close()

    except mysql.connector.Error as e:
        print("数据表已存在, %s" % e)

def CreateCaseResult():

    myUser = conf.myUser
    myPwd = conf.myPwd
    myIp = conf.myIp
    myPort = conf.myPort
    myDb = conf.myDb
    myauth_plugin = conf.myAuth_plugin

    try:
        conn = mysql.connector.connect(
            host=myIp,
            user=myUser,
            passwd=myPwd,
            database=myDb,
            port=myPort,
            auth_plugin=myauth_plugin,
        )
        print(conn,"连接成功...")
        #建立游标指向
        cur = conn.cursor()

        sql = """create table TestCaseResult(
        C_ResId int not null auto_increment comment '用例ID',
        C_MapId int(30)  null  comment '映射用例ID',
        C_ResProjectName varchar(30) null comment '测试项目名称',
        C_ResCaseName varchar(30) null comment '测试用例标题',
        C_CaseResult varchar(2000) null comment '测试用例标题',
        create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP comment '创建时间',
        update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP comment '更新时间',
        primary key(C_ResId)
        )"""

        #执行建库
        cur.execute(sql)
        print("创建成功")
        #关闭数据库
        conn.close()

    except mysql.connector.Error as e:
        print("数据表已存在, %s" % e)

def CreateDatabaseUser():

    myUser = conf.myUser
    myPwd = conf.myPwd
    myIp = conf.myIp
    myPort = conf.myPort
    myDb = conf.myDb
    myauth_plugin = conf.myAuth_plugin

    try:
        conn = mysql.connector.connect(
            host=myIp,
            user=myUser,
            passwd=myPwd,
            database=myDb,
            port=myPort,
            auth_plugin=myauth_plugin,
        )
        print(conn,"连接成功...")
        #建立游标指向
        cur = conn.cursor()

        sql = """create table LoginInfo(
        D_Id int not null auto_increment comment '用户ID',
        D_Name varchar(30) null comment '用户名',
        D_Passwd varchar(30) not null comment '用户密码',
        D_Phone int(15) not null comment '用户手机号码',
        create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP comment '创建时间',
        update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP comment '更新时间',
        primary key(D_Id)
        )"""

        #执行建库
        cur.execute(sql)
        print("创建成功")
        #关闭数据库
        conn.close()

    except mysql.connector.Error as e:
        print("数据表已存在, %s" % e)

if __name__ == '__main__':
    CreateDatabaseCase()
    CreateDatabaseUser()
    CreateCaseResult()