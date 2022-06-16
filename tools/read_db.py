# 导包
import pymysql
import cx_Oracle as cx

# 新建数据库读取类
class ReadDB:
    # 定义类属性
    conn = None

    # 封装获取连接对象方法 for Mysql
    # def get_conn(self):
    #     if self.conn is None:
    #         self.conn = pymysql.connect(host="10.241.125.6", port=1521, user="ggcsjc", password="ggcsjc",
    #                                     database="ora11g", charset="utf8")
    #     return self.conn

    # 封装获取连接对象方法 for Oracle
    def get_conn(self):
        if self.conn is None:
            self.conn = cx.connect('ggcsjc/ggcsjc@10.241.125.6:1521/ora11g')
        return self.conn

    # 封装获取游标方法
    def get_cur(self):
        return self.get_conn().cursor()

    # 封装关闭游标方法
    def close_cur(self, cursor):
        if cursor:
            cursor.close()

    # 封装关闭连接方法
    def close_conn(self):
        if self.conn:
            self.conn.close()
            # 关闭连接对象后，对象还存在在内存中，需手动设置对象为None
            self.conn = None

    # 封装执行方法 获取单条数据
    def get_sql_one(self, sql):
        # 定义游标对象、数据
        curs = None
        result = None
        try:
            # 获取游标对象
            curs = self.get_cur()
            # 调用执行方法
            curs.execute(sql)
            # 获取执行结果
            result = curs.fetchone()
        except Exception as e:
            print("get_sql_one:", e)
        finally:
            # 关闭游标
            self.close_cur(curs)
            # 关闭连接
            self.close_conn()
            # 返回执行结果
            return result

    # 封装获取所有数据集方法
    def get_sql_all(self, sql):
        curs = None
        results = None
        try:
            # 获取游标
            curs = self.get_cur()
            # 调用执行方法
            curs.execute(sql)
            # 获取执行结果
            results = curs.fetchall()
        except Exception as e:
            print("get_sql_all:", e)
        finally:
            # 关闭游标
            self.close_cur(curs)
            # 关闭连接
            self.close_conn()
            # 返回执行结果
            return results

    # 修改
    def update_sql(self, sql):
        curs = None
        res = None
        try:
            curs = self.get_cur()
            curs.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print("update_sql:", e)
            self.close_cur(curs)
            self.close_conn()
            return res

    def delete_sql(self, sql):
        curs = None
        res = None
        try:
            curs = self.get_cur()
            curs.execute(sql)
            self.conn.rollback()
        except Exception as e:
            self.conn.rollback()
            print("delete_sql:", e)
            self.close_cur(curs)
            self.close_conn()
            return res

    def query_sql(self, sql):
        curs = None
        res = None
        try:
            curs = self.get_cur()
            curs.execute(sql)
            res = curs.fetchone()
        except Exception as e:
            print("query_sql:", e)
            self.close_cur(curs)
            self.close_conn()
            return res

