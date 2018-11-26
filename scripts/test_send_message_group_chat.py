import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_group_id_by_task_list, \
    select_task_list_and_meetingId_by_create_task, get_first_task_id_by_task_list, end_meeting, delete_by_taskId, \
    adding_dict


class TestSendMessageGroupChat(unittest.TestCase):
    url = get_url('data', 'send_message_group_chat', 'url')
    # content = get_params('data', 'send_message_group_chat', 'params')['content']
    # fromUsername = get_params('data', 'send_message_group_chat', 'params')['fromUsername']
    # # 将在data中取到的字符串转化为此接口可用的二进制数据
    # content_binary_system = content.encode()
    # fromUsername_dict = dict()
    # fromUsername_dict['fromUsername'] = fromUsername
    # content_dict = dict()
    # content_dict['content'] = content_binary_system
    # params = adding_dict(fromUsername_dict, content_dict)
    params = get_params('data', 'send_message_group_chat', 'params')
    res = get_res('data', 'send_message_group_chat', 'res')

    # @unittest.skipIf(condition=True, reason='二进制问题')
    def test_send_message_group_chat(self):
        u"""群聊消息发送接口"""
        task_list_msg, meetingId = select_task_list_and_meetingId_by_create_task()
        groupId = get_group_id_by_task_list(task_list_msg)
        new_params = dict(groupId, **self.params)
        task_id = get_first_task_id_by_task_list(task_list_msg)
        print(new_params)
        r = requests.post(self.url, params=new_params, headers={'Content-Type':'binary'})
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        delete_by_taskId(task_id)
