import unittest
import requests

from base.base_action import get_url, get_params, get_res, get_token


class TestSelectTaskICreate(unittest.TestCase):

    url = get_url('data', 'select_task_i_create', 'url')
    params = get_params('data', 'select_task_i_create', 'params')
    res = get_res('data', 'select_task_i_create', 'res')

    def test_select_task_i_create(self):
        u"""查询我创建的任务接口"""
        userToken = get_token()
        new_params = dict(userToken, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
