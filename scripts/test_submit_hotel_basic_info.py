#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/6/14 18:11 
"""
from time import sleep

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_db import ReadDB
from tools.read_file import read_file


class TestModifyHotelBasicInfo:
    def setup_class(self):
        # 初始化driver
        driver = GetDriver().get_web_driver(page.url)
        # 获取统一入口类对象Pagin
        self.page_in = PageIn(driver)
        # 获取PageLogin对象并登录
        self.page_in.page_get_page_login().page_login_success()
        # 获取PageSysMenu对象进入主界面
        self.menu = self.page_in.page_get_page_sysmenu()
        # 获取PageSubmit对象
        self.submit = self.page_in.page_get_page_submit()

        # def teardown_class(self):
        #     # 关闭driver
        #     GetDriver().quit_web_driver()

    @pytest.mark.parametrize("target_id, expected_status", read_file("hotel_submit_basic_info.yaml"))
    @pytest.mark.run(order=5)
    def test_submit_hotel_basic_info(self, target_id, expected_status):
        # 调用PageSysMenu对象的page_sys_menu业务组合方法进入宾馆主界面
        self.menu.page_sys_menu()
        # 调用PageSubmit的page_submit提交调查表
        self.submit.page_submit(target_id)

        # 数据库断言：验证编号为target_id的记录的proc_status为2-已提交
        sql = "select proc_status from T_BASE_INFO_HOTEL where code = '%s'" % target_id
        result = ReadDB().get_sql_one(sql)
        print("数据库查询的记录是:", result)
        assert result[0] == 2
        print("\n 数据库返回的数据状态为{}".format(result[0]))
        # 界面断言：验证市县待审核列表是否存在指定问卷编号的记录
        assert expected_status == True
        print("问卷编号为{}.format(target_id)的状态为'已提交'")
