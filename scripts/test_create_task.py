import unittest
import requests

from base.base_action import get_url, get_params, get_res, get_task_begin_time, get_task_end_time, get_token, \
    end_meeting, get_meeting_id_with_create_fast_meeting


class TestCreateTask(unittest.TestCase):

    url = get_url('data', 'create_task', 'url')
    params = get_params('data', 'create_task', 'params')
    res = get_res('data', 'create_task', 'res')

    def test_create_task(self):
        u"""创建新的任务接口"""
        meetingId = get_meeting_id_with_create_fast_meeting()
        beginTime = get_task_begin_time()
        endTime = get_task_end_time()
        userToken = get_token()
        new_params = dict(userToken, **meetingId, **beginTime, **endTime, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId)
