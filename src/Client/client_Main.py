import sys,os
import socket
import json
sys.path.append("/autotesting")

from src.Server.common import readConfig as conf
import src.Client.method.loginAndRegister as LAR


"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:client端主程序
"""
# @with_goto

#控制台
def client_main():
    #连接Server
    sk_client = socket.socket()
    sk_client.connect((Host, Port))
    #接收server发送的用户信息
    Server_msg = sk_client.recv(10240)


    try:
        #操控界面
        while True:
            print("                 Welcome!  tester")
            print("------------------1.登录----------------------")
            print("------------------2.注册----------------------")
            print("------------------3.修改密码-------------------")
            print("------------------输入Q退出--------------------")

            Key = input("请输入序号:\n")

            while True:
                if Key < "0" and Key > "3":
                    print()

                elif Key == "1":
                    RDS = {"id":Key}
                    #读取用户信息
                    LAR.Send_messege().personageInfo(sk_client=sk_client,data=RDS,Server_msg=Server_msg)
                    phoneNum = input("请输入手机号码:\n")
                    passWd = input("请输入密码:\n")
                    redius = {"phoneNum":phoneNum,"passWd":passWd}
                    #认证
                    dl_msg = LAR.Send_messege().reception_Send_messege(sk_client=sk_client,data=redius)

                    #认证成功跳转MenuUi
                    if json.loads(dl_msg)["result"] == True :

                        while True:
                            print("                      MenuUi")
                            print("                  01.执行性能测试 ")
                            print("                  02.执行接口测试用例 ")
                            print("                  03.查看结果 ")
                            print("                  04.进入聊天室 ")
                            print("                  05.进入游戏厅 ")
                            print("                  输入exit退出系统 ")
                            menu = input("请输入序号:\n")
                            while True:

                                if menu < "00" and menu > "06":
                                    print()
                                elif menu == "01":
                                    print("性能测试功能待定")
                                    break
                                elif menu == "02":
                                    print("                      TestMenuUi")
                                    print("                  001.查询接口测试用例             ")
                                    print("                  002.插入单条接口用例               ")
                                    print("                  003.执行批量接口测试                ")
                                    print("                  004.执行单条接口测试                ")
                                    # print("                  005.上传接口测试用例文件      ")
                                    # print("                  006.读取Swagger到数据库                ")
                                    # print("                  007.下载接口测试用例模板                ")
                                    print("                  输入exit退出系统                 ")

                                    caseButton = input("请输入序号:\n")
                                    while True:
                                        if menu < "000" and menu > "004":
                                            print()
                                        elif caseButton == "001":
                                            Menu = {"id": caseButton}
                                            # 读取用例信息
                                            LAR.Send_messege().personageInfo(sk_client=sk_client, data=Menu, Server_msg=Server_msg)
                                            print("' * '为必填项")
                                            C_ProjectName = input("*请输入测试项目名称:\n")
                                            C_CaseName = input("请输入测试用例标题:\n")
                                            get_one = input("查询一条请输入'Y',全部请'回车':\n")
                                            if get_one == "Y" or get_one == "y":
                                                get_one = True
                                            irInfo = {"C_ProjectName": C_ProjectName, "get_one": get_one, "C_CaseName": C_CaseName}
                                            # 执行查询
                                            LAR.Send_messege().reception_Send_messege(sk_client=sk_client, data=irInfo)
                                            break

                                        elif caseButton == "002":
                                            Menu = {"id": caseButton}
                                            # 插入用例信息
                                            LAR.Send_messege().personageInfo(sk_client=sk_client, data=Menu, Server_msg=Server_msg)
                                            print("' * '为必填项")
                                            C_ProjectName = input("*请输入测试项目名称:\n")
                                            C_CaseName = input("*请输入测试用例标题:\n")
                                            C_Url = input("*请输入请求地址(例如:http://www.Kuro.com):\n")
                                            C_Class = input("*请输入接口类型(例如:get):\n")
                                            C_Api = input("*请输入接口API(例如:/Milo):\n")
                                            C_Body = input("请输入接口请求体(不能以Json格式写入，需要压缩后写入):\n")
                                            C_Expectation = input("请输入期望结果状态码:\n")
                                            C_Comment = input("请输入备注:\n")

                                            insertInfo = {
                                                'C_ProjectName': C_ProjectName,
                                                'C_CaseName': C_CaseName,
                                                'C_Url': C_Url,
                                                'C_Class': C_Class,
                                                'C_Api': C_Api,
                                                'C_Body': C_Body,
                                                'C_Expectation': C_Expectation,
                                                'C_Comment': C_Comment,
                                            }
                                            # 执行写入
                                            LAR.Send_messege().reception_Send_messege(sk_client=sk_client, data=insertInfo)
                                            break
                                        elif caseButton == "003":
                                            break
                                        elif caseButton == "004":
                                            Menu = {"id": caseButton}
                                            # 读取用例信息
                                            LAR.Send_messege().personageInfo(sk_client=sk_client, data=Menu, Server_msg=Server_msg)
                                            print("' * '为必填项")
                                            C_ProjectName = input("*请输入测试项目名称:\n")
                                            C_Id = input("*请输入执行测试用例ID:\n")
                                            tokens = input("是否需要输入token，'是'请输入'Y'，'否'请'回车':\n")
                                            if tokens == "Y" or tokens == "y":
                                                TK = input("请输入token信息:\n")
                                            else:
                                                TK = None
                                            irInfo = {"C_ProjectName": C_ProjectName, "C_Id": C_Id, "tokens":TK}
                                            # 执行查询
                                            LAR.Send_messege().reception_Send_messege(sk_client=sk_client, data=irInfo)
                                            break

                                        elif caseButton == "exit" or caseButton == "EXIT":
                                            print("是否确认退出? '是'请输入'y','否'请输入'n'")
                                            caseButtonQ = input("请输入:\n")
                                            if caseButtonQ == "Y" or caseButtonQ == "y":
                                                print("成功退出系统\n")
                                                return
                                            elif caseButtonQ == "N" or caseButtonQ == "n":
                                                break
                                            else:
                                                print("命令输入有误，请重新输入\n")
                                                break
                                        else:
                                            print("命令输入有误，请重新输入\n")
                                            break

                                elif menu == "03":
                                    print("功能待定")
                                    break

                                elif menu == "04":
                                    print("聊天室功能待定")
                                    break

                                elif menu == "exit" or menu == "EXIT":
                                    print("是否确认退出? '是'请输入'y','否'请输入'n'")
                                    menuQ = input("请输入:\n")
                                    if menuQ == "Y" or menuQ == "y":
                                        print("成功退出系统\n")
                                        return
                                    elif menuQ == "N" or menuQ == "n":
                                        break
                                    else:
                                        print("命令输入有误，请重新输入\n")
                                        break
                                else:
                                    print("命令输入有误，请重新输入\n")
                                    break
                    break

                elif Key == "2":
                    RDS = {"id":Key}
                    LAR.Send_messege().personageInfo(sk_client=sk_client, data=RDS, Server_msg=Server_msg)
                    reuserName = input("请输入用户名:\n")
                    rephoneNum = input("请输入手机号码:\n")
                    repassWd = input("请输入密码:\n")
                    redius = {"userName":reuserName,"phoneNum": rephoneNum, "passWd": repassWd}
                    LAR.Send_messege().reception_Send_messege(sk_client=sk_client,data=redius)
                    break

                elif Key == "3":
                    print("密码修改待定\n")
                elif Key == "Q" or Key == "q" or Key == "exit" or Key == "EXIT":
                    print("成功退出系统\n")
                    return
                else:
                    print("命令输入有误，请重新输入...\n")
                    break

    except ConnectionAbortedError as e:
        print("err:", e)



if __name__=="__main__":
    Host = conf.cli_Host
    Port = conf.cli_Port
    client_main()
