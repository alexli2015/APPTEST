#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from selenium.webdriver.common.by import By

"""
设置/搜索
"""
# 搜索框
el_search = (By.ID, "com.android.settings:id/search")
# 输入框
el_input = (By.ID, "android:id/search_src_text")
# 返回键
el_back = (By.CLASS_NAME, "android.widget.ImageButton")

"""
头条登录
"""
# 加号按钮
tt_add_btn = (By.ID, "io.manong.developerdaily:id/tab_bar_plus")
# 密码登录按钮
tt_pwd_login = (By.XPATH, "//*[@text='密码登录']")
# 手机号输入框
tt_phone = (By.ID, "io.manong.developerdaily:id/edt_phone")
# 密码输入框
tt_pwd = (By.ID, "io.manong.developerdaily:id/edt_password")
# 登录按钮
tt_login_btn = (By.ID, "io.manong.developerdaily:id/btn_login")

"""
联系人
"""
# 新增联系人
user_add = (By.ID, "com.android.contacts:id/floating_action_button")
# 本地保存
local_save = (By.XPATH, "//*[@text='本地保存']")
# 联系人姓名
user_name = (By.XPATH, "//*[@text='姓名']")
# 联系人电话
user_phone = (By.XPATH, "//*[@text='电话']")
# 向上导航
user_save = (By.XPATH, "//*[@content-desc='向上导航']")
# 修改按钮
user_edit = (By.ID, "com.android.contacts:id/menu_edit")
# 所有联系人
users = (By.ID, "com.android.contacts:id/cliv_name_textview")