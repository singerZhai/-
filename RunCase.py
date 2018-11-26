import unittest
from HTMLTestReportCN import HTMLTestRunner
import time


if __name__ == '__main__':
    case_path = './scripts/'
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_send_message_group_chat.py')
    # 报告生成路径
    # Report/路径必须提前创建，否则报错
    report_path = './Report/'
    # 获取当前时间
    now_time = time.strftime('%Y-%m-%d %H-%M-%S')
    # 设置报告名称
    report_name = report_path + now_time + '-TestReport.html'
    # 打开并写入报告
    with open(report_name, 'wb') as f:
        # 初始化报告生成对象
        runner = HTMLTestRunner(stream=f, verbosity=2, title='接口测试报告', description='正在编写全部业务接口测试脚本', tester='Mr.Zhai')
        runner.run(discover)
