import datetime
import random
import string
import time
import traceback
from time import sleep
import requests
import yaml
from MySQL import OpenDB
from base.logger import Log

main_url = ''
path = './data/'


def get_url(file, urls, url_name):
    with open(path + file + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return main_url + result[urls][url_name]


def get_params(file, urls, params):
    with open(path + file + '.yml', encoding='utf-8') as f:
        result = yaml.load(f)
        return result[urls][params]


def get_res(file, urls, res):
    with open(path + file + '.yml', encoding='utf-8') as f:
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
    device_Udid = random_device_Udid()
    new_params = dict(device_Udid, **params)
    print(new_params)
    r = requests.post(url, new_params)
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


def get_meeting_id_with_create_fast_meeting():
    demo_dict = dict()
    url = get_url('data', 'create_fast_meeting', 'url')
    params = get_params('data', 'create_fast_meeting', 'params')
    user_token = get_token()
    new_params = dict(params, **user_token)
    r = requests.post(url, new_params)
    res = r.json()
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


def get_appoint_meeting_msg():
    # 获取指定会议的详细信息
    url = get_url('data', 'get_appoint_meeting_msg', 'url')
    params = get_meeting_id_with_create_fast_meeting()
    r = requests.post(url, params)
    res = r.json()
    return res


def get_meetingid_with_get_appoint_meeting_msg(appoint_meeting_msg):
    # 用获取指定会议信息方法返回的信息来获取meetingId
    meetingId_dict = dict()
    meetingId = appoint_meeting_msg['data']['meeting']['meetingId']
    meetingId_dict['meetingId'] = meetingId
    return meetingId_dict


def get_summaryId_with_get_appoint_meeting_msg(appoint_meeting_msg):
    # 用获取指定会议信息方法返回的信息来获取summaryId
    summaryId_dict = dict()
    summaryId = appoint_meeting_msg['data']['summary']['summaryId']
    summaryId_dict['summaryId'] = summaryId
    return summaryId_dict


def get_task_begin_time():
    new_result = dict()
    res = datetime.datetime.now() + datetime.timedelta(minutes=30)
    result = res.strftime("%Y-%m-%d %H:%M:%S")
    new_result['beginTime'] = result
    return new_result


def get_task_end_time():
    new_result = dict()
    res = datetime.datetime.now() + datetime.timedelta(hours=1)
    result = res.strftime("%Y-%m-%d %H:%M:%S")
    new_result['endTime'] = result
    return new_result


def create_task_in_meeting_and_return_meeting_id():
    url = get_url('data', 'create_task', 'url')
    params = get_params('data', 'create_task', 'params')
    meetingId = get_meeting_id_with_create_fast_meeting()
    beginTime = get_task_begin_time()
    endTime = get_task_end_time()
    userToken = get_token()
    new_params = dict(userToken, **meetingId, **beginTime, **endTime, **params)
    requests.post(url, new_params)
    end_meeting(meetingId)
    return meetingId


def select_task_list_and_meetingId_by_create_task():
    create_task_url = get_url('data', 'create_task', 'url')
    create_task_params = get_params('data', 'create_task', 'params')
    select_url = get_url('data', 'select_task_i_create', 'url')
    select_params = get_params('data', 'select_task_i_create', 'params')
    meetingId = get_meeting_id_with_create_fast_meeting()
    beginTime = get_task_begin_time()
    endTime = get_task_end_time()
    userToken = get_token()
    new_params = dict(userToken, **meetingId, **beginTime, **endTime, **create_task_params)
    requests.post(create_task_url, new_params)
    end_meeting(meetingId)
    userToken = get_token()
    new_params = dict(userToken, **select_params)
    r = requests.post(select_url, new_params)
    res = r.json()
    return res['data']['list'], meetingId


def get_first_task_id_by_task_list(task_list_msg):
    first_task_dict = dict()
    for first_task in task_list_msg:
        first_taskId = first_task['taskId']
        first_task_dict['taskId'] = first_taskId
        return first_task_dict


def get_group_id_by_task_list(task_list_msg):
    first_group_dict = dict()
    first_task = task_list_msg[0]['groupId']
    first_group_dict['groupId'] = first_task
    return first_group_dict


def delete_by_taskId(taskId):
    url = get_url('data', 'delete_by_taskId', 'url')
    userToken = get_token()
    params = dict(taskId, **userToken)
    requests.post(url, params)


def edit_appoint_task_msg():
    url = get_url('data', 'edit_appoint_task_msg', 'url')
    params = get_params('data', 'edit_appoint_task_msg', 'params')
    task_list, meetingId = select_task_list_and_meetingId_by_create_task()
    taskId = get_first_task_id_by_task_list(task_list)
    edit_begin_time = get_task_begin_time()
    edit_end_time = get_task_end_time()
    userToken = get_token()
    new_params = dict(userToken, **taskId, **meetingId, **edit_begin_time, **edit_end_time, **params)
    requests.post(url, new_params)
    return taskId, meetingId


def get_date():
    date_dict = dict()
    now_date = time.strftime('%Y-%m-%d')
    date_dict['date'] = now_date
    return date_dict


def send_message_group_chat_content():
    # 创建任务并且留言，以备查询留言case调用
    url = get_url('data', 'send_message_group_chat_content', 'url')
    params = get_params('data', 'send_message_group_chat_content', 'params')
    task_list_msg, meetingId = select_task_list_and_meetingId_by_create_task()
    groupId = get_group_id_by_task_list(task_list_msg)
    taskId = get_first_task_id_by_task_list(task_list_msg)
    new_params = dict(groupId, **params)
    requests.post(url, new_params)
    return meetingId, taskId, groupId


params_log = '传入参数：'
res_log = '返回数据：'
start_log = '==========start=========='
end_log = '========== end =========='
runtime_log = 'runtime: '
end_meeting_log = '结束会议'
end_task_log = '结束任务'


def now_time():
    result = time.time()
    return result


# 脚本运行时长
def runtime(start_time):
    end_time = time.time()
    result = end_time - start_time
    res = round(result, 2)
    return runtime_log + str(res) + 's'


# 二次封装断言方法
# 加入log
def assert_equal(result, expect):
    try:
        assert str(result) == str(expect)
        global logger
        logger = Log()
        logger.info('断言结果:  ' + str(result) + ' == ' + str(expect))
    except AssertionError:
        s = traceback.format_exc()
        logger.info(s)
        logger.error('断言结果:  ' + str(result) + ' != ' + str(expect))
        raise


def select_sql(sql):
    # 只能查询返回一条完整数据
    with OpenDB() as f:
        # 执行sql
        f.execute(sql)
        # 获取数据
        result = f.fetchall()
        return result


def insert_sql(sql):
    with OpenDB() as f:
        f.execute(sql)


def update_sql(sql):
    with OpenDB() as f:
        f.execute(sql)


def delete_sql(sql):
    with OpenDB() as f:
        f.execute(sql)


# 生成随机字符串作为创建团队的name
def get_random_str(str_length=6):
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(str_length)]
    random_str = ''.join(str_list)
    return random_str


# 调用上面生成随机字符串来添加到字典中,生成teamName参数
def random_team_name():
    team_name = dict()
    random_str = get_random_str()
    team_name['teamName'] = random_str + '(接口测试脚本生成的团队)'
    return team_name


# 调用上面的生成随机字符串方法来添加到字典中,生成Udid参数
def random_device_Udid():
    Udid_dict = dict()
    random_str = get_random_str()
    Udid_dict['deviceUdid'] = random_str
    return Udid_dict


# 获取用户的团队列表
def get_team_list():
    url = get_url('data', 'select_team_and_team_member_list', 'url')
    userToken = get_token()
    r = requests.post(url=url, data=userToken)
    res = r.json()
    result = res['data']['teamList']
    return result


# 获取当前用户的最后一个团队的teamId
# (因为每一个新创建的团队都是在团队列表的最后一个,固返回最后一团队的teamId)
def get_team_id():
    teamId_dict = dict()
    team_list = get_team_list()
    teamId_dict['teamId'] = team_list[-1]['teamId']
    return teamId_dict


# 利用查询团队列表返回的数据提取成员Id
# 同样为最后一个团队中的成员id
def get_id():
    id_dict = dict()
    team_list = get_team_list()
    id_dict['id'] = team_list[-1]['teamMemberList'][-1]['id']
    return id_dict


# 创建团队方法
def create_team():
    url = get_url('data', 'create_team', 'url')
    params = get_params('data', 'create_team', 'params')
    team_name = random_team_name()
    userToken = get_token()
    new_params = dict(userToken, **team_name, **params)
    requests.post(url=url, data=new_params)


# 删除团队方法
def delete_team(teamId):
    url = get_url('data', 'markup_delete_team', 'url')
    requests.post(url=url, data=teamId)


# 添加团队成员方法(供删除删除团队成员接口调用)
def add_team_member(teamId):
    url = get_url('data', 'add_team_member', 'url')
    params = get_params('data', 'add_team_member', 'params')
    userToken = get_token()
    new_params = dict(userToken, **teamId, **params)
    requests.post(url=url, data=new_params)


# 创建订单并返回orderId
def create_times_order_and_return_orderId():
    orderId_dict = dict()
    url = get_url('data', 'create_times_order_by_productId', 'url')
    params = get_params('data', 'create_times_order_by_productId', 'params')
    userToken = get_token()
    new_params = dict(userToken, **params)
    r = requests.post(url=url, data=new_params)
    res = r.json()
    orderId = res['data']['order']['orderId']
    orderId_dict['orderId'] = orderId
    return orderId_dict



if __name__ == '__main__':
    # print(get_url('data', 'login', 'url'))
    # print(get_params('data', 'login', 'params'))
    # print(get_res('data', 'login', 'res'))
    # print(get_token())
    # print(change_back_password_params())
    # # 将密码更改回‘123456’
    # # again_change_password()
    print(sign_in_device_user())
    # print(get_user_id())
    # print(get_meeting_start_time())
    # print(get_meeting_end_time())
    # print(get_appoint_meeting_msg())
    # print(get_meeting_id_with_create_fast_meeting())
    # print(get_date())
    # sql = "select username,password from user where username='lidabao'"
    # res = select_sql(sql)
    # print(res)
    # print(get_random_str())
    # print(random_team_name())
    # print(get_team_list())
    # print(get_team_id())
    # print(get_id())
