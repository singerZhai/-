import json
import unittest
import requests

from base.base_action import get_url, get_params, get_summaryId_with_get_appoint_meeting_msg, get_appoint_meeting_msg, \
    get_res, end_meeting, get_meetingid_with_get_appoint_meeting_msg, start_log, params_log, res_log, end_log, now_time, \
    runtime, assert_equal
from base.logger import Log


class TestEditMeetingSummary(unittest.TestCase):
    url = get_url('data', 'edit_meeting_summary', 'url')
    params_summary_text = get_params('data', 'edit_meeting_summary', 'params')
    res = get_res('data', 'edit_meeting_summary', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('编辑会议纪要接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_edit_meeting_summary(self):
        u"""编辑会议纪要接口"""
        appoint_meeting_msg = get_appoint_meeting_msg()
        logger.info('创建会议并获取会议详情')
        summaryId_dict = get_summaryId_with_get_appoint_meeting_msg(appoint_meeting_msg)
        logger.info('获取summaryId')
        meetingId_dict = get_meetingid_with_get_appoint_meeting_msg(appoint_meeting_msg)
        logger.info('获取meetingId')
        params = dict(meetingId_dict, **self.params_summary_text, **summaryId_dict)
        logger.warning(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        end_meeting(meetingId_dict)
        logger.info('结束会议')
