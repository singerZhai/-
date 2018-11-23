import unittest
import requests
from base.base_action import get_url, get_params, get_res


class TestSendMessageGroupChat(unittest.TestCase):

    url = get_url('data', 'send_message_group_chat', 'url')
    params = get_params('data', 'send_message_group_chat', 'params')
    res = get_res('data', 'send_message_group_chat', 'res')

    def test_send_message_group_chat(self):
        u"""群聊消息发送接口"""
        groupId =