import unittest
import requests

from base.base_action import get_url, get_res, select_task_list_by_create_task, get_first_taskId_by_task_list


class TestGetAppointTaskMsg(unittest.TestCase):

    url = get_url('data', 'get_appoint_task_msg', 'url')
    res = get_res('data', 'get_appoint_task_msg', 'res')

    def test_get_appoint_task_msg(self):
        u"""获取指定任务的详细信息接口"""
        task_list = select_task_list_by_create_task()
        taskId = get_first_taskId_by_task_list(task_list)
        r = requests.post(self.url, taskId)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
