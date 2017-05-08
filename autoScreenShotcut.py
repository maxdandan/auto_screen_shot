# coding=utf-8
# __author__ = 'pc_go'

# 自动定时截屏并保存到桌面目录下

import os
import time
import datetime

# 间隔时间
INTERVAL = 3600 * 0.5
save_path = '/Users/pc_go/Desktop/screenShotcuts/'

def mkdirr(dir_path):
    try:
        os.mkdir(dir_path)
    except Exception as e:
        print e
        pass


def doScreenShotcut():
    now = datetime.datetime.now()
    dir_path = "%s%s" % (save_path, now.strftime('%Y%m%d'))
    mkdirr(dir_path)
    file_path = dir_path + "/%d:%d" % (now.hour, now.minute) + '.png'
    os.system("screencapture -t png -T 1 " + file_path)


def run():
    while 1:
        doScreenShotcut()
        time.sleep(INTERVAL)


if __name__ == '__main__':
    run()
