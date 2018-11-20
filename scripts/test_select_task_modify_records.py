import unittest
import requests
from base.base_action import get_url, get_res, edit_appoint_task_msg, end_meeting, delete_by_taskId


class TestSelectTaskModifyRecords(unittest.TestCase):

    url = get_url('data', 'select_task_modify_records', 'url')
    res = get_res('data', 'select_task_modify_records', 'res')

    def test_select_task_modify_records(self):
        u"""任务变更记录查询接口"""
        taskId, meetingId = edit_appoint_task_msg()
        r = requests.post(self.url, taskId)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        delete_by_taskId(taskId)
