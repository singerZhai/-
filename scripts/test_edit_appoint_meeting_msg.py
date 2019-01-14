import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, appointment_meeting, select_appointment_meeting_msg, \
    get_meeting_start_time, get_meeting_end_time, get_appointment_meetingId, get_meeting_access_code, end_meeting, \
    start_log, params_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestEditAppointMeetingMsg(unittest.TestCase):

    url = get_url('data', 'edit_appoint_meeting_msg', 'url')
    params = get_params('data', 'edit_appoint_meeting_msg', 'params')
    res = get_res('data', 'edit_appoint_meeting_msg', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('编辑指定会议的详细信息接口（只允许创建人修改未结束的会议）')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_edit_appoint_meeting_msg(self):
        u"""编辑指定会议的详细信息接口（只允许创建人修改未结束的会议）"""
        # 先预约会议
        appointment_meeting()
        logger.info('预约会议')
        # 由于预约会议没有返回会议详细信息，所以此步骤为获取刚刚预约的会议的详细信息
        appoint_meeting_msg = select_appointment_meeting_msg()
        logger.info('获取预约会议信息')
        # 获取meetingId
        meetingId = get_appointment_meetingId(appoint_meeting_msg)
        logger.info('通过预约会议信息获取meetingId')
        # 获取会议接入码
        meeting_access_code = get_meeting_access_code(appoint_meeting_msg)
        logger.info('获取会议接入码')
        # 需要更改的会议开始和结束时间
        params_meeting_start_time = get_meeting_start_time()
        params_meeting_end_time = get_meeting_end_time()
        new_params = dict(meetingId, **meeting_access_code, **self.params, **params_meeting_start_time, **params_meeting_end_time)
        logger.warning(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        # 关闭会议
        end_meeting(meetingId)
        logger.info('关闭会议')
