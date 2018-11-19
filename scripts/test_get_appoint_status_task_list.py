import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token


class TestGetAppointStatusTaskList(unittest.TestCase):

    url = get_url('data', 'get_appoint_status_task_list', 'url')
    params = get_params('data', 'get_appoint_status_task_list', 'params')
    res = get_res('data', 'get_appoint_status_task_list', 'res')

    def test_get_appoint_status_task_list(self):
        u"""获取指定状态的任务列表接口"""
        userToken = get_token()
        new_params = dict(userToken, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
