#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/6/22 14:13 
"""
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_db import ReadDB
from tools.read_file import read_file


class TestAuditHotelBasicInfo(object):
    def setup_class(self):
        # 初始化浏览器
        driver = GetDriver().get_web_driver(page.url)
        # 初始化统一入口类对象PageIn
        self.page_in = PageIn(driver)
        # 通过PageIn对象调用登录，登录系统
        self.page_in.page_get_page_login().page_login_success()
        # 初始化PageSysMenu对象，调用page_sys_menu()方法点击
        self.page_in.page_get_page_sysmenu().page_sys_menu()
        # 初始化PageAuditHotelBasicInfo对象
        self.page_audit = self.page_in.page_get_page_audit()

    def teardown_class(self):
        # 关闭浏览器
        self.driver = GetDriver().quit_web_driver()

    @pytest.mark.parametrize('input_id', read_file('hotel_audit_basic_info.yaml'))
    def test_audit_hotel_basic_info(self, input_id):
        # 调用审批组合方法page_audit_hotel_basic
        self.page_audit.page_audit_hotel_basic(input_id)

        # 断言数据库-数据状态为2
        sql = "select PROC_STATUS from T_BASE_INFO_HOTEL where CODE = '%s'" % input_id
        result = ReadDB().get_sql_one(sql)
        # PROC_STATUS为3-省级待审核
        assert result[0] == 4
