import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, \
    select_task_list_and_meetingId_by_create_task, get_group_id_by_task_list, params_log, res_log, assert_equal, \
    end_meeting, delete_by_taskId, get_first_task_id_by_task_list
from base.logger import Log


class TestResetUnreadCountGroupChat(unittest.TestCase):

    url = get_url('data', 'reset_unread_count_group_chat', 'url')
    params = get_params('data', 'reset_unread_count_group_chat', 'params')
    res = get_res('data', 'reset_unread_count_group_chat', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    @unittest.skipIf(condition=True, reason='接口返回请求失败')
    def test_reset_unread_count_group_chat(self):
        u"""群聊消息已读回执"""
        task_list_msg, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('创建会议和任务获取task_list_msg')
        groupId = get_group_id_by_task_list(task_list_msg)
        logger.info('获取groupId')
        taskId = get_first_task_id_by_task_list(task_list_msg)
        new_params = dict(self.params, **groupId)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, data=new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        logger.info('关闭会议')
        delete_by_taskId(taskId)
        logger.info('结束任务')
