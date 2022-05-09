#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/7 23:00 
"""
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestModifyHotelBasicInfo():
    def setup_class(self):
        # 初始化driver
        driver = GetDriver().get_web_driver(page.url)
        # 获取统一入口类对象Pagin
        self.pagein = PageIn(driver)
        # 获取PageLogin对象并登录
        self.pagein.page_get_page_login()
        # 获取PageSysMenu对象
        self.menu = pagein.page_get_page_sysmenu()

    def teardown_class(self):
        # 关闭driver
        pass

    def test_modify_hotel_basic_info(self):
        pass

