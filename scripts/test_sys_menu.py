#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/3/26 19:52 
"""
from time import sleep

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page


class TestSysMenu:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver().get_web_driver(page.url)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # self.pl = PageIn(driver).page_get_page_login()
        # 获取PageLogin对象并调用登录成功方法
        self.page_in.page_get_page_login().page_login_success()

        # 获取PageSysMenu页面对象
        sleep(3)
        self.menu = self.page_in.page_get_page_sysmenu()

    # 结束
    def teardown_class(self):
        GetDriver().quit_web_driver()

    # 进入菜单页面
    def test_access_menu(self):
        # 调用打开菜单页面方法
        self.menu.page_sys_menu()
        # 断言
        print(self.page_in.driver.title)
        assert self.page_in.driver.title == "公共场所监测"
