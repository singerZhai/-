import unittest
import requests

from base.base_action import get_url, get_params, get_summaryId_with_get_appoint_meeting_msg, get_appoint_meeting_msg, \
    get_res, end_meeting, get_meetingId_with_get_appoint_meeting_msg


class TestEditMeetingSummary(unittest.TestCase):
    url = get_url('data', 'edit_meeting_summary', 'url')
    params_summary_text = get_params('data', 'edit_meeting_summary', 'params')
    res = get_res('data', 'edit_meeting_summary', 'res')

    def test_edit_meeting_summary(self):
        u"""编辑会议纪要接口"""
        appoint_meeting_msg = get_appoint_meeting_msg()
        summaryId_dict = get_summaryId_with_get_appoint_meeting_msg(appoint_meeting_msg)
        meetingId_dict = get_meetingId_with_get_appoint_meeting_msg(appoint_meeting_msg)
        params = dict(meetingId_dict, **self.params_summary_text, **summaryId_dict)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        end_meeting(meetingId_dict)
