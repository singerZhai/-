import unittest
import requests
from base.base_action import get_url, get_params, get_res, select_task_list_and_meetingId_by_create_task, \
    get_group_id_by_task_list, end_meeting, delete_by_taskId, get_first_task_id_by_task_list, \
    send_message_group_chat_content


class TestSelectMessageGroupChat(unittest.TestCase):

    url = get_url('data', 'select_message_group_chat', 'url')
    params = get_params('data', 'select_message_group_chat', 'params')
    res = get_res('data', 'select_message_group_chat', 'res')

    def test_select_message_group_chat(self):
        u"""群聊消息查询接口"""
        meetingId, taskId, groupId = send_message_group_chat_content()
        new_params = dict(groupId, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], 200)
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        delete_by_taskId(taskId)
