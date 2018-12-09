# import os
# import logging
# from time import sleep
#
# path = os.path.dirname(os.path.realpath(__file__))
# print(path)
# demo_path = os.path.join(path, 'demo')
# print(demo_path)
# number = 0
# logger = logging.getLogger()
# ch = logging.StreamHandler()
# formatter = logging.Formatter('[%(asctime)s] - %(levelname)s: %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)
# logger.setLevel(logging.DEBUG)
#
#
# while number <= 100:
#     logger.debug(number)
#     if not os.path.exists(demo_path):
#         os.mkdir(demo_path)
#         logger.info('目录已创建')
#         sleep(1)
#         number += 1
#     else:
#         if os.path.exists(demo_path):
#             os.rmdir(demo_path)
#             logger.info('目录已删除')
#             sleep(1)
#             number += 1
# import shutil
#
# Report_path = './Report/'
# files_count = len(os.listdir(Report_path))
# if files_count > 10:
#      shutil.rmtree(Report_path)
#      os.mkdir(Report_path)
# import datetime
# import time
#
# from jinja2 import runtime
#
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))
# print(time.time())
# print(type(time.time()))
# print(runtime)
#!/usr/bin/python3

from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    name = '小樱'
    t = Thread(target=sayhi,args=(name,), name='first')
    t.start()
    print(t.name)
    s = Thread(target=sayhi, args=('小红',), name='second')
    s.start()
    print(s.name)