import json
import unittest
import requests
from base.base_action import get_url, get_res, get_params, start_log, res_log, end_log, now_time, runtime, assert_equal, \
    params_log
from base.logger import Log


class TestSelectMeetingModifyRecords(unittest.TestCase):

    url = get_url('data', 'select_meeting_modify_records', 'url')
    params = get_params('data', 'select_meeting_modify_records', 'params')
    res = get_res('data', 'select_meeting_modify_records', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('会议变更记录查询接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_meeting_modify_records(self):
        u"""会议变更记录查询接口"""
        # 将meetingId写死了(9280)，是一个之前做过编辑操作的预约会议
        logger.warning(params_log + str(self.params))
        r = requests.post(self.url, self.params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
