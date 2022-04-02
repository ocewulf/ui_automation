#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@File   : .py
@Contact: ocewulf@126.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/22 17:22   ocewulf      1.0         None
"""
import page
from base.base import Base
from time import sleep

from tools.get_log import GetLogger

log = GetLogger.get_log()


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类输入方法
        self.base_input(page.username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.pwd, pwd)

    # # 输入验证码
    # def page_input_code(self, code):
    #     self.base_input(page.code, code)

    # 点击登录
    def page_click_login_btn(self):
        sleep(2)
        self.base_click(page.login_btn)

    # 获取登录用户名
    def page_get_login_name(self):
        return self.base_get_text(page.login_name)

    # 组合业务方法 -> 测试脚本层调用
    def page_login(self, username, pwd):
        log.info("正在进行登录操作，用户名：{}，密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        # self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法 -> 进入子系统依赖方法
    def page_login_success(self, username="hn_ggcs001", pwd="Abcd1234"):
        log.info("正在进行登录操作，用户名：{}，密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        # self.page_input_code(code)
        self.page_click_login_btn()

