import datetime
from time import sleep
import requests
import yaml

# main_url = 'http://www.dingchengvideo.cn:8080'
main_url = 'http://www.freevoip.com.cn'
# main_url = '192.168.1.238:8080'


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


def sign_in_device_user():
    url = get_url('data', 'sign_in_device_user', 'url')
    params = get_params('data', 'sign_in_device_user', 'params')
    r = requests.post(url, params)
    res = r.json()
    return res['data']['deviceUser']['userid']


def get_user_id():
    userid = sign_in_device_user()
    demo = dict()
    demo['userid'] = userid
    return demo


def get_meeting_start_time():
    new_result = dict()
    res = datetime.datetime.now() + datetime.timedelta(minutes=30)
    result = res.strftime("%Y-%m-%d %H:%M:%S")
    new_result['preBeginTime'] = result
    return new_result


def get_meeting_id():
    demo_dict = dict()
    url = get_url('data', 'create_fast_meeting', 'url')
    params = get_params('data', 'create_fast_meeting', 'params')
    user_token = get_token()
    new_params = dict(params, **user_token)
    r = requests.post(url, new_params)
    res = r.json()
    # print(res)
    result = res['data']['meetingId']['meetingId']
    demo_dict['meetingId'] = result
    return demo_dict


def get_meeting_end_time():
    new_result = dict()
    res = datetime.datetime.now() + datetime.timedelta(hours=1)
    result = res.strftime("%Y-%m-%d %H:%M:%S")
    new_result['preEndTime'] = result
    return new_result


def end_meeting(meetingId_dict):
    del_meeting_url = get_url('data', 'delete_appointment_meeting_record', 'url')
    new_userToken = get_token()
    delete_meeting_params = adding_dict(new_userToken, meetingId_dict)
    requests.post(del_meeting_url, delete_meeting_params)


def adding_dict(dict1, dict2):
    # 将两个字典遍历，然后加到第三个字典中并return
    demo_dict = dict()
    for k, v in dict1.items():
        demo_dict[k] = v
    for k, v in dict2.items():
        demo_dict[k] = v
    return demo_dict


def select_appointment_meeting_msg():
    # 获取预约会返回的会议相关信息
    url = get_url('data', 'meeting_status_search_with_me', 'url')
    params = get_params('data', 'meeting_status_search_with_me', 'params')
    userToken = get_token()
    new_params = adding_dict(params, userToken)
    r = requests.post(url, new_params)
    res = r.json()
    return res


def get_appointment_meetingId(appointment_meeting_msg):
    # 利用预约会议的信息来获取meetingId
    demo_dict = {}
    demo_list = appointment_meeting_msg['data']['list']
    for dict in demo_list:
        int_meetingId = dict['meetingId']
        demo_dict['meetingId'] = int_meetingId
        return demo_dict


def get_meeting_access_code(appointment_meeting_msg):
    # 利用预约会议的信息来获取会议接入码
    demo_dict = {}
    demo_list = appointment_meeting_msg['data']['list']
    for dict in demo_list:
        int_meeting_access_code = dict['meetingAccessCode']
        demo_dict['meetingAccessCode'] = int_meeting_access_code
        return demo_dict


def appointment_meeting():
    # 预约会议方法
    url = get_url('data', 'appointment_meeting', 'url')
    params = get_params('data', 'appointment_meeting', 'params')
    preBeginTime = get_meeting_start_time()
    preEndTime = get_meeting_end_time()
    user_token = get_token()
    new_params = dict(params, **preBeginTime, **preEndTime, **user_token)
    requests.post(url, new_params)


def create_fast_meeting():
    # 快速创建会议
    url = get_url('data', 'create_fast_meeting', 'url')
    params = get_params('data', 'create_fast_meeting', 'params')
    meetingId_dict = dict()
    user_token = get_token()
    new_params = dict(params, **user_token)
    r = requests.post(url, new_params)
    res = r.json()
    result = res['data']['meetingId']['meetingId']
    meetingId_dict['meetingId'] = result
    return meetingId_dict


if __name__ == '__main__':
    # print(get_url('data', 'login', 'url'))
    # print(get_params('data', 'login', 'params'))
    # print(get_res('data', 'login', 'res'))
    # print(get_token())
    # print(change_back_password_params())
    # # 将密码更改回‘123456’
    # # again_change_password()
    # print(sign_in_device_user())
    # print(get_user_id())
    print(get_meeting_start_time())
    print(get_meeting_end_time())
