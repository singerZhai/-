import unittest
import requests
from base.base_action import get_url, get_params, get_res, select_task_list_and_meetingId_by_create_task, \
    get_group_id_by_task_list, delete_by_taskId, get_first_task_id_by_task_list, end_meeting


class TestSendMessageGroupChatContent(unittest.TestCase):

    url = get_url('data', 'send_message_group_chat_content', 'url')
    params = get_params('data', 'send_message_group_chat_content', 'params')
    res = get_res('data', 'send_message_group_chat_content', 'res')

    def test_send_message_group_chat_content(self):
        u"""2．群聊文本消息发送接口（不支持图片）"""
        task_list_msg, meetingId = select_task_list_and_meetingId_by_create_task()
        groupId = get_group_id_by_task_list(task_list_msg)
        taskId = get_first_task_id_by_task_list(task_list_msg)
        new_params = dict(groupId, **self.params)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        delete_by_taskId(taskId)
        end_meeting(meetingId)
