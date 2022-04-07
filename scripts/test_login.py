#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@File   : .py
@Contact: ocewulf@126.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/22 18:01   ocewulf      1.0         None
"""

from time import sleep
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLogger
from tools.read_file import read_file
import page
log = GetLogger.get_log()


class TestLogin:
    # 初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url)
        # 2.通过统一入口获取PageLogin对象
        self.pl = PageIn(driver).page_get_page_login()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,pwd,expected", read_file("login.yaml"))
    def test_login(self, username, pwd, expected):
        # 调用登录业务方法
        self.pl.page_login(username, pwd)
        sleep(2)
        # 断言
        print("\n 获取的登录用户名是：", self.pl.page_get_login_name())
        try:
            assert expected == self.pl.page_get_login_name()
        except Exception as e:
            log.error("验证失败，错误信息：{}".format(e))
            # 输入错误信息
            print("错误原因:", e)
            # 截图
            self.pl.base_get_img()
            # 抛出异常
            raise
