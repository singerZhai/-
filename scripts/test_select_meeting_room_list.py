import unittest
import requests
import json
from base.base_action import get_url, get_res, now_time, start_log, runtime, end_log, get_token, params_log, res_log, \
    assert_equal
from base.logger import Log


class TestSelectMeetingRoomList(unittest.TestCase):

    url = get_url('data', 'select_meeting_room_list', 'url')
    res = get_res('data', 'select_meeting_room_list', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('会议室查询接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_meeting_room_list(self):
        u"""会议室查询接口"""
        userToken = get_token()
        logger.warning(params_log + str(userToken))
        r = requests.post(url=self.url, data=userToken)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
