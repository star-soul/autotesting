import os,sys
import json
sys.path.append("/autotesting")


"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:用于client端收发数据信息
"""

class Send_messege:
    #用户信息
    def personageInfo(self,sk_client,data,Server_msg):
        sk_client.sendall(bytes(json.dumps(data).encode("utf-8")))
        self.rep_msg = sk_client.recv(1024).decode('utf-8')
        print(Server_msg.decode('utf-8') + self.rep_msg)

    #收发信息
    def reception_Send_messege(self,sk_client,data):
        sk_client.sendall(bytes(json.dumps(data).encode("utf-8")))
        self.msg = sk_client.recv(10240).decode('utf-8')
        print(json.loads(self.msg)['message'])
        return self.msg



#修改密码
def re_Pwd():
    pass