import pymysql


def mysql_select(sql):
    try:
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456',
                             port=3306,
                             database='iwebshop',
                             charset='utf8')
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        # print('打开')
        cur.execute(sql)
        data = cur.fetchone()
        return data
    except Exception:
        print('Error:数据库连接异常！！！！！！')
    finally:
        cur.close()
        db.close()
        # print('数据库已关闭连接')


if __name__ == '__main__':
    select_sql = 'select * from iwebshop_user where username = "singer"'
    res = mysql_select(select_sql)
    print(res)
    assert res['id'] == 2
    print('测试结束')
