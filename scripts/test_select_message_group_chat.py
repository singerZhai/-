import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, end_meeting, delete_by_taskId, \
    send_message_group_chat_content, start_log, params_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestSelectMessageGroupChat(unittest.TestCase):

    url = get_url('data', 'select_message_group_chat', 'url')
    params = get_params('data', 'select_message_group_chat', 'params')
    res = get_res('data', 'select_message_group_chat', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('群聊消息查询接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_message_group_chat(self):
        u"""群聊消息查询接口"""
        meetingId, taskId, groupId = send_message_group_chat_content()
        logger.info('获取meetingId、taskId、groupId')
        new_params = dict(groupId, **self.params)
        logger.warning(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        logger.info('结束会议')
        delete_by_taskId(taskId)
        logger.info('结束任务')
