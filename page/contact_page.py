#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from commonlib.base import Base
import page
import allure


class Contact(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def contact_list(self):
        return [ele.text for ele in self.find_elements(page.users)]

    def click_add(self):
        self.click_element(page.user_add)

    def click_local_save(self):
        self.click_element(page.local_save)

    def add_contact(self, name, phone):
        allure.attach("描述", f"输入姓名{name}")
        self.send_data(page.user_name, name)
        allure.attach("描述", f"输入手机号{phone}")
        self.send_data(page.user_phone, phone)
        allure.attach("描述", "点击添加页返回按钮")
        self.click_element(page.user_save)
        if name or phone:
            if self.is_disp(page.user_edit):
                allure.attach("描述", "点击手机返回按钮")
                self.driver.keyevent(4)


