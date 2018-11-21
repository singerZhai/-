import pymysql


def mysql_select(sql):
    try:
        db = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456',
                             port=3306,
                             database='students',
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
    select_sql = 'select * from students where studentNo = "001"'
    res = mysql_select(select_sql)
    print(res['name'])
    assert res['name'] == '王昭君'
    print('测试结束')
