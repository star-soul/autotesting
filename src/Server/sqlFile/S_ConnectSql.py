import sys
sys.path.append("/autotesting")
import mysql.connector
import src.Server.common.readConfig as rc
import src.Server.Logs.logs as log

logger = log.logger

"""
    @Author:alex-jiang
    @CreateTime: 2020/5/1
    @UpdateTime:
    @model:数据库增删改查
"""

class Database():

    #初始化数据库
    def __init__(self,host=rc.myIp,db=rc.myDb,port=rc.myPort,user=rc.myUser,
                 passwd=rc.myPwd,auth_plugin=rc.myAuth_plugin):
        self.host = host
        self.db = db
        self.port = port
        self.user = user
        self.passwd = passwd
        self.auth_plugin = auth_plugin

    #链接数据库
    def connect_Data_Table(self):

        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                db=self.db,
                port=self.port,
                auth_plugin=self.auth_plugin)

            print("数据库连接成功")
            self.cursor = self.conn.cursor()
            return True
        except mysql.connector.Error as e:
            logger.error("connectDatabase failed, %s" % e)
            return False






    # 插入数据
    def Insert_Sql(self, table, val_obj):
        self.connect_Data_Table()

        sql_top = 'insert into ' + table + '('
        sql_tail = ') values ('
        try:
            for key, val in val_obj.items():
                sql_top += key + ','
                sql_tail += "\'" + val + "\'" + ','
            sql = sql_top[:-1] + sql_tail[:-1] + ')'
            self.conn.cursor().execute(sql)
            self.conn.commit()
            print("插入数据成功")
            self.close()
            return sql
        except mysql.connector.Error as e:
            self.conn.rollback()
            print("插入数据失败, %s" % e)
            return False

        # self.close()

    def query_Sql(self, table, field, asslgn=None, get_one=False):
        self.connect_Data_Table()

        try:
            query_res = 'SELECT {field} FROM {table}'.format(field=field,table=table)
            if asslgn:
                query_res = 'SELECT {field} FROM {table} WHERE {asslgn}'.format(field=field, table=table,asslgn=asslgn)

            self.cursor.execute(query_res)
            col_name_list = [tuple[0] for tuple in self.cursor.description]
            # print(len(col_name_list))
            if get_one:
                result = self.cursor.fetchone()
            else:
                result = self.cursor.fetchall()
            print("查询成功")
            self.close()
            return col_name_list, result#返回结果
        except mysql.connector.Error as e:
            logger.error("query result failed, %s" % e)
            self.close()
            return False

    def update_Sql(self, table, field, asslgn=None):
        self.connect_Data_Table()

        try:
            update_res = 'UPDATE {field} SET {table}'.format(field=field,table=table)
            if asslgn:
                update_res = 'UPDATE {table} SET {field} WHERE {asslgn}'.format(field=field, table=table,asslgn=asslgn)

            self.conn.cursor().execute(update_res)
            self.conn.commit()
            print("数据更新成功")
            self.close()
            return update_res  #返回结果
        except mysql.connector.Error as e:
            self.conn.rollback()
            logger.error("query result failed, %s" % e)
            self.close()
            return False

    # 关闭数据库连接
    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except:
            logger.error("databasesClose failed")



if __name__=='__main__':
    Database()