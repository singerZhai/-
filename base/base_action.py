from time import sleep
import requests
import yaml

main_url = 'http://www.freevoip.com.cn'


def get_url(path, urls, url_name):
    with open('./data/' + path + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return main_url + result[urls][url_name]


def get_params(path, urls, params):
    with open('./data/' + path + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return result[urls][params]


def get_res(path, urls, res):
    with open('./data/' + path + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return result[urls][res]


def change_back_password_params():
    with open('./data/data.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return result['change_password']['change_back_password']['params']


def get_token():
    sleep(2)
    login_url = get_url('data', 'login', 'url')
    login_params = get_params('data', 'login', 'params')
    r = requests.post(login_url, login_params)
    res = r.json()['data']['userToken']
    demo = dict()
    demo['userToken'] = res
    sleep(2)
    return demo


def change_password_get_token(username, password):
    sleep(2)
    login_url = get_url('data', 'login', 'url')
    login_params = {'username': username, 'password': password}
    r = requests.post(login_url, login_params)
    res = r.json()['data']['userToken']
    demo = dict()
    demo['userToken'] = res
    sleep(2)
    return demo


def again_change_password():
    url = get_url('data', 'change_password', 'url')
    userToken = change_password_get_token('15611066631', '654321')
    change_params = change_back_password_params()
    params = dict(change_params, **userToken)
    # 防止频繁调用登陆接口获取userToken衍生出的“token无效”问题
    try:
        r = requests.post(url, params)
        res = r.json()
        if res['status'] == 200:
            return
    except Exception:
        while True:
            new_token = get_token()
            new_params = dict(change_params, **new_token)
            new_r = requests.post(url, new_params)
            new_res = new_r.json()
            if new_res['status'] == 200:
                return


if __name__ == '__main__':
    # print(get_url('data', 'login', 'url'))
    # print(get_params('data', 'login', 'params'))
    # print(get_res('data', 'login', 'res'))
    # print(get_token())
    # print(change_back_password_params())
    again_change_password()
