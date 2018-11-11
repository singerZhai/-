import allure
import requests
from base.base_action import get_url, get_res, sign_in_device_user, get_user_id


class TestLogoutDeviceUser:

    url = get_url('data', 'logout_device_user', 'url')
    params = get_user_id()
    res = get_res('data', 'logout_device_user', 'res')

    # 注销设备用户
    @allure.step('注销设备用户')
    def test_logout_device_user(self):
        r = requests.post(self.url, self.params)
        r = requests.post(self.url, self.params)
        res = r.json()
        assert r.status_code == 200
        assert res['status'] == self.res['status']
        assert res['msg'] == self.res['msg']