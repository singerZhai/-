import requests
import yaml

main_url = 'http://www.freevoip.com.cn'


def get_url(path, urls, url_name):
    with open('../data/' + path + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return main_url + result[urls][url_name]


def get_params(path, urls, params):
    with open('../data/' + path + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return result[urls][params]


def get_res(path, urls, res):
    with open('../data/' + path + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return result[urls][res]


def get_token():
    login_url = get_url('data', 'login', 'url')
    login_params = get_params('data', 'login', 'params')
    r = requests.post(login_url, login_params)
    res = r.json()['data']
    demo = dict()
    for i, j in res:
        if i == 'userToken':
            demo.


if __name__ == '__main__':
    print(get_url('data', 'login', 'url'))
    print(get_params('data', 'login', 'params'))
    print(get_res('data', 'login', 'res'))
    print(get_token())
