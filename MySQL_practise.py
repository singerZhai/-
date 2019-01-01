from base.base_action import select_sql, insert_sql, update_sql, delete_sql


class UserData(object):

    @staticmethod
    def __get_all_data():
        __all = select_sql("select username,password from user")
        __new_list = list()
        for i in __all:
            for j in i.values():
                __new_list.append(j)
        all_data_list = __new_list
        all_data = dict(zip(all_data_list[0::2], all_data_list[1::2]))
        return all_data

    def __sign_in(self):
        while True:
            all_data = self.__get_all_data()
            new_username = input('请输入用户名：')
            if new_username not in all_data:
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
                            if new_password != new_username:
                                insert_sql(
                                    "insert into user(username,`password`) values('%s','%s')" % (new_username, new_password))
                                print('注册成功')
                                return True
                            else:
                                print('密码不能与用户名完全相同')
                                continue
            elif new_username in all_data:
                print('%s用户已存在' % new_username)
                continue

    def login(self):
        while True:
            __all_data = self.__get_all_data()
            username = input('请输入用户名：')
            if username in __all_data:
                while True:
                    password = input('请输入密码：')
                    # 判断密码是否等于输入的username所对应的下标加1的对应的密码
                    if password == __all_data[username]:
                        print('welcome to %s\'s home' % username)
                        return username
                    else:
                        print('密码不正确，请重新输入')
            else:
                print('不存在此用户，请选择操作：')
                while True:
                    doing = input('1(注册)    2(退出)')
                    if doing == '1':
                        self.__sign_in()
                        break
                    elif doing == '2':
                        print('退出成功')
                        return False
                    else:
                        print('输入有误，请重新输入：')
                        continue

    def doing(self):
        username = self.login()
        if username:
            while True:
                while True:
                    print('请输入操作：')
                    flag = input('1(更改密码), 2(删除), 3(退出)')
                    if flag == '1':
                        while True:
                            new_password = input('password：')
                            if 0 < len(new_password) <= 16:
                                update_sql(
                                    "update user set password='%s' where username='%s'" % (new_password, username))
                                print('修改成功')
                                break
                            else:
                                print('密码长度不能超过16位')
                                continue
                    elif flag == '2':
                        delete_sql("delete from user where username='%s'" % username)
                        print('删除成功')
                        return
                    elif flag == '3':
                        print('退出成功')
                        return
                    else:
                        print('输入有误')
                        continue


user_data = UserData()
user_data.doing()
