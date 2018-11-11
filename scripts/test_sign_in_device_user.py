import pytest
import allure
import requests
from base.base_action import get_url, get_params, get_res


class TestSignInDeviceUser:

    url = get_url('data', 'sign_in_device_user', 'url')
    params = get_params('data', 'sign_in_device_user', 'params')
    res = get_res('data', 'sign_in_device_user', 'res')

    # 注册设备用户接口
    @allure.step('注册设备用户接口')
    def test_sign_in_device_user(self):
        r = requests.post(self.url, self.params)
        res = r.json()
        assert r.status_code == 200
        assert res['status'] == self.res['status']
        assert res['msg'] == self.res['msg']
