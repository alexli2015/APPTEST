#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from appium import webdriver


def init_driver(pkg, act):
    """
    生成driver对象
    :param pkg: app包名
    :param act: app启动名
    :return: driver对象
    """
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.237.102:5555'
    # app的信息
    desired_caps['appPackage'] = pkg
    desired_caps['appActivity'] = act
    # 不要在会话前重置应用状态
    desired_caps["noReset"] = True
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 返回driver对象
    return webdriver.Remote('http://192.168.0.106:4723/wd/hub', desired_caps)
