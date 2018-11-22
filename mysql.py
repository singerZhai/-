from pymysql import connect, cursors


class OpenDB:
    def __init__(self, user='root', password='123456', database='students', charset='utf8'):
        # 初始化
        try:
            self.conn = connect(host='localhost',
                                port=3306, user=user,
                                password=password,
                                database=database,
                                charset=charset)
            self.cs = self.conn.cursor(cursor=cursors.DictCursor)
        except Exception:
            print('数据库连接异常')

    def __enter__(self):
        # 返回游标进行执行操作
        return self.cs

    def __exit__(self):
        # 结束提交数据并关闭数据库
        self.conn.commit()
        self.cs.close()
        self.conn.close()
