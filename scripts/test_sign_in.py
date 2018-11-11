import allure
import pytest
import requests
from base.base_action import get_url, get_params, get_res


class TestSignIn:

    sign_in_url = get_url('data', 'sign_in', 'url')
    sign_in_params = get_params('data', 'sign_in', 'params')
    sign_in_res = get_res('data', 'sign_in', 'res')

    # 用户注册接口
    @pytest.mark.skipif(condition=True, reason='万能验证码')
    @allure.step('用户注册接口测试')
    def test_sign_in(self):
        r = requests.post(self.sign_in_url, self.sign_in_params)
        res = r.json()
        assert r.status_code == 200
        assert res['status'] == self.sign_in_res['status']
        assert res['msg'] == self.sign_in_res['msg']
