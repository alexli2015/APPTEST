#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import pytest
import allure
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from commonlib.driver import init_driver
from commonlib.read_data import read_yaml
from page.pageopt import Page


def get_para():
    user_dic = read_yaml("user_data.yaml").get("User_Data")
    return [(k, user_dic[k]["name"], user_dic[k]["phone"], user_dic[k]["expect"]) for k in user_dic]


class TestContact(object):
    def setup_class(self):
        self.pkg = 'com.android.contacts'
        self.act = '.activities.PeopleActivity'
        self.driver = init_driver(self.pkg, self.act)
        # 声明我们的driver对象
        self.contact_obj = Page(self.driver).to_contact()

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="点击添加新联系人")   # 不会显示该提示信息
    @pytest.fixture()
    def before(self):
        self.contact_obj.click_add()

    @allure.step(title="添加联系人信息")
    @pytest.mark.usefixtures("before")
    @pytest.mark.parametrize("test_num, name, phone, expect", get_para())
    def test_001(self, test_num, name, phone, expect):
        print(test_num)
        self.contact_obj.add_contact(name, phone)
        if name or phone:
            assert expect in self.contact_obj.contact_list()
        else:
            assert expect not in self.contact_obj.contact_list()
