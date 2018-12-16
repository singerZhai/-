import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, select_task_list_and_meetingId_by_create_task, \
    get_group_id_by_task_list, delete_by_taskId, get_first_task_id_by_task_list, end_meeting, start_log, params_log, \
    res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestSendMessageGroupChatContent(unittest.TestCase):

    url = get_url('data', 'send_message_group_chat_content', 'url')
    params = get_params('data', 'send_message_group_chat_content', 'params')
    res = get_res('data', 'send_message_group_chat_content', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('群聊文本消息发送接口（不支持图片）')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_send_message_group_chat_content(self):
        u"""群聊文本消息发送接口（不支持图片）"""
        task_list_msg, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('获取任务列表和meetingId')
        groupId = get_group_id_by_task_list(task_list_msg)
        logger.info('获取groupId')
        taskId = get_first_task_id_by_task_list(task_list_msg)
        logger.info('获取taskId')
        new_params = dict(groupId, **self.params)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.info(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        delete_by_taskId(taskId)
        logger.info('结束任务')
        end_meeting(meetingId)
        logger.info('结束会议')
