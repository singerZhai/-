from base.base_action import select_sql, insert_sql


def login_sign_in():
    while True:
        all_data = select_sql("select username,password from user")
        new_list = list()
        for i in all_data:
            for j in i.values():
                new_list.append(j)
        username = input('请输入用户名：')
        if username in new_list:
            while True:
                password = input('请输入密码：')
                if password == new_list[new_list.index(username) + 1]:
                    print('welcome to %s\'s home' % username)
                    return
                else:
                    print('密码不正确，请重新输入')
        else:
            print('不存在此用户，请选择操作：')
            doing = input('1(注册)    2(退出)')
            if doing == '1':
                while True:
                    new_username = input('请输入用户名：')
                    if len(new_username) > 16:
                        print('用户名不能超过16位字符，请重新输入：')
                        continue
                    else:
                        while True:
                            new_password = input('请输入密码：')
                            if len(new_password) > 16:
                                print('密码不能超出16位字符，请重新输入：')
                                continue
                            else:
                                insert_sql("insert into user(username,`password`) values('%s','%s')" % (new_username, new_password))
                                print('注册成功')
                                break
                        break
            elif doing == '2':
                print('退出成功')
                return


login_sign_in()
