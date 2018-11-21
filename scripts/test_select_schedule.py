import unittest
import requests
from base.base_action import get_url, get_res, get_date, get_token


class TestSelectSchedule(unittest.TestCase):

    url = get_url('data', 'select_schedule', 'url')
    res = get_res('data', 'select_schedule', 'res')

    def test_select_schedule(self):
        u"""获取用户指定日期的日程列表接口"""
        now_date = get_date()
        print(now_date)
        userToken = get_token()
        params = dict(userToken, **now_date)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
