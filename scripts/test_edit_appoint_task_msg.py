import unittest
import requests

from base.base_action import get_url, get_params, get_res, get_task_begin_time, get_task_end_time, get_token, \
    end_meeting, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, delete_by_taskId


class TestEditAppointTaskMsg(unittest.TestCase):
    url = get_url('data', 'edit_appoint_task_msg', 'url')
    params = get_params('data', 'edit_appoint_task_msg', 'params')
    res = get_res('data', 'edit_appoint_task_msg', 'res')

    def test_edit_appoint_task_msg(self):
        u"""编辑指定任务的详细信息接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        taskId = get_first_task_id_by_task_list(task_list)
        edit_begin_time = get_task_begin_time()
        edit_end_time = get_task_end_time()
        userToken = get_token()
        new_params = dict(userToken, **taskId, **meetingId, **edit_begin_time, **edit_end_time, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        delete_by_taskId(taskId)
        end_meeting(meetingId)
