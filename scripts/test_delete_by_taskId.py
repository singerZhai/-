import unittest
import requests
from base.base_action import get_url, get_res, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, get_token, end_meeting, delete_by_taskId


class TestDeleteByTaskId(unittest.TestCase):

    url = get_url('data', 'delete_by_taskId', 'url')
    res = get_res('data', 'delete_by_taskId', 'res')

    def test_delete_by_taskId(self):
        u"""删除指定的任务记录接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        taskId = get_first_task_id_by_task_list(task_list)
        userToken = get_token()
        params = dict(userToken, **taskId)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        delete_by_taskId(taskId)
