import unittest
import requests
from base.base_action import get_url, get_params, get_res, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, get_token, end_meeting, delete_by_taskId


class TestModifyTaskSchedule(unittest.TestCase):

    url = get_url('data', 'modify_task_schedule', 'url')
    params = get_params('data', 'modify_task_schedule', 'params')
    res = get_res('data', 'modify_task_schedule', 'res')

    def test_modify_task_schedule(self):
        u"""修改任务进度接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        taskId = get_first_task_id_by_task_list(task_list)
        print(taskId)
        userToken = get_token()
        new_params = dict(userToken, **taskId, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        delete_by_taskId(taskId)
        end_meeting(meetingId)
