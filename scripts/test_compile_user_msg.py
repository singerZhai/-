import allure
import requests

from base.base_action import get_url, get_params, get_token, get_res


class TestCompileUserMsg:

    url = get_url('data', 'compile_user_msg', 'url')
    userToken = get_token()
    params = get_params('data', 'compile_user_msg', 'params')
    new_params = dict(params, **userToken)
    res = get_res('data', 'compile_user_msg', 'res')

    # 编辑用户信息接口
    @allure.step('编辑用户信息接口')
    def test_compile_user_msg(self):
        r = requests.post(self.url, self.new_params)
        res = r.json()
        assert res['status'] == res['status']
        assert res['msg'] == res['msg']


if __name__ == '__main__':
    TestCompileUserMsg().test_compile_user_msg()