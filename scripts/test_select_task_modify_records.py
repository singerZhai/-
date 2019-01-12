import json
import unittest
import requests
from base.base_action import get_url, get_res, edit_appoint_task_msg, end_meeting, delete_by_taskId, start_log, res_log, \
    end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestSelectTaskModifyRecords(unittest.TestCase):

    url = get_url('data', 'select_task_modify_records', 'url')
    res = get_res('data', 'select_task_modify_records', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('任务变更记录查询接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_task_modify_records(self):
        u"""任务变更记录查询接口"""
        taskId, meetingId = edit_appoint_task_msg()
        logger.info('获取taskId和meetingId')
        r = requests.post(self.url, taskId)
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
