import unittest
import requests
from base.base_action import get_url, get_token, get_res


class TestTaskInterfaceSearchNeedRelevanceMeeting(unittest.TestCase):
    url = get_url('data', 'task_interface_search_need_relevance_meeting', 'url')
    res = get_res('data', 'task_interface_search_need_relevance_meeting', 'res')

    def test_task_interface_search_need_relevance_meeting(self):
        u"""任务界面查询需要关联的会议接口"""
        params = get_token()
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
