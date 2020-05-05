import socketserver
import sys,os
import json
sys.path.append("/autotesting")
import src.Server.Logs.logs as log
import src.Server.common.readConfig as conf
import src.Server.common.login_Register_Manage as LRM
import src.Server.caseRequest.interfaceRequest as IR
import src.Server.caseRequest.execute_Case as TEC
logger = log.logger

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:server端主程序
"""

class main(socketserver.BaseRequestHandler):

    def handle(self):

        try:
            while True:
                self.data = self.request.recv(1024).strip()
                print("等待接收客户端信息：\n")
                #接收客户端信息
                print("{}\n".format(self.client_address),str(self.data,encoding="utf-8"))
                if not self.data:
                    print("连接失败")
                    break
                print("类型", type(self.data))
                print("值", json.loads(self.data))

                #登录控制
                if json.loads(self.data)["id"] == "1":
                    self.request.sendall(bytes(" 请登录","utf-8"))
                    while True:
                        self.login = self.request.recv(1024).strip()
                        # #调用登录接口验证
                        res_lm = LRM.loginManage(acceptInfo=self.login)
                        print("res_lm",res_lm)
                        self.request.sendall(bytes(json.dumps(res_lm).encode("utf-8")))
                        break

                #查询测试用例
                if json.loads(self.data)["id"] == "001":
                    self.request.sendall(bytes(" 欢迎查询Case", "utf-8"))
                    while True:
                        self.findCase = self.request.recv(1024).strip()
                        # 调用读取测试用例操作相关接口
                        res_fc = IR.interfaceRequestReadInfo(acceptInfo=self.findCase)
                        print("res_fc", res_fc)
                        self.request.sendall(bytes(json.dumps(res_fc).encode("utf-8")))
                        break

                #写入测试用例
                if json.loads(self.data)["id"] == "002":
                    self.request.sendall(bytes(" 欢迎填写Case", "utf-8"))
                    while True:
                        self.writeCase = self.request.recv(1024).strip()
                        # 调用读取测试用例操作相关接口
                        res_wc = IR.interfaceRequestWriteInfo(acceptInfo=self.writeCase)
                        print("res_wc", res_wc)
                        self.request.sendall(bytes(json.dumps(res_wc).encode("utf-8")))
                        break

                #执行一条测试用例
                if json.loads(self.data)["id"] == "004":
                    self.request.sendall(bytes(" 欢迎测试一条Case", "utf-8"))
                    while True:
                        self.executeOnlyCase = self.request.recv(1024).strip()
                        # 调用读取测试用例操作相关接口
                        res_findOnly = TEC.testFile().date_comtrast(acceptInfo=self.executeOnlyCase)
                        print("res_wc", res_findOnly)
                        self.request.sendall(bytes(json.dumps(res_findOnly).encode("utf-8")))
                        break

                #注册控制
                if json.loads(self.data)["id"] == "2":
                    self.request.sendall(bytes("请注册","utf-8"))
                    while True:
                        self.register = self.request.recv(1024).strip()
                        #调用注册接口
                        res_rm = LRM.registerManage(acceptInfo=self.register)
                        print("res_lm",res_rm)
                        self.request.sendall(bytes(json.dumps(res_rm).encode("utf-8")))
                        break

        except Exception as e:
            logger.error(e)
            print(self.client_address,"连接断开")
        finally:
            self.request.close()

    def setup(self):
        print("before handle,连接建立：",self.client_address)
        self.request.sendall(bytes("ようこそ！ 先輩", "utf-8")) #" + self.client_address[0] + "

    def finish(self):
        logger.error("finish run  after handle")
        print()

if __name__=="__main__":
    print("服务器正在启动...")
    server = socketserver.ThreadingTCPServer((conf.cli_Host, conf.cli_Port), main)
    print("服务器启动成功...")
    server.serve_forever()