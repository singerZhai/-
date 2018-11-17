import unittest
import requests
from base.base_action import get_url, get_params, get_res, appointment_meeting, select_appointment_meeting_msg, \
    get_meeting_start_time, get_meeting_end_time, get_appointment_meetingId, get_meeting_access_code, end_meeting


class TestEditAppointMeetingMsg(unittest.TestCase):

    url = get_url('data', 'edit_appoint_meeting_msg', 'url')
    params = get_params('data', 'edit_appoint_meeting_msg', 'params')
    res = get_res('data', 'edit_appoint_meeting_msg', 'res')

    def test_edit_appoint_meeting_msg(self):
        u"""编辑指定会议的详细信息接口（只允许创建人修改未结束的会议）"""
        # 先预约会议
        appointment_meeting()
        # 由于预约会议没有返回会议详细信息，所以此步骤为获取刚刚预约的会议的详细信息
        appoint_meeting_msg = select_appointment_meeting_msg()
        # 获取meetingId
        meetingId = get_appointment_meetingId(appoint_meeting_msg)
        # 获取会议接入码
        meeting_access_code = get_meeting_access_code(appoint_meeting_msg)
        # 需要更改的会议开始和结束时间
        params_meeting_start_time = get_meeting_start_time()
        params_meeting_end_time = get_meeting_end_time()
        new_params = dict(meetingId, **meeting_access_code, **self.params, **params_meeting_start_time, **params_meeting_end_time)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        # 关闭会议
        end_meeting(meetingId)
