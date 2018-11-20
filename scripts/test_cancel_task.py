import unittest
import requests
from base.base_action import get_url, get_res, select_task_list_and_meetingId_by_create_task, get_token, end_meeting, \
    get_first_task_id_by_task_list, delete_by_taskId


class TestCancelTask(unittest.TestCase):

    url = get_url('data', 'cancel_task', 'url')
    res = get_res('data', 'cancel_task', 'res')

    def test_cancel_task(self):
        u"""取消任务接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        taskId = get_first_task_id_by_task_list(task_list)
        userToken = get_token()
        params = dict(taskId, **userToken)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        delete_by_taskId(taskId)
